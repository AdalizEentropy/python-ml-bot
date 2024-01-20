import filter


X = []
y = []
INTENTS = {}

for intent in INTENTS:
    examples = INTENTS[intent]["examples"]
    for example in examples:
        example = filter.filter_text(example)
        if len(example) < 3:
            continue
        X.append(example)
        y.append(intent)