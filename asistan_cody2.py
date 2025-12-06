import random
from datetime import datetime
import os
import threading
import sys  # Нужно для остановки программы

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


# >НОВАЯ ФУНКЦИЯ ОСТАНОВКИ<#
def stop_bot():
    phrase = random.choice(farewells)
    print(f"\n{NAME}: {phrase}")
    print(">>> SYSTEM SHUTDOWN <<<")
    sys.exit()  # Останавливает скрипт


# >Функция таймера (если долго молчать)<#
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
    # Добавил больше слов для выхода
    elif "бувай" in text or "до зустрічі" in text or "стоп" in text or "выход" in text or "exit" in text:
        return "exit"
    elif "жарт" in text or "сміши" in text:
        return "joke"
    elif "мотив" in text or "порада" in text:
        return "motivate"
    elif "час" in text:
        return "time"
    elif "пустота" in text:
        return "fallback"
    elif "друга сторона" in text or "альтер е-го" in text:
        return "personal_switch"
    elif "имя" in text or "name" in text:
        return "personal_name"

    return "unknown"


def get_response(text):
    t = text.lower()
    tag = analyze_text(t)

    # Если тег exit — возвращаем кодовое слово, чтобы main() вызвал функцию остановки
    if tag == "exit":
        return "EXIT_NOW"

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
    print(f"{NAME}: {random_gretings()}")

    while True:
        # Ждет ввода 60 секунд, потом ругается
        user = input_with_timeout("Omega: ", timeout=60)

        response = get_response(user)

        # Проверяем, не пора ли закрываться
        if response == "EXIT_NOW":
            stop_bot()  # Вызываем нашу новую функцию
            break  # На всякий случай, хотя sys.exit() уже все остановит

        print(response)


if __name__ == "__main__":
    main()