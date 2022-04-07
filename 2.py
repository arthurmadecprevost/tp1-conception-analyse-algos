import random
import threading
from time import *
def generateTab(n):
    tab = []
    neg = random.randint(0,n)
    pos = random.randint(0,n)
    while(pos == neg):
            pos = random.randint(0,n)
    for i in range(n):
        if i == neg:
            tab.append(random.randint(int(-(n/2)),-1))
        elif i == pos:
            tab.append(random.randint(1,int(n/2)))
        else :
            tab.append(random.choice([random.randint(int(-(n/2)),-1),random.randint(1,int(n/2))]))
    return tab

def generateTabs(n):
    tab = []
    for i in range(n):
        tab.append(generateTab(n))
    return tab
    
def MaxSomme1(tab):
    sommeMax = tab[0] - tab[1]
    sommeTemp = 0
    for i in range(len(tab)):
        sommeTemp = 0
        for j in range(len(tab)):
            sommeTemp += tab[j]
            if sommeTemp>sommeMax:
                sommeMax = sommeTemp
    return sommeMax

def MaxSomme2(tab, debut, fin):
    i = 0
    somme = 0
    mg = 0
    md = 0
    
    if debut == fin:
        return max(0, tab[fin])
    
    milieu = pei((debut+fin)/2)

    mg = 0
    somme = 0

    i = milieu

    while i >= debut:
        somme = somme + tab[i]
        mg = max(mg, somme)
        i = i - 1
    
    md = 0
    somme = 0

    i = milieu + 1

    while i <= fin:
        somme = somme + tab[i]
        md = max(md, somme)
        i = i + 1
    
    return max3(mg + md, MaxSomme2(tab, debut, milieu), MaxSomme2(tab, milieu + 1, fin))

def maxSomme3(tab, n):
    p,q,i = 0

    while i<n:
        q = max(q+tab[i],0)
        p = max(p,q)
        i+=1
    return p

def pei(n):
    return int(n)

def max3(a,b,c):
    return max(a,b,c)


n = [1000, 10000, 100000]
l = [50, 500, 5000]
demo_file = open('testSomme2.txt','w')
somme = 0 
i=0
event = threading.Event()

while i < len(n) and somme<180 :
    valN = n[i]
    incr = l[i]
    k=incr
    while k < valN and somme<180:
        tabs = generateTabs(k)
        j = 0
        while j < len(tabs) and somme<180:
            t0 = time()
            #MaxSomme1(tabs[j])
            MaxSomme2(tabs[j], 0, len(tabs[j])-1)
            #maxSomme3(tabs[j], k)
            t1 = time()
            timeT = t1-t0
            somme = somme + timeT
            string = "k = "+str(k)+ " time = "+str(timeT)+"\n"
            demo_file.write(string)
            j = j + 1
        k = k + incr
        print(k, somme)
    i = i+1
demo_file.close()