import random
from time import *
import threading

#Question 1
def generateBooleanTab(n):
    tab = []
    for i in range(n):
        tab.append(random.choice([True, False]))
    return tab

def generateBooleanTabs(nbTab, n):
    tab = []
    for i in range(nbTab):
        tab.append(generateBooleanTab(n))
    return tab

#Question 2
def mystere(tab, n):
    Event.wait(2)
    i = 1
    while i  <= n and tab[i] != True:
        i += 1
    
    return i

def int_input(message):
    while True:
        try:
            x = int(input(message))       
        except ValueError:
            print("Ce n'est pas un entier ! Merci de réessayer")
            continue
        else:
            return x

nbTab = int_input("Entrez le nombre de tableau souhaité : ")
n = int_input("Entrez le nombre d'élément dans le tableau : ")
boolTabs = generateBooleanTabs(nbTab, n)
mini = 180
maxi = -1
i = 0
somme = 0
event = threading.Event()
for tab in boolTabs:
    i+=1
    t0 = process_time()
    mystere(tab, n)
    t1 = process_time()
    time = t1-t0
    somme += time
    if(time < mini):
        mini = time
    if( time > maxi):
        maxi = time
moy = somme/i

print(moy, mini, maxi)
