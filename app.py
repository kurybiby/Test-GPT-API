from flask import Flask, render_template, request

from generate_message import generate_message
from generate_image import generate_image

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def main():
    return render_template('main.html')


@app.route('/text_generation', methods = ['GET', 'POST'])
def text_generation():
    user_request = request.form.get('user_request')
    print(generate_message(user_request))
    
    return render_template('text_generation.html')


@app.route('/image_generation', methods = ['GET', 'POST'])
def image_generation():
    user_request = request.form.get('user_request')
    print(generate_image(user_request))
    return render_template('image_generation.html')


if __name__ == '__main__':
    app.run(debug = True)