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
for i in range(1, 11):
    name = f'file{i}.txt'
    with open(os.path.join(BASE_DIR, name), 'r', encoding='utf-8') as f:
        text = f.read()
    print(f'{name}: {text.strip()}')
    for pos, s in enumerate(get_stems(text), start=1):
        index.setdefault(s, {}).setdefault(name, []).append(pos)
print()

word1 = stem(input("Введите первое слово: ").strip().lower())
word2 = stem(input("Введите второе слово: ").strip().lower())
distance = int(input("Введите расстояние: "))
mode = input("Расстояние - это разность позиций (1) или слов между ними (2)? ").strip()

# Если считаем слова между, то разность позиций на 1 больше
needed_diff = distance if mode == "1" else distance + 1

result = []
files1 = index.get(word1, {})
files2 = index.get(word2, {})
for name in files1:
    if name in files2:
        # есть ли пара позиций с нужной разностью
        if any(abs(p1 - p2) == needed_diff for p1 in files1[name] for p2 in files2[name]):
            result.append(name)

if result:
    print("Подходящие файлы:", sorted(result))
else:
    print("Подходящих файлов нет")