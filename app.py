from flask import Flask, render_template, request, jsonify
from app.chatbot.chatbot_bourntec import out

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    # out("message")
    return jsonify({'response': "pong"})

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    query = data.get('query')
    # print("--------------------------------------------------------------------------------",data)
    # print("--------------------------------------------------------------------------------",query)
    # Use your chatbot logic from the chatbot_logic module

    response = out(query)

    return jsonify({'response': response})

@app.route('/')
def index():
    return render_template('chat_ui.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5005, debug=True)

