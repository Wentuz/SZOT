from random import choice





def get_response_command(user_input: str) -> str:
    lowered: str = user_input.lower()


    if lowered == '':
        return 'Somehow you\'ve send an empty command'
    else:
        return choice(['Sorry... What ?',
                        'I don\'t get it...',
                        'What are you talking about ?'])