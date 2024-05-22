import pickle

def load_pickle(file_path):
    try:
        with open(file_path, 'rb') as file:
            return pickle.load(file, encoding="latin1", fix_imports=True)
    except Exception as e:
        print(f"Failed to load the pickle file: {e}")
        return None
    
def write_to_text(data, file_path):
    try:
        with open(file_path, 'w') as file:
            for item in data:
                file.write(f"{item}\n")
    except Exception as e:
        print(f"Failed to write to text file: {e}")
# /Users/buckethoop/GitHub/BERTPROJ/attention-analysis-master/unlabeled_attn.pkl
# /Users/buckethoop/GitHub/BERTPROJ/attention-analysis-master/data/depparse/dev_attn.pkl 42 1286 13 1671 111 244 192 680 975 979
if __name__ == "__main__":
    file_path1 = '/Users/buckethoop/GitHub/BERTPROJ/attention-analysis-master/depparse/word_dependencies_attn.pkl'  # Replace with your pickle file path
    data1 = load_pickle(file_path1)
    
    #if data1 is not None:
    #    write_to_text(data1, file_path1.replace(".pkl", ".txt"))
    #print("Data1")
    print(data1[13]["words"])
    print(data1[13]["tokens"])
    #print(data1[13]["attns"])
    print(len(data1))
    
    file_path2 = '/Users/buckethoop/GitHub/depparse/dev_attn.pkl' 
    data2 = load_pickle(file_path2)   
    #if data2 is not None:
    #    write_to_text(data2, file_path2.replace(".pkl", ".txt"))
    print("Data2")
    print(data2[13]["words"])
    print(data2[13]["tokens"])
    #print(data2[13]["attns"])
    print(len(data2))

    '''
    file_path3 = '/Users/buckethoop/GitHub/BERTPROJ/attention-analysis-master/depparse/word_dependencies_attn(max).pkl' 
    data3 = load_pickle(file_path3)
    print("Data3")
    print(data3[6]["attns"][0])

    file_path4 = '/Users/buckethoop/GitHub/BERTPROJ/attention-analysis-master/data/depparse/dev_attn.pkl' 
    data4 = load_pickle(file_path4)
    print("Data4")
    print(data4[111]["attns"][0])
    '''

'''
import json

# Specify the path to your JSON file
file_path = '/Users/buckethoop/GitHub/BERTPROJ/attention-analysis-master/output_sentences.json'

# Open and read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)

# Check the type of the parsed data
if isinstance(data, list):
    # If it's a list, print the number of entries
    print(f'The JSON file contains {len(data)} entries.')
'''