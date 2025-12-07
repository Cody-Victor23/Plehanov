import random
from datetime import datetime
import os
import threading
import sys 
import json

# >basis setings assistent<#

NAME = "У-Сянь"
DEFAULT_PERSONALITY = "Лайтовий вчитель, покер фейс"


# >I don't know, what is it?<#

def load_persona(filename="persona.txt"):
    if os.path.exists(filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                text = f.read().strip()
                if text:
                    return text
        except Exception:
            pass
    return DEFAULT_PERSONALITY


PERSONALITY = load_persona()

mood = random.choice(["(дружній)", "(жартівливий)", "(підтримуючий)"])

#>@<#

def load_user():
    if os.path.exists("user.json"):
        try: 
            with open("user.json", "r") as f:
                text = f.read().strip() 
                if not text:
                    return None
                data = json.loads(text)
                return data.get("name")
        except Exception:
            return None
    return None 


def get_user():
    user = load_user()   
    if user:
        return user
    
    print(f"{NAME}: Скинь свій паспорт, ну так, щоб я знав хто ти?")
    while True:
        ask_user = input("you: ").strip()
        if not ask_user:
            print(f"{NAME}: Огизок, по новому!")
        else:
            with open("user.json", "w") as f:   
                json.dump({"name":ask_user}, f)
            return ask_user
         
    
def add_note():
    print(f"{NAME}: пиши мені, паспортні данні.")  
    text = input("Ти: ")
    with open("notes.txt"< "a") as f:
        f.write(text)
    return "Усьо, Very-good"

def read_note():
    pass
   
    
    
    

# >СПИСОК СЛІВ<#

motivates = ["не сумуй", "поплач", "все сможеш"]
empty = ["чо молчишь? полбу дали?",
         "Ой, здається, ви пропустили введення. Чим я можу допомогти?",
         "Ввід порожній. Спробуйте ще раз!"]
fallbacks = ["леша, все поновой, херня",
             "Цікаве запитання, але я ще не навчений відповідати на нього.",
             "Я можу допомогти з іншими темами. Що ви мали на увазі?"]
personal = ["Cody", "У-Сянь", "Джон Увик", "Уэейн", "Тайлер-Дердан"]
greatings = ["Ку", "Що потрібо?", "Хєй", "Ку>, чим допомгти?", "Be<"]
jokes = ["колобок повесился", "куплю гараж", "смішно, аж плакати хочеться"]
farewells = ["Давай, буду плакать... Be (3", "Оффлайн. Не скучай.", "Связь разорвана.", "Ну и иди... работать. ББ."]

# >random helpers<#

def random_fallbaks():
    return random.choice(fallbacks)
def random_empety():
    return random.choice(empty)
def random_motivation():
    return random.choice(motivates)
def random_personal():
    return random.choice(personal)
def random_gretings():
    return random.choice(greatings)
def random_jokes():
    return random.choice(jokes)

#><#

def stop_bot():
    phrase = random.choice(farewells)
    print(f"\n{NAME}: {phrase}")
    print(">>> SYSTEM SHUTDOWN <<<")
    sys.exit()  # Останавливает скрипт

# >Р.Т.З.Т.С.Г.Н.З.К.Г.<#

def input_with_timeout(prompt, timeout=60):
    def on_timeout():
        print(f"\n{NAME}: Алло? Прием? Я сейчас уйду в спящий режим...")
        print(prompt, end="", flush=True)

    t = threading.Timer(timeout, on_timeout)
    t.start()
    try:
        answer = input(prompt).strip()
        return answer
    finally:
        t.cancel()

# >analyze_text<#

def analyze_text(text):
    if not text:
        return "empty"
    elif "жарт" in text or "сміши" in text:
        return "joke"
    elif "мотив" in text or "порада" in text:
        return "motivate"
    elif "хто ти" in text or "що ти" in text:
        return "personal"
    elif "привіт" in text or "вітаю" in text or "хай" in text:
        return "greating"
    elif "час" in text:
        return "time"
    elif "збережи" in text or "read" in text:
        return "add note"
    elif  "" in text or "" in text:
        return "read note"
    elif "бувай" in text or "П.О.С." in text:
        return "exit"
    return "unknown"


def get_response(text):
    t = text.lower()
    tag = analyze_text(t)

#>Be!<# 
   
    if tag == "exit":
        return "EXIT_NOW"
    if "add note" in tag:
        return add_note()
    if "read note" in tag:
        return read_note()
    if "personal_switch" in tag:
        return f"{NAME}: {random_fallbaks()}"
    if "personal_name" in tag:
        return f"{NAME}: {random_personal()}"
    if "empty" in tag:
        return f"{NAME}: {random_empety()}"
    if "motivate" in tag:
        return f"{NAME}: {random_motivation()}"
    if "joke" in tag:
        return f"{NAME}: {random_jokes()}"
    if "time" in tag:
        return f"{NAME}: Зараз {datetime.now().strftime('%H:%M')}"

    return f"{NAME}: Не розумем? - '{text}'"


# >MAIN<#
def main():
    print(PERSONALITY)
    name = get_user()
    print(f"{NAME}: {name}, {random_gretings()}. Сьогодні я {mood}")
    while True:
        user = input_with_timeout("Omega: ", timeout=35)
        response = get_response(user)
        if response == "EXIT_NOW":
            stop_bot()  
            break
        print(response)


if __name__ == "__main__":

    main()
