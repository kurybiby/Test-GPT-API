from g4f import Client

client = Client()

response = client.images.generate(
    model = 'flux',
    prompt = 'Anime girl falling from high building and crying',
    response_format = 'url'

)
print(response.data[0].url)