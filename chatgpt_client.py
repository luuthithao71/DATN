import os
from openai import OpenAI

# Modify OpenAI's API key and API base to use vLLM's API server.
openai_api_key = os.getenv("openai_api_key")
openai_api_base = os.getenv("openai_api_base")

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=openai_api_key,
    base_url=openai_api_base + "/v1/",
)

models = client.models.list()
model = models.data[0].id

def request_chat_gpt(user_message):
    try:
        completion = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": user_message}
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""  # Return an empty string or handle the error appropriately