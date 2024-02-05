from random import choice


def guess_number(user_input, generated_number) -> str:
    value_tab = user_input.split()
    guessed_number = int(value_tab[1])
    goal = int(generated_number)
    if guessed_number == goal:
        return choice(['Bravo ! You\'ve got it correct !',
                       'Congrats m8. Randal is by your side',
                       'Beginners luck',
                       'Oho see who is lucky today !'])
    elif guessed_number < goal:
        return choice(['Try a higher number',
                       'A little greater number',
                       'Small numbers... Try something bigger',
                       'minimum polish wage'])
    else:
        return choice(['Try a lower number',
                       'Not that high',
                       'Unlike this guess, snoop dog can never be too high'])