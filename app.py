from os import abort
from flask import Flask

app = Flask(__name__)

def calculateCheckDigit(number):
    checkDigit = 0
    sum = 0
    i = 0

    for digit in map(int, number):
        i += 1
        if i % 2 == 0:
            sum += digit
        else:
            sum += digit * 3

    checkDigit = 10 - sum % 10

    return checkDigit

@app.route('/barcode/<int:number>', methods=['GET'])
def barcode(number):
    if len(str(number)) != 12:
        abort(400, "12 digits are required")

    return 'barcode'

@app.route('/number/<int:number>', methods=['GET'])
def number(number):
    return {
        "input": number,
        "checkDigit": calculateCheckDigit(str(number))
    }

@app.route('/')
def index():
    return 'Index Page'

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
