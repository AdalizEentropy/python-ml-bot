import logging

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score, f1_score

import formatter

vectorizer = CountVectorizer()
model = RandomForestClassifier()
x = []
y = []
vec_x = None


def prepare_context(intents):
    global x
    for intent in intents:
        examples = intents[intent]["examples"]
        responses = intents[intent]["responses"]
        prepare_x_data(examples, intent)
        prepare_x_data(responses, intent)
    vectorizing()


def prepare_x_data(x_data, intent):
    global x
    for data in x_data:
        data = formatter.format_text(data)
        if len(data) < 3:
            continue
        x.append(data)
        y.append(intent)


# Обучаем векторайзер и все тексты преобразуем в вектора
def vectorizing():
    global vec_x
    vectorizer.fit(x)
    vec_x = vectorizer.transform(x)


# Проверка точности модели
def check_model():
    y_predicted = model.predict(vec_x)
    logging.debug("Accuracy_score: %s, f1_score: %s", accuracy_score(y, y_predicted),
                  f1_score(y, y_predicted, average="macro"))


# Обучение модели
def modeling(intents):
    prepare_context(intents)
    model.fit(vec_x, y)
    check_model()
    logging.debug("Model is ready for working")


def get_intent(user_text):
    formatted_text = formatter.format_text(user_text)
    vec_text = vectorizer.transform([formatted_text])
    intent = model.predict(vec_text)[0]

    proba = model.predict_proba(vectorizer.transform([formatted_text]))
    # Вывести на экран список вероятных интентов
    print(pd.DataFrame(columns=model.classes_, data=[proba[0]]).T.sort_values(by=0, ascending=False))
    return intent
