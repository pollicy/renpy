init python:
    import json
    import requests

    API_URL = "http://127.0.0.1:4001/api/v1/story/generate_story" 
    #connects renpy and api 
    
    API_HEADERS = {
        "Content-Type": "application/json",
        # "Authorization": "Bearer YOUR_API_KEY"
    }

    def call_backend(character, question):
        payload = {
            "character": character,
            "question": question
        }

        try:
            response = requests.post(API_URL, headers=API_HEADERS, json=payload)
            data = response.json()
            return data.get("answer", "The API returned no answer.")
        
        except Exception as e:
            return f"Error contacting API: {e}"
