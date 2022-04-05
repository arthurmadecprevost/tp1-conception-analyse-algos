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
    i, somme, mg, md = 0
    
    if debut = fin:
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


tab = [1,2,3]
MaxSomme1(tab)