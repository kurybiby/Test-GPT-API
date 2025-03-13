from flask import Flask, render_template, request

from generate_message import generate_message
from generate_image import generate_image

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def main():
    return render_template('main.html')


@app.route('/message', methods = ['POST'])
def answer_user():
    user_request = request.form.get('user_request')
    print(generate_message(user_request))
    
    return render_template('main.html')


@app.route('/image', methods = ['POST'])
def image():
    user_request = request.form.get('user_request')
    print(generate_image(user_request))
    return render_template('main.html')


if __name__ == '__main__':
    app.run(debug = True)