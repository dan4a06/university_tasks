import re

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
    # re.findall(r'[а-яё]+', "Кот ел суп, а рис не трогал.".lower()) -> 
    # ['кот', 'ел', 'суп', 'а', 'рис', 'не', 'трогал']
    return [stem(w) for w in words]


index = {}
for i in range(1, 11):
    name = f'file{i}.txt'
    with open(name, 'r', encoding='utf-8') as f:
        text = f.read()
    print(f'{name}: {text.strip()}')
    for s in get_stems(text):
        files = index.setdefault(s, [])
        if name not in files:
            files.append(name)
print()

word1 = stem(input("Введите первое слово: ").strip().lower())
word2 = stem(input("Введите второе слово: ").strip().lower())
operation = input("Введите операцию or или and: ").strip().lower()

files1 = set(index.get(word1, []))
files2 = set(index.get(word2, []))

if operation == "and":
    print("Оба слова встречаются в файлах:", sorted(files1 & files2))
else:
    print("Эти слова встречаются в файлах:", sorted(files1 | files2))
    