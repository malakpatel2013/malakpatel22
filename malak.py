from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def home():
    return send_from_directory(os.path.dirname(__file__), 'malak.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')

    # Simple response logic - you can replace this with actual AI integration
    if 'hello' in user_message.lower():
        response = "Hello! Nice to meet you!"
    elif 'hi' in user_message.lower():
        response = "Hi there! What's up?"
    elif 'i am fine' in user_message.lower():
        response = "That's great to hear! How can I help you today?"
    elif 'who are you' in user_message.lower():
        response = "I'm a chatbot created to assist malak!"
    elif 'what can you do' in user_message.lower():
        response = "I can chat with you and answer simple questions!"
    elif 'tell me a joke' in user_message.lower():
        response = "Why don't scientists trust atoms? Because they make up everything!"
    elif 'what is your name' in user_message.lower():
        response = "I don't have a name yet, but you can call me MalakBot!"
    elif 'how are you' in user_message.lower():
        response = "I'm doing well, thank you for asking! How about you?"
    elif 'bye' in user_message.lower():
        response = "Goodbye! Have a great day!"
    else:
        response = f"You said: {user_message}. That's interesting!"

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
