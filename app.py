from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
import datetime
# from app.chatbot.chatbot_bourntec import out
from app.chatbot_ml_model_bourntec.main import chat_with_ml

app = Flask(__name__)

# Replace <YOUR_CONNECTION_STRING> with your MongoDB connection string
client = MongoClient(
    "mongodb+srv://rudraprasadmohapatra51:AJkCE0Qb9UEXbUfX@chatbot.738aw0x.mongodb.net/"
)

db = client["Chatbot"]  # Replace "your_database_name" with your database name

collection = db["user_queries"]


def log_user_query(query):
    try:
        # Insert user query into the MongoDB collection
        log_entry = {"query": query, "timestamp": datetime.datetime.utcnow()}
        collection.insert_one(log_entry)
    except ServerSelectionTimeoutError as e:
        print("Failed to log user query to MongoDB:", e)


@app.route("/ping", methods=["GET"])
def ping():
    # out("message")
    return jsonify({"response": "pong"})


@app.route("/")
def index():
    return render_template("chat_ui.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    query = data.get("query")

    # Log the user query to MongoDB
    log_user_query(query)

    # Use your chatbot logic from the chatbot_logic module

    # response = out(query)
    response = chat_with_ml(query)

    return jsonify({"response": response})


if __name__ == "__main__":
    try:
        client.server_info()
        print("Connected to MongoDB")
    except ServerSelectionTimeoutError as e:
        print("Failed to connect to MongoDB:", e)

    print("Server running at port: 5005")
    app.run(host="127.0.0.1", port=5005, debug=True, use_reloader=True)