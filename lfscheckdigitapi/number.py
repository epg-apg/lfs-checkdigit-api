from flask import (
    Blueprint, abort
)

from .checkdigit import calculateCheckDigit

bp = Blueprint('number', __name__, url_prefix='/number')


@bp.route('/<number>', methods=['GET'])
def number(number):
    intNumber = 0
    try:
        intNumber = int(number)
    except:
        abort(400)
        
    return {
        "input": intNumber,
        "checkDigit": calculateCheckDigit(number)
    }
