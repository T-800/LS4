
#!/opt/local/bin/python3.3
def importer(fichier):
    #Convertissons les poids en tableau
    return [int(i) for i in open(fichier,"r").readlines()]

def creer(fichier,arbre):
    f = open(fichier,"w")
    f.write(arbre)

def indiceMini(list):
    print('IndiceMin ->')
    i = 0
    min = list[0]
    for j,k in enumerate(list):
        if k < min:
            print('Compare:'+str(k)+" < "+str(min))
            print('NewMin avant:' + str(min))
            #min = k
            print('NewMin apres:'+str(min))
            i = j
    return i

def indiceMini2(list):
    print('IndiceMin2 ->')
    i = 0
    min = list[0]
    for j,k in enumerate(list):
        if k < min:
            print('Compare:'+str(k)+" < "+str(min))
            print('NewMin avant:' + str(min))
            min = k
            print('NewMin apres:'+str(min))
            i = j
    return i




def indiceMax(list):
    i = 0
    max = list[0]
    for j,k in enumerate(list):
        if k > max:
            i = j
    return i

def insertTri(list,somme):
    i=0
    for j,k in enumerate(list):
        if k < somme:
            i = j
        else:
            break
    list.insert(i+1,somme)
    return list

def getIndice(list,somme):
    for j,k in enumerate(list):
        if k == somme:
           return j

def algoMin(list):
    print('-> Algomin')
    if len(list) != 2:
        listDiff = [list[i+1] - list[i] for i in range(0,len(list)-1)]
        print("liste" + str(list))
        print("listeD"+str(listDiff))
        i = indiceMini(listDiff)
        print('indiceMin:'+str(i))
        somme = list[i] + list[i+1]
        newList = [k for j,k in enumerate(list) if j != i and j-1 != i]
        newList = insertTri(newList,somme)
        arbre = algoMin(newList)
        print(arbre)
        arbre = arbre.replace(str(somme),str([list[i],list[i+1]]),1)
        print('Algomin ->')
        return arbre
    else :
        print('Algomin ->')
        return str(list)


def algoMin2(list):
    print('-> Algomin2')
    if len(list) != 2:
        listDiff = [list[i + 1] - list[i] for i in range(0, len(list) - 1)]
        print("liste" + str(list))
        print("listeD" + str(listDiff))
        i = indiceMini2(listDiff)
        print('indiceMin2:' + str(i))
        somme = list[i] + list[i + 1]
        newList = [k for j, k in enumerate(list) if j != i and j - 1 != i]
        newList = insertTri(newList, somme)
        arbre = algoMin2(newList)
        print(arbre)
        arbre = arbre.replace(str(somme), str([list[i], list[i + 1]]), 1)
        print('Algomin2 ->')
        return arbre
    else:
        print('Algomin2 ->')
        return str(list)


def algoMax_old(list):
    if len(list) != 2:
        somme = list[len(list)-1] + list[0]
        newList = list[1:-2]
        newList = insertTri(newList,somme)
        arbre = algoMax(newList)

        arbre = arbre.replace(str(somme),str([list[0],list[len(list)-1]]),1)
        return arbre
    else:
        return str(list)


def algoMax(list):
    if len(list) > 2:
        somme = list[len(list) - 1] + list[0]
        newList = list[1:-1]
        newList.append(somme)
        arbre = algoMax(newList)
        print(arbre)
        arbre = arbre.replace(str(somme), str([list[0], list[len(list) - 1]]), 1)
        return arbre
    elif len(list) == 2:
        return str(list)
    else:
        return str(list[0])


def algoMax2(list):
    if len(list) > 2:
        somme = list[len(list) - 1] + list[0]
        newList = list[1:-2]
        print('a'+str(newList))
        newList = insertTri(newList, somme)
        print('b' + str(newList))
        arbre = algoMax2(newList)
        arbre = arbre.replace(str(somme), str([list[0], list[len(list) - 1]]), 1)
        #print(arbre)
        return arbre
    elif len(list) == 2:
        #print(str(list))
        return str(list)
    else:
        return str(list[0])


def run(fichier):
    list = importer(fichier)
    list.sort()
    print(list)
    arbre = algoMin(list)
    print('final'+str(arbre))
    print("\n\n\n\n")
    print(list)
    arbre2 = algoMin2(list)
    print('final2' + str(arbre2))
    #creer(fichier+"test.txt",arbre)



run("fic2")



