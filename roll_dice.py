from random import randint
import re

def get_roll(user_input: str):
    integers = re.findall(r'\d+', user_input)
    
    integers = list(map(int, integers))
    
    num_dice = integers[0]
    num_size = integers[1]
    result = []

    while num_dice > 0:
        value = randint(1, num_size)
        print(value)
        num_dice = num_dice - 1

        result.append(value)

    return result