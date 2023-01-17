from flask import Flask, render_template, request
from functionality import convert_message_to_morse_code, MORSE_CODE_DICT

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/morse-code', methods=['GET', 'POST'])
def morse_coded_message():
    message = request.form['message'].upper()
    resulting_morse_message = convert_message_to_morse_code(MORSE_CODE_DICT, message)
    return render_template('result.html', html_morse_message=resulting_morse_message)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
