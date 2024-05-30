import os
import g4f
# models = client.models.list()
model = "gpt-4o"

def request_chat_gpt(user_message):
    try:
        completion = g4f.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "user", "content": user_message}
            ]
        )
        return completion
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Empty Msg!"  # Return an empty string or handle the error appropriately
