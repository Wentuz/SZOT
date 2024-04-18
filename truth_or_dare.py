import json
import random


def get_truth_or_dare(user_input: int) -> str:

    if user_input == 1:
        file_path = 'dares'
    else:
        file_path = 'truths'
    
    try:
        with open(file_path + '.json', 'r') as file:
            data = json.load(file)
        
        responses = data.get(file_path, [])

        random_response = random.choice(responses)

        return random_response
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == '__main__':
    print(get_truth_or_dare(1))
    print(get_truth_or_dare(0))