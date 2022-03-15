import random
from time import *
import threading 
from threading import Timer



#Question 1
def generateBooleanTab(n, i):
    tab = []
    for j in range(n):
        if j == i:
            tab.append(True)
        else :
            tab.append(False)
    return tab

def generateBooleanTabs(n):
    tab = []
    for i in range(n):
        tab.append(generateBooleanTab(n, i))
    tab.append(generateBooleanTab(n, -1))
    return tab

#Question 2
def mystere(tab, n):
    i = 1
    while i < n and tab[i] != True:
        sleep(1)
        i += 1
    
    return i

def int_input(message):
    while True:
        try:
            x = int(input(message))       
        except ValueError:
            print("Ce n'est pas un entier ! Merci de reessayer")
            continue
        else:
            return x


n = int_input("Entrez le nombre d'element dans le tableau : ")
# boolTabs = generateBooleanTabs(n)
#     mini = 180
#     maxi = -1
#     i = 0
#     somme = 0
#     event = threading.Event()
#     for tab in boolTabs:
#         i+=1
#         t0 = time()
#         mystere(tab, n)
#         t1 = time()
#         timeT = t1-t0
#         somme += timeT
#         if(timeT < mini):
#             mini = timeT
#         if( timeT > maxi):
#             maxi = timeT
#     moy = somme/i

#     print(moy, mini, maxi)

l=1
somme=0
while(somme<180 and l != n):
    boolTabs = generateBooleanTabs(n)
    i = 0
    event = threading.Event()
    for tab in boolTabs:
        i+=1
        t0 = time()
        mystere(tab, n)
        t1 = time()
        timeT = t1-t0
        somme += timeT
    print(somme, l)
    l=l+1

   