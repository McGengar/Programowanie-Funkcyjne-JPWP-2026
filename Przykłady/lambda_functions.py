#1. Przykład funkcji anonimowej

x = lambda a,b:a+b
print(x(4,5))

# składnia 
# -->   lambda argumenty : wyrażenie
# przykłady
# lambda x : x*x
# lambda x : 1 if x>0 else 0

#2. Zastosowanie lambdy w funkcjach wyższego rzędu

from functools import reduce
t = [1,2,3,4]

sum = reduce(lambda a,b:a+b,t) 
print(sum) # -> 10

maximum = reduce(lambda a,b: a if a>b else b ,t)
print(maximum) # -> 4

#3. Zastosowanie lambdy w funkcji sorted

data = [('a', 3), ('c', 1), ('b', 2)]

sorted_by_letter = sorted(data, key=lambda x: x[0])
sorted_by_number = sorted(data, key=lambda x: x[1])
print(sorted_by_letter) # -> [('a', 3), ('b', 2), ('c', 1)]
print(sorted_by_number) # -> [('c', 1), ('b', 2), ('a', 3)]