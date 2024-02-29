from openai import openAI

def chatfun(user_input: str) -> str: 
    messages = []
    sys_msg = {"role": "system", "content": "You are a helpful bot named Miko."}
    messages.append(sys_msg)

    while True:
        usr_msg = {"role": "user", "content": user_input}
        messages.append(usr_msg)
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                                messages=messages)
        reply = response["choices"][0]["message"]["content"]
        print("\n"+reply+"\n")
        assistant_msg = {"role": "assistant", "content": reply}
        messages.append(assistant_msg)

if __name__ == '__main__':
    chatfun()