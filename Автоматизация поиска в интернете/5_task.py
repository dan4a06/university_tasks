import math
import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Окончания, которые отрезаем (самые длинные проверяются первыми)
ENDINGS = sorted([
    'ами', 'ями', 'ого', 'его', 'ому', 'ему', 'ыми', 'ими',
    'ать', 'ять', 'ить', 'еть', 'ешь', 'ишь',
    'ой', 'ей', 'ом', 'ем', 'ам', 'ям', 'ах', 'ях', 'ов', 'ев',
    'ий', 'ый', 'ая', 'яя', 'ое', 'ее', 'ые', 'ие', 'ую', 'юю', 'ых', 'их',
    'ть',
    'а', 'я', 'о', 'е', 'ы', 'и', 'у', 'ю', 'ь', 'й',
], key=len, reverse=True)


def stem(word):
    """Отрезает окончание, оставляя корень (минимум 2 буквы)."""
    for ending in ENDINGS:
        if word.endswith(ending) and len(word) - len(ending) >= 2:
            return word[:-len(ending)]
    return word


def get_stems(text):
    """Разбивает текст на слова (без знаков препинания) и берёт корни."""
    words = re.findall(r'[а-яё]+', text.lower())
    return [stem(w) for w in words]


# Координатный индекс: {корень: {файл: [позиции]}}, позиции с 1
index = {}
lengths = {}  # сколько слов в каждом файле
for i in range(1, 11):
    name = f'file{i}.txt'
    with open(os.path.join(BASE_DIR, name), 'r', encoding='utf-8') as f:
        text = f.read()
    print(f'{name}: {text.strip()}')
    stems = get_stems(text)
    lengths[name] = len(stems)
    for pos, s in enumerate(stems, start=1):
        index.setdefault(s, {}).setdefault(name, []).append(pos)
print()

N = len(lengths)  # всего файлов в коллекции


def tf(word, name):
    """TF = сколько раз слово встретилось в файле / сколько всего слов в файле."""
    count = len(index.get(word, {}).get(name, []))
    return count / lengths[name]


def idf(word):
    """IDF = log(всего файлов / в скольких файлах есть слово)."""
    df = len(index.get(word, {}))
    if df == 0:
        return 0
    return math.log(N / df)


query = [stem(w) for w in re.findall(r'[а-яё]+', input("Введите запрос: ").lower())]

scores = {}
for name in lengths:
    # итоговая оценка файла: сумма TF-IDF по всем словам запроса
    scores[name] = sum(tf(w, name) * idf(w) for w in query)

print()
for name, score in sorted(scores.items(), key=lambda x: x[1], reverse=True):
    if score > 0:
        print(f'{name}: {score:.4f}')