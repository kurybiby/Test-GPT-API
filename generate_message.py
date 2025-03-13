from g4f import Client

client = Client()

def generate_message(user_request: str) -> str:
    response = client.chat.completions.create(
        model = 'gpt-4o-mini',
        messages = [{'role': 'user', 'content': f'{user_request}'}],
        web_search = False
    )
    return response.choices[0].message.content