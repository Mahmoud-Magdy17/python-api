from gradio_client import Client

client = Client("mahmoud176203/chat_bot")

def handler(request):
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
