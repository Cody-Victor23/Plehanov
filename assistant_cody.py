#>import<#
import random
from datetime import datetime
import os

#>basis setings assistent<#

NAME = "У-Сянь"
DEFAULT_PERSONALITY = "Лайтовий вчитель, покер фейс"

#>I don't know, what is it?<#

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

#>СПИСОК СЛІВ<#

motivates = ["не сумуй", "поплач", "все сможеш"]
empty = ["чо молчишь? полбу дали?",
         "Ой, здається, ви пропустили введення. Чим я можу допомогти?", "Ввід порожній. Спробуйте ще раз!"]
fallbacks = ["леша, все поновой, херня",
             "Цікаве запитання, але я ще не навчений відповідати на нього.",
             "Я можу допомогти з іншими темами. Що ви мали на увазі?"]
personal = ["Cody", "У-Сянь", "Джон Увик", "Уэейн", "Тайлер-Дердан"]
greatings = ["Ку", "Що потрібо?", "Хєй", "Ку>, чим допомгти?", "Be<"]
jokes = ["колобок повесился", "joke 2", "joke 3"]

#>random<#
def random_fallbaks():
    return random.choice(fallbaks)
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

#>analyze_text<#

def analyze_text(text):
    if not text.strip():
        return "empty"
    elif "жарт" in text or "сміши" in text:
        return "joke"
    elif "мотив" in text or "порада" in text:
        return "motivate"
    elif "час" in text:
        return "time"
    elif "пустота" in text:
        return "fallback"
    elif "друга сторона" in text or "альтер е-го" in text:
        return "personal"
    elif "бувай" in text or "до зустрічі" in text:
        return "exit"
    return "unknown"


def get_response(text):
    t = text.lower()
    tag = analyze_text(t)

#>in tag:<#
    if "personal" in tag:
        return f"{NAME}: {random_fallbaks()}"
    if "personal" in tag:
        return f"{NAME}: {random_personal()}"
    if "empety" in tag:
        return f"{NAME}: {random_empety()}"
    if "motivate" in tag:
        return f"{NAME}: {random_motivation()}"
    if "empty" in tag:
        return f"{NAME}: Бездарь, по новому пиши."
    if "joke" in tag:
        return f"{NAME}: {random_jokes()}"
    if "time" in tag:
        return f"{NAME}: Зараз {datetime.now().strftime("%H:%M")}"
    return f"{NAME}: Не розумем? - '{text}'"
    if "exit" in tag:
        return "exit"
    return f"{NAME}: Все по новому, и нормально. - '{text}"

#>№2 (I don't know, what is it?)<#

def main():
    print(PERSONALITY)
    print(f"{NAME}: {random_gretings()}")
    while True:
        user = input("Omega: ").strip()
        response = get_response(user)
        if response == "exit":
            print(f"{NAME}: Давай, буду плакать...Be (3")
            break
        print(response)



if __name__ == "__main__":
    main()