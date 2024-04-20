import random
import json


file_path = 'prompts_art.json'

def get_art_prompt(appearance_num: int, emotion_num: int, action_num: int) -> str:


    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        responses = data.get(file_path, [])

        random_response = random.choice(responses)

        return random_response
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == '__main__':
    print(get_art_prompt(1,2,3))
    print(get_art_prompt(0,3,0))