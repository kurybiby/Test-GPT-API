from g4f import Client

client = Client()

response = client.chat.completions.create(
    model = 'gpt-4o-mini',
    messages = [{'role': 'user', 'content': 'По каким критериям блокировать пользователей?'}],
    web_search = False
)
print(response.choices[0].message.content)