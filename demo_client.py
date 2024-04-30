from openai import OpenAI

# Modify OpenAI's API key and API base to use vLLM's API server.
openai_api_key = ""
openai_api_base = "https://06bf-34-83-127-218.ngrok-free.app"

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=openai_api_key,
    base_url=openai_api_base + "/v1/",
)

models = client.models.list()
model = models.data[0].id

# Your code here

# chat_completion = client.chat.completions.create(
#     messages=[{
#         "role": "system",
#         "content": "You are a helpful assistant."
#     }, {
#         "role": "user",
#         "content": "Who won the world series in 2020?"
#     }, {
#         "role": "assistant",
#         "content": "The Los Angeles Dodgers won the World Series in 2020."
#     }, {
#         "role": "user",
#         "content": "Where was it played?"
#     }],
#     model=model,
# )

# print("Chat completion results:")
# print(chat_completion)

completion = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "user", "content": "Bạn là ai?"}
    ]
)

print(completion.choices[0].message.content)