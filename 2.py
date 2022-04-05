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

def MaxSomme2:
    i = 0



tab = [1,2,3]
MaxSomme1(tab)