import csv

echantillon1=[]
echantillon2=[]
echantillon3=[]
echantillon4=[]
echantillon5=[]
echantillon6=[]
echantillon7=[]
echantillon8=[]
echantillon9=[]
echantillon10=[]
echantillon11=[]
echantillon12=[]
list_31=[1,3,5,7,8,10,12]
echantillon=[echantillon1,echantillon2,echantillon3,echantillon4,echantillon5,echantillon6,echantillon7,echantillon8,echantillon9,echantillon10,echantillon11,echantillon12]

for a in range (12):
    if a < 10:
        b = "0"+str(a+1)
    else:
        b = str(a+1)
    if (a+1) in list_31:    #mois 31 jours
        for i in range (1,32):
            if i < 10:
                echantillon[a].append("2022-"+str(b)+"-0"+str(i))
            else:
                echantillon[a].append("2022-"+str(b)+"-"+str(i))
    elif (a+1) == 2:    #2022 n'est pas une année bisextille
        for i in range (1,29):
            if i < 10:
                echantillon[a].append("2022-"+str(b)+"-0"+str(i))
            else:
                echantillon[a].append("2022-"+str(b)+"-"+str(i))
    else :      #mois 30 jours
        for i in range (1,31):
            if i < 10:
                echantillon[a].append("2022-"+str(b)+"-0"+str(i))
            else:
                echantillon[a].append("2022-"+str(b)+"-"+str(i))


list_fossile1=[]
list_fossile2=[]
list_fossile3=[]
list_fossile4=[]
list_fossile5=[]
list_fossile6=[]
list_fossile7=[]
list_fossile8=[]
list_fossile9=[]
list_fossile10=[]
list_fossile11=[]
list_fossile12=[]
list_fossile=[list_fossile1,list_fossile2,list_fossile3,list_fossile4,list_fossile5,list_fossile6,list_fossile7,list_fossile8,list_fossile9,list_fossile10,list_fossile11,list_fossile12]


liste_verte1=[]
liste_verte2=[]
liste_verte3=[]
liste_verte4=[]
liste_verte5=[]
liste_verte6=[]
liste_verte7=[]
liste_verte8=[]
liste_verte9=[]
liste_verte10=[]
liste_verte11=[]
liste_verte12=[]
liste_verte=[liste_verte1,liste_verte2,liste_verte3,liste_verte4,liste_verte5,liste_verte6,liste_verte7,liste_verte8,liste_verte9,liste_verte10,liste_verte11,liste_verte12]


a = 0
nb = 0
with open("RTE_2022.csv", encoding="utf-8",newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=",")
    for row in reader:
        if a == 0:
            a = 1
        else :
            a = 0
            for i in echantillon:
                if row[2] in i:
                    nb = int(row[2][5]+row[2][6]) - 1 
                    list_fossile[nb].append(int(row[7])+int(row[8])+int(row[9])+int(row[10]))
                    liste_verte[nb].append(int(row[11])+int(row[12])+int(row[13]))

