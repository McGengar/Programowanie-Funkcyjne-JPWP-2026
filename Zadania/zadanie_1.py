#Napraw kod aby spełniał założenia progeramowania funkcyjnego
#Końcowo program ma korzystać z funkcji do dzielenia liczb 6/3 
#i w osobnej linijce podwojenia wyniku (niekoniecznie z użyciem funkcji)

result = 0
def divide(a,b):
    global result
    if b==0: return 0
    a = a/b
    result = a

divide(6,3)
result = result*2

#Naprawiony kod zapisz poniżej