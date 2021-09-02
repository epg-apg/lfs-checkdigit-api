import sentry_sdk
from flask import Flask, abort
from sentry_sdk.integrations.flask import FlaskIntegration
from .checkdigit import calculateCheckDigit

sentry_sdk.init(
    dsn="https://9dbd1798137d41778fa81ba3203b92a1@o340050.ingest.sentry.io/5942394",
    integrations=[FlaskIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # By default the SDK will try to use the SENTRY_RELEASE
    # environment variable, or infer a git commit
    # SHA as release, however you may want to set
    # something more human-readable.
    # release="myapp@1.0.0",
)
app = Flask(__name__)

@app.route('/barcode/<int:number>', methods=['GET'])
def barcode(number):
    if len(str(number)) != 12:
        abort(400, '12 digits are required')

    return 'barcode'

@app.route('/number/<int:number>', methods=['GET'])
def number(number):
    return {
        "input": number,
        "checkDigit": calculateCheckDigit(str(number))
    }
