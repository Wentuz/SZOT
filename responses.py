from random import choice, randint

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'So... You\'re not very talkative person'
    elif 'hello' in lowered:
        return 'Ohaio !'
    elif 'bye' in lowered:
        return 'ci@o !'
    elif 'roll' in lowered:
        return f'You rolled {randint(1,6)} !'
    else:
        return choice(['Sorry... What ?',
                        'I don\'t get it...',
                        'What are you talking about ?'])