from google import genai
from google.genai import types


API_KEY = "AIzaSyBvgsku1Ie3LWvx7W04Vi3XiQysqf8t9Fw"

config = types.GenerateContentConfig(
    system_instruction="Учитель боевых искуств"
)

client = genai.Client(api_key=API_KEY)

while True:
    user = input("you:")
    
    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = user,
        config = config,    
    )
    
    answer = response.text
    print(answer)