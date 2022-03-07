import random

#Question 1
def generateBooleanTab(n):
    tab = []
    for i in range(n):
        tab.append(random.choice[True, False])
    return tab

#Question 2
def mystere(tab, n):
    i = 1
    while i  <= n and tab[i] != True:
        i += 1
    
    return i


