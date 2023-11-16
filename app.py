from flask import Flask, request, jsonify
from app.chatbot.chatbot_bourntec import get_response,out

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    query = data.get('query')
    # print("--------------------------------------------------------------------------------",data)
    # print("--------------------------------------------------------------------------------",query)
    # Use your chatbot logic from the chatbot_logic module

    response = out(query)

    return jsonify({'response': response})

@app.route('/ping', methods=['GET'])
def ping():
    # out("message")
    return jsonify({'response': "pong"})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5005, debug=True)

