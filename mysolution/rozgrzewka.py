from random import *

def fun(list):
    list2=[]
    list2.append(list[0])
    for i in list:
        if i != list2[-1]:
            list2.append(i)
    print list2

a = [1, 1, 2, 2, 3, 5, 8, 8,8, 9,9]
#fun(a)
wczytana = 10
i = 0
while wczytana != i:
    wczytana = input("Podaj liczbe: \n")
    i = randint(0,9)
