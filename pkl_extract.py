import pickle

def load_pkl_file(file_path):
    with open(file_path, 'rb') as file:
        data = pickle.load(file, encoding="latin1", fix_imports=True)
    return data

def reconstruct_sentence(data):
    sentences = []
    for entry in data:
        words = entry['words']
        sentence = ' '.join(words)
        sentences.append(sentence)
    return sentences

def main():
    # Replace with your .pkl file path
    pkl_file_path = '/Users/buckethoop/GitHub/BERTPROJ/attention-analysis-master/data/depparse/dev_attn.pkl'
    
    # Replace with your output .txt file path
    output_file_path = 'output_sentences.txt'
    
    data = load_pkl_file(pkl_file_path)
    reconstructed_sentences = reconstruct_sentence(data)
    
    # Write sentences to the output file
    with open(output_file_path, 'w') as output_file:
        for sentence in reconstructed_sentences:
            output_file.write(sentence + '\n')

if __name__ == '__main__':
    main()
