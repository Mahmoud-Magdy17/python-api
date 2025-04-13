from flask import Flask, request
from gradio_client import Client

app = Flask(__name__)

# Gradio client setup
client = Client("mahmoud176203/chat_bot")

@app.route('/')
def index():
    return 'Send a GET request to /askAi?text=your_message'

@app.route('/askAi')
def ask_ai():
    text = request.args.get('text')
    if not text:
        return 'Please provide a "text" parameter in the URL.'

    try:
        result = client.predict(
            message=text,
            system_message="You are a friendly Chatbot.",
            max_tokens=512,
            temperature=0.7,
            top_p=0.95,
            api_name="/chat"
        )
        return result
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
