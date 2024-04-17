from roll_dice import get_roll
from num_guess import guess_number
from gen_num import generate_number
import play
import json

def get_help() -> str:
    file_path:str = "help.json"
    with open(file_path, 'r') as file:
        library:list = json.load(file)
    
    response = ''

    for x in library:
        response = response + '' + library[x]

    #print(response)
    return response


def get_response_command(user_input: str) -> str:
    lowered: str = user_input.lower()


    if lowered == '':
        return 'Somehow you\'ve send an empty command'
    elif lowered[1] == 'p':
        return play(lowered)
    elif 'generate' in lowered:
        number:int = generate_number()
        return f'Generating number...{number}'
    elif lowered[1] == 'r':
        return get_roll(lowered)
    elif lowered[1] == 'g':
        return guess_number(lowered, generate_number())
    elif 'help' in lowered:
        return get_help()
    #else:
    #    return choice(['Sorry... What ?',
    #                    'I don\'t get it...',
    #                    'What are you talking about ?'])