from random import choice, randint
import re


def guess_number(user_input: str, generated_number: int) -> str:
    num:str = ''
    for char in user_input:
        if char.isdigit():
            num = num + char
    
    if int(num) == generated_number:
        return f"Viola ! That's the number :3"
    elif int(num) > generated_number:
        return f"Too big. It was {generated_number}"
    elif int(num) < generated_number:
        return f"Too shmall. It was {generated_number}"


if __name__ == '__main__':
    print(guess_number('!g 12',23))
    print(guess_number('!g 423',423))
    print(guess_number('!g 30',20))
