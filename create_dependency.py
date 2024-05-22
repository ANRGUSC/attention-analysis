import spacy

def process_file(input_file_path, output_file_path):
    # Load the English NLP model
    nlp = spacy.load("en_core_web_sm")
    
    # Open the input file and the output file
    with open(input_file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    with open(output_file_path, 'w', encoding='utf-8') as out_file:
        # Process the text using spaCy
        doc = nlp(text)
        
        for sent in doc.sents:
            for token in sent:
                # Calculate index relative to the sentence
                #print(token.dep_)
                #print(token.text)
                head_idx = token.head.i - sent.start + 1
                if token == token.head:  # This checks if the token is the root of the sentence
                    head_idx = 0  # Convention for root word
                # Write to output file
                out_file.write(f"{token.text} {head_idx}-{token.dep_}\n")
            # Write an empty line after each sentence
            out_file.write("\n")


    



# Example usage
input_path = '/Users/buckethoop/GitHub/BERTPROJ/attention-analysis-master/depparse/output_sentences.txt'
output_path = '/Users/buckethoop/GitHub/BERTPROJ/attention-analysis-master/word_dependencies.txt'
process_file(input_path, output_path)
