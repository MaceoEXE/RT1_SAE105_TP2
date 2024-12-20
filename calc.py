from file_reader import *

def CalcFossile(month):
    TotalF = 0
    if month == 0:
        for i in range(0,12):
            for j in list_fossile[i]:
                TotalF += int(j)
    else:
        for i in list_fossile[month-1]:
            TotalF += int(i)
    return TotalF
        

def CalcVerte(month):
    TotalV = 0
    if month == 0: 
        for i in range(0,12) :
         for j in liste_verte[i]:
            TotalV += int(j)
    else :
        for i in liste_verte[month-1]:
            TotalV += int(i)
    return TotalV