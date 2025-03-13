from flask import Flask, render_template, request

from generate_message import generate_message


app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def main():
    return render_template('main.html')


@app.route('/message', methods = ['POST'])
def answer_user():
    user_request = request.form.get('user_request')
    print(generate_message(user_request))
    return render_template('main.html')


if __name__ == '__main__':
    app.run(debug = True)