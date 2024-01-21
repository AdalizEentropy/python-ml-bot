import ml
import storage


def get_answer(name, user_text):
    if user_text == '/start':
        answer = "Приветствую, " + name
    else:
        intent = ml.get_intent(user_text)
        answer = storage.get_random_response(intent)
    return answer
