d = {
"Коши": [1,2,3],
"Лебег": [3,4,5]
}


def peresech(first_key, second_key):
	print(list(set(d[first_key]) & set(d[second_key])))


def obied(first_key, second_key):
	print(set(d[first_key]) | set(d[second_key]))


def otric(key):
	ten = {1,2,3,4,5,6,7,8,9,10}
	print(ten - set(d[key]))

otric("Коши")

obied("Коши", "Лебег")

peresech("Лебег", "Коши")
