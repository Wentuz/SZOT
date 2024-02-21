from random import randint
import re

def get_roll(user_input: str) -> int:
    tab:int = re.findall(r'\d+', user_input)
    
    tab:int = list(map(int, tab))
    
    num_dice:int = tab[0]
    num_size:int = tab[1]
    result = []

    while num_dice > 0:
        value:int = randint(1, num_size)
        print(value)
        num_dice = num_dice - 1

        result.append(value)

    return result