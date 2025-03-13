from g4f import Client

client = Client()

def generate_image(user_request: str) -> str:
    response = client.images.generate(
        model = 'flux',
        prompt = f'{user_request}',
        response_format = 'url'

    )
    return response.data[0].url