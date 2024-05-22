import spacy
import numpy as np
import pickle
import argparse

# Example for cmd line usage: "python3 analyzeSpacy.py --filepath data.pkl --indices 0 1 2 --dep_type nsubj --top_n 1"

def load_data(filepath):
    """Load data from a pickle file."""
    try:
        with open(filepath, 'rb') as file:
            data = pickle.load(file, encoding="latin1", fix_imports=True)
        return data
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return None

def dependency_pairs(sentence, dep_type):
    """Use spaCy to parse the sentence and return indices of word pairs with the specified dependency type."""
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(sentence)
    pairs = []
    for token in doc:
        if token.dep_ == dep_type:
            head_idx = token.head.i + 1  # Convert to 1-based index to align with attention indices
            token_idx = token.i + 1
            pairs.append((token_idx, head_idx))
    return pairs

def find_top_attention_pairs(sentence_data, dep_type, top_n=1):
    words = sentence_data['words']
    sentence = " ".join(words)  # Reconstruct sentence from words
    dep_pairs = dependency_pairs(sentence, dep_type)  # Get dependency pairs of the specified type
    attns = sentence_data['attns']
    num_layers = len(attns)
    num_heads = len(attns[0])

    attn_dict = {}
    for layer in range(num_layers):
        for head in range(num_heads):
            attn_matrix = np.array(attns[layer][head])
            np.fill_diagonal(attn_matrix, 0)  # Remove self-attention

            for (i, j) in dep_pairs:
                attn_value = attn_matrix[i, j]
                if (i, j) not in attn_dict or attn_value > attn_dict[(i, j)][0]:
                    attn_dict[(i, j)] = (attn_value, layer, head)

    sorted_pairs = sorted(attn_dict.items(), key=lambda x: x[1][0], reverse=True)[:top_n]
    top_pairs = []
    for pair, details in sorted_pairs:
        word1, word2 = words[pair[0] - 1], words[pair[1] - 1]  # Convert 1-based back to 0-based
        attn_value, layer, head = details
        top_pairs.append((word1, word2, attn_value, layer, head))
    return top_pairs

def process_sentences(data, indices, dep_type, top_n=1):
    results = {}
    for index in indices:
        sentence_data = data[index]
        top_pairs = find_top_attention_pairs(sentence_data, dep_type, top_n)
        results[index] = top_pairs
    return results

def main():
    parser = argparse.ArgumentParser(description='Analyze attention in sentences based on given file path.')
    parser.add_argument('--filepath', type=str, help='the file path of the pickle data file')
    parser.add_argument('--indices', type=int, nargs='*', help='indices of sentences to analyze')
    parser.add_argument('--dep_type', type=str, help='dependency type to filter pairs')
    parser.add_argument('--top_n', type=int, default=1, help='number of top attended pairs to display (default: 1)')

    args = parser.parse_args()
    data = load_data(args.filepath)
    if data is None:
        return
    
    results = process_sentences(data, args.indices, args.dep_type, args.top_n)
    for sentence_index, pairs in results.items():
        print(f"Sentence Index: {sentence_index}")
        for word1, word2, attn, layer, head in pairs:
            print(f"Top attended pair: '{word1}' to '{word2}' with attention {attn} found at layer {layer}, head {head}")

if __name__ == '__main__':
    main()
