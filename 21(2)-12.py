import os
from google import genai
from google.genai import types

# --- ---
API_KEY = ""  
MODEL_ID = "gemini-2.0-flash"
LOG_FILE = "history.txt"

client = genai.Client(api_key=API_KEY)

def save_to_log(user_text, assistant_text):
    """Функція для запису діалогу в файл history.txt"""
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"USER: {user_text}\n")
        f.write(f"ASSISTANT: {assistant_text}\n")
        f.write("-" * 30 + "\n")

def start_chat(instruction):
    """Функція для створення або перезапуску чату з новою інструкцією"""
    config = types.GenerateContentConfig(system_instruction=instruction)
    return client.chats.create(model=MODEL_ID, config=config)

# Початкова інструкція
current_instruction = "Ти — дружній асистент, який пояснює складне простими словами."
chat = start_chat(current_instruction)

print("--- Асистент готовий до роботи! ---")
print("Команди: /style <стиль> — змінити роль, /clearlog — очистити історію")

while True:
    user_input = input("\nВи: ").strip()

    if not user_input:
        continue

    # --- ---
    if user_input.startswith("/style:"):
        new_style = user_input.replace("/style:", "").strip()
        current_instruction = new_style
        chat = start_chat(current_instruction) 
        print(f"Стиль оновлено на: '{current_instruction}'. Продовжуємо.")
        continue

    # --- ---
    if user_input == "/clearlog":
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            f.write("") # Очищення файлу
        print("🗑 Логи очищено.")
        continue

    # --- ---
    try:
        response = chat.send_message(user_input)
        answer = response.text
        print(f"\nАсистент: {answer}")

        # --- Завдання 2: Логування ---
        save_to_log(user_input, answer)

    except Exception as e:
        print(f"Сталася помилка: {e}")