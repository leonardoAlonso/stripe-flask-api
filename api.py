from flask import Flask, request, jsonify

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1> Flask API </h1>"

@app.route('/api/acept_payment', methods=['POST'])
def acept_payment():
    data = request.get_json()
    print(data)
    return {'ff':'ff'}

app.run()