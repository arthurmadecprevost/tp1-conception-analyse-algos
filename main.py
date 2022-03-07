import random

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


