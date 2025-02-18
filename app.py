from flask import Flask, request, jsonify
import random

app = Flask(__name__)

quotes = [
    "The best way to predict the future is to invent it.",
    "Life is 10% what happens to us and 90% how we react to it.",
    "The only way to do great work is to love what you do."
]

@app.route('/')
def home():
    return "Welcome to the Quotes API! Go to /quote to get a random quote."

@app.route('/quote', methods=['GET'])
def get_quote():
    return jsonify({
        'quote': random.choice(quotes)
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
