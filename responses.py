from random import choice
from roll_dice import get_roll
from num_guess import guess_number
from gen_num import generate_number
from readWH import read_WH


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()


    if lowered == '':
        return 'So... You\'re not very talkative person'
    elif 'hello' in lowered:
        return 'Ohaio !'
    elif lowered[1] == 'w' and lowered[2] == 'h':
        return read_WH(lowered)
    elif 'generate' in lowered:
        number:int = generate_number()
        return f'Generating number...{number}'
    elif lowered[1] == 'r':
        return get_roll(lowered)
    elif lowered[1] == 'g':
        return guess_number(lowered, generate_number())
    elif 'help' in lowered:
        return '1. !wh (file_name) - quick encyclopedia, write list in filename for more\n2. !r (2d20) - roll a die\n3. !generate - generate number\n4. !g (number) - guess a number'
    #else:
    #    return choice(['Sorry... What ?',
    #                    'I don\'t get it...',
    #                    'What are you talking about ?'])