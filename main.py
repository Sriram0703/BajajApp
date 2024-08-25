import os
from flask import Flask, request, jsonify
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)

app.wsgi_app = ProxyFix(app.wsgi_app)

@app.route('/bfhl', methods=['POST'])
def handle_post():
    data = request.json.get('data', [])
    user_id = "john_doe_17091999"  # Replace with your logic to generate the user_id
    email = "john@xyz.com"
    roll_number = "ABCD123"
    
    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha()]
    lowercase_alphabets = [item for item in data if item.islower()]
    highest_lowercase_alphabet = max(lowercase_alphabets) if lowercase_alphabets else []

    response = {
        "is_success": True,
        "user_id": user_id,
        "email": email,
        "roll_number": roll_number,
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": [highest_lowercase_alphabet] if highest_lowercase_alphabet else []
    }
    return jsonify(response)

@app.route('/bfhl', methods=['GET'])
def handle_get():
    return jsonify({"operation_code": 1})

if __name__ == '__main__':
    app.run(debug=True)