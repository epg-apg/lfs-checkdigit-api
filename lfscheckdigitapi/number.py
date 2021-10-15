from flask import (
    Blueprint, escape
)

from .checkdigit import calculateCheckDigit

bp = Blueprint('number', __name__, url_prefix='/number')


@bp.route('/<int:number>', methods=['GET'])
def number(number):
    return {
        "input": int(number),
        "checkDigit": calculateCheckDigit(str(number))
    }
