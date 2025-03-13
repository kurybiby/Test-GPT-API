from flask import Flask, render_template, request

from generate_message import generate_message
from generate_image import generate_image

app = Flask(__name__)

chat_history = []

@app.route('/', methods = ['GET', 'POST'])
def main():
    return render_template('main.html')


@app.route('/text_generation', methods = ['GET', 'POST'])
def text_generation():
    user_request = request.form.get('user_request')
    bot_response = generate_message(user_request)
    chat_history.append({'role': 'user', 'text': user_request})
    chat_history.append({'role': 'bot', 'text': bot_response})

    return render_template('text_generation.html', chat_history = chat_history)


@app.route('/image_generation', methods = ['GET', 'POST'])
def image_generation():
    image_url = None  
    if request.method == 'POST':
        user_request = request.form.get('user_request')
        if user_request:  
            image_url = generate_image(user_request) 

    return render_template('image_generation.html', image_url=image_url)


if __name__ == '__main__':
    app.run(debug = True)