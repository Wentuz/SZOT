from random import choice
from roll_dice import get_roll
from num_guess import guess_number
from gen_num import generate_number


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()


    if lowered == '':
        return 'So... You\'re not very talkative person'
    elif 'hello' in lowered:
        return 'Ohaio !'
    #elif 'bye' in lowered:
    #    return 'ci@o !'
    elif 'generate' in lowered:
        number:int = generate_number()
        return f'Generating number...{number}'
    elif lowered[1] == 'r':
        return get_roll(lowered)
    elif lowered[1] == 'g':
        return guess_number(lowered, generate_number())
    
    #else:
    #    return choice(['Sorry... What ?',
    #                    'I don\'t get it...',
    #                    'What are you talking about ?'])