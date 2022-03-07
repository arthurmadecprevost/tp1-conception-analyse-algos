import random
import time

#Question 1
def generateBooleanTab(n):
    tab = []
    for i in range(n):
        tab.append(random.choice[True, False])
    return tab

def generateBooleanTabs(nbTab, n):
    tab = []
    for i in range(nbTab):
        tab.append(generateBooleanTab(n))
    return tab

#Question 2
def mystere(tab, n):
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
loop=True

while loop:
    print("cc")
