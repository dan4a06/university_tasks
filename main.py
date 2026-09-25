dict = {}
for i in range(1, 11):
	with open(f'file{i}.txt', 'r') as f:
		line = f.readline().split()
		for word in line:
			if word not in dict:
				dict[word] = [] 
				dict[word].append(f'file{i}.txt')
			else:
				dict[word].append(f'file{i}.txt')


word1 = input("введите первое слово: ")
word2 = input("введите второе слово: ")
operation = input("Введите оперцию or или and: ")

files1 = set(dict[word1])
files2 = set(dict[word2])

if operation == "and":
	print("Оба этих слова встречаются в файлах: ", files1 & files2)
else:
	print("Эти слова встречаются в файлах: ", files1 | files2)
