from gradio_client import Client
from urllib.parse import parse_qs

client = Client("mahmoud176203/chat_bot")

def handler(request):
    try:
        query_params = parse_qs(request.query_string.decode())
        text_list = query_params.get('text', [])
        
        if not text_list:
            return {"error": "Missing 'text' parameter"}, 400
        
        text = text_list[0]
        
        # Add timeout to prevent hanging
        result = client.predict(
            message=text,
            system_message="You are a friendly Chatbot.",
            max_tokens=512,
            temperature=0.7,
            top_p=0.95,
            api_name="/chat",
            timeout=30  # 30 second timeout
        )
        return {"response": result}
        
    except Exception as e:
        # Return a proper error response
        return {"error": str(e)}, 500