from flask import Flask

app = Flask(__name__)

def calculateCheckDigit(number):
    checkDigit = 0
    return checkDigit

@app.route('/barcode/<int:number>', methods=['GET'])
def barcode():
    return 'barcode'

@app.route('/number/<int:number>', methods=['GET'])
def number(number):
    return f'Number {number}'

@app.route('/')
def index():
    return 'Index Page'
