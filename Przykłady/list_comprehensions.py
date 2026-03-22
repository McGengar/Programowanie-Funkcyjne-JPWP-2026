#Składnia list comprehensions
# [wyrażenie for element in kolekcja]
# [wyrażenie for element in kolekcja if warunek]
# [wyrażenie if warunek else wyrażenie for element in kolekcja]

#Porównanie kompozycji funkcji wyższego rzędu z list comprehensions
#Obie funkcje liczą kwadraty parzystych elementów zbioru
t = [1,2,3,4]

result = map(lambda x: x*x, filter(lambda x: x % 2 == 0, t))
print(list(result))

result = [x*x for x in t if x % 2 == 0]
print(result)