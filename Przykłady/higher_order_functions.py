#1. Przykład autorskiej funkcji wyższego rzędu, apply

def double(x):
    return x*2

def apply(func, value):
    return func(value)

result = apply(double, 5)

#2. Funkcja wyższego rzędu map i filter

def square(a):
    return a*a

def is_even(a):
    return a%2==0

t = [1,2,3,4]

result = map(square,t)
print(list(result))# -> [1,4,9,16]

result = filter(is_even,t) 
print(list(result))# -> [2,4]

#3.Funkcja wyższego rzędu reduce

from functools import reduce

t = [1,2,3,4]

def add(a,b):
    return a+b

sum = reduce(add,t) 
print(sum) # -> 10


def compare(a,b):
    if a>b:
        return a
    return b

maximum = reduce(compare,t)
print(maximum) # -> 4