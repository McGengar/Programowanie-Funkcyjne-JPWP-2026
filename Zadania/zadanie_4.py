#Zadanie ma zasymulować prosty pipeline przesyłu danych
#w jakimś systemie telekomunikacyjnym

#Pipline działa w ten sposób:

#1.Sygnał nadany jest modulowany modulacją PAM, 
#u nas jest to zasymulowane zamienianiem 0 i 1 na -1 i 1

#2.Sygnał zmodulowany przechodzi przez zaszumiony kanał,
#co w zadaniu rozumienmy jako dodanie szumu "noise" do naszeo sygnału
#(warto zauważyć, że noise to też lista o długości takiej jak dane)

#3.Zaszumiony sygnał jest odbierany i poddany detekcji, naszym progiem
#detekcyjnym jest 0, co oznacza że każdy odebrany symbol większy od 0
#zostaje zinterpretowany jako 1, a poniżej 0 jako 0

#4.Porównujemy sygnał nadany i zdemodulowany i liczmy ilość błędów

#W tym zadaniu uzupełnij tylko i wyłączenie funkcje pipelinu aby ostatecznie
#uzyskać wyniki:

#[0, 0, 1, 1, 0, 1, 1, 0, 1]
#[1, 0, 1, 1, 0, 0, 0, 1, 0]
#5

#Nie edytuj danych, nie korzystaj z listcomprehensions, edytuj
#tylko ciała funkcji w miejscach ... wewnątrz funkcji wyższego rzędu.

import numpy as np
from functools import reduce
seed = 10
np.random.seed(seed)

data = [0,0,1,1,0,1,1,0,1]
noise_power = 6
noise = map(lambda a:(float(a)-0.5)*noise_power,np.random.rand(len(data)))


#Modulacja -> zamiana każdego symbolu danych z 1 na 1, 0 na -1
def modulate(x):
    return list(map(...))
#Kanał -> dodanie do każdej próbki próbkę szumu
#UWAGA - funkcja map może przyjmować więcej niż jeden zbiór,
#jeżeli funkcja wyższego rzędu ma więcej niż jeden argument
def awgn(x,n):
    return list(map(...))
#Detekcja -> Zamiana każdej wartości >0 na 1, reszta na 0
def detect(x):
    return list(map(...))

#Liczenie błędów -> policzenie ilości różnic w symbolach
#Podpowiedź - np.array(x)-np.array(y) zwraca array różnic poszczególnych elementów
#np. dla [1,1,0] i [0,1,1] zwróci [1,0,-1]. W naszym przypadku różnice dadzą nam 1 albo -1
def errno(x,y):
    return reduce(...)

recived_data = detect(awgn(modulate(data),noise))

print(data)
print(recived_data)
print(errno(data,recived_data))