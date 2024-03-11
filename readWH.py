import json

def read_WH(user_input: str) -> str:

    file_path:str = "WHlib.json"
    with open(file_path, 'r') as file:
        library:list = json.load(file)
    
    cut_lib = user_input[4:]
    lib = library[f'{cut_lib}']
    response = ''

    for x in lib:
        response = response + '' + lib[x]

    print(response)
    return response

if __name__ == '__main__':
    read_WH("!wh mbasic")