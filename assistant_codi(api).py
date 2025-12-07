import requests
import json
URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

API_KEY = "AIzaSyC-eHVTwBrAY5TkZ3gaUvvBoN2f2D87jFY"

headers = {
    "Content-Type": "application/json",
    "X-goog-api-key" : API_KEY,
}

payload = {
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
  }

response = requests.post(URL, headers=headers, json=payload)
print(response.json())




