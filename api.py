from flask import Flask, request, jsonify
from flask_cors import CORS

import stripe

stripe.api_key = 'secret'

app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)


@app.route('/', methods=['GET'])
def home():
    return "<h1> Flask API </h1>"

@app.route('/api/acept_payment', methods=['POST'])
def acept_payment():
    data = request.get_json()
    amount = 2000
    payment = stripe.PaymentIntent.create(
        amount=amount*100,
        currency='mxn',
        payment_method=data['payment_method'],
        payment_method_types=["card"],
        off_session=True,
        confirm=True
    )
    print(payment)
    return payment

app.run(ssl_context=('cert.pem', 'key.pem'))
