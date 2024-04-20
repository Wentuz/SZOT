import random
import json


file_path = 'prompts_art.json'

def get_art_prompt(appearance_num: int, emotion_num: int, action_num: int) -> str:


    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        

        appearance = data.get("appearance", [])
        emotion = data.get("emotion", [])
        action = data.get("action", [])


        response = ""
        

        while appearance_num > 0:
            response = response + " " + random.choice(appearance)
            appearance_num = appearance_num - 1
        while emotion_num > 0:
            response = response + " "+ random.choice(emotion)
            emotion_num = emotion_num - 1
        while action_num > 0:
            response = response + " " + random.choice(action)
            action_num = action_num - 1


        return response
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == '__main__':
    print(get_art_prompt(1,2,3))
    print(get_art_prompt(0,3,0))