import pickle
import json

def load_pkl_file(file_path):
    with open(file_path, 'rb') as file:
        data = pickle.load(file, encoding="latin1", fix_imports=True)
    return data

def extract_words(data):
    words_list = []
    for entry in data:
        words = entry['words']
        sentence = ' '.join(words)
        words_list.append({'words': words})
    return words_list

def main():
    # Replace with your .pkl file path
    pkl_file_path = 'data/depparse/dev_attn.pkl'
    
    # Replace with your output .txt file path
    output_file_path = 'output_sentences.json'
    
    data = load_pkl_file(pkl_file_path)
    words_list = extract_words(data)
    
    # Write sentences to the output file
    with open(output_file_path, 'w') as output_file:
        json.dump(words_list, output_file, indent=4)
        print(f"Number of entries: {len(words_list)}")

if __name__ == '__main__':
    main()
