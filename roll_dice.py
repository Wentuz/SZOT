from random import randint
import re

def get_roll(num_dice, value_dice) -> int:
    
    result = []

    while num_dice > 0:
        value:int = randint(1, value_dice)
        print(value)
        num_dice = num_dice - 1

        result.append(value)

    return result

if __name__ == '__main__':
    get_roll(3, 20)