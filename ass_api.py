import sounddevice as sd
import numpy as np
import speech_recognition as sr
import io
import wave
from google import genai
from google.genai import types

# --- ---
API_KEY = "AIzaSyBvgsku1Ie3LWvx7W04Vi3XiQysqf8t9Fw"
MODEL_ID = "gemini-2.0-flash"

client = genai.Client(api_key=API_KEY)
config = types.GenerateContentConfig(
    system_instruction="Ти — мудрий учитель бойових мистецтв. Відповідай коротко і повчально."
)

fs = 44100  
duration = 5 
recognizer = sr.Recognizer()

def get_audio_text():
    print(f"\n--- Запис пішов ({duration} сек)... Говоріть! ---")
    
    # Запис звуку
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    print("Запис завершено. Обробка...")

    byte_io = io.BytesIO()
    with wave.open(byte_io, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2) # 16-bit
        wf.setframerate(fs)
        wf.writeframes(recording.tobytes())
    
    byte_io.seek(0)


    with sr.AudioFile(byte_io) as source:
        audio_data = recognizer.record(source)
        try:
            # Використовуємо Google Web Speech API (безкоштовно)
            text = recognizer.recognize_google(audio_data, language="uk-UA")
            print(f"Ви сказали: {text}")
            return text
        except sr.UnknownValueError:
            print("Вибачте, я не зміг розібрати слова.")
            return None
        except sr.RequestError:
            print("Помилка сервісу розпізнавання.")
            return None

# --- ---
while True:
    input("Натисніть Enter, щоб почати запис питання (або Ctrl+C для виходу)...")
    
    user_text = get_audio_text()
    
    if user_text:
        # Відправка в Gemini
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=user_text,
            config=config,
        )
        
        print(f"\nУчитель: {response.text}")