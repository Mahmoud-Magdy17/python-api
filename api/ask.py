from gradio_client import Client
from urllib.parse import parse_qs

client = Client("mahmoud176203/chat_bot")

def handler(request):
    try:
        # Parse query string manually
        query_params = parse_qs(request.query_string.decode())
        text_list = query_params.get('text', [])

        if not text_list:
            return "Please provide a 'text' parameter in the URL."

        text = text_list[0]

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
        import traceback
        return traceback.format_exc()
