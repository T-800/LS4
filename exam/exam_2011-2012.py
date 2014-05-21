#! /usr/bin/env python3
import re


d = {i: i*i for i in range(2, -3, -1)}
e = {}

for i in range(2, -3, -1):
    e[d[i]] = i

for i in range(-5, 5):
    if i in d:
        print(d[i])
    if i in e:
        print(e[i])


def fic_to_dico(path):
    dico = dict()
    f = open(path)
    liste = [l.strip() for l in f.readlines()]
    for ligne in liste:
        tmp = ligne.split(" ", 3)
        d = tmp[1].split("/")
        date = int(""+d[2]+d[1]+d[0])
        h = int(tmp[2][:2])
        m = int(tmp[2][3:])/100
        heure = h+m
        if tmp[0] in dico:
            dico[tmp[0]].append([date, heure, tmp[3]])
        else:
            dico[tmp[0]] = [[date, heure, tmp[3]]]
    return dico

SPAM = r".*0899[0-9]{6}.*"
MAJ = r"([A-Z])"
DOLL = r"\$"


def search(dico, mot):
    reg = r" "+str(mot)+" "
    ens = set()
    for num in dico:
        for mess in dico[num]:
            if re.search(reg, mess[2]):
                ens.add(num)
    return list(ens)


def liste_noire(dico):
    liste = []
    for num in dico:
        for mess in dico[num]:
            nombre = re.findall(MAJ, mess[2])
            nombre2 = re.search(DOLL, mess[2])
            spam = re.search(SPAM, mess[2])
            if len(nombre) > len(mess[2])//2 or nombre2 or spam:
                liste += [num]
    return liste


def dico_sans_spam(dico):
    dic = dict()
    print()
    for num in dico:
        for mess in dico[num]:
            if not re.search(SPAM, mess[2]):
                if num in dic:
                    dic[num].append([mess])
                else:
                    dic[num] = [[mess]]
    return dic


def dico_sans_pub(dico):

    dic = dict()
    print()
    for num in dico:
        for mess in dico[num]:
            nombre = re.findall(MAJ, mess[2])
            nombre2 = re.search(DOLL, mess[2])
            if len(nombre) <= len(mess[2])//2 and not nombre2:
                if num in dic:
                    dic[num].append(mess)
                else:
                    dic[num] = [mess]
    return dic

"""
MAIN
"""

fichier = "./test"
dico = fic_to_dico(fichier)

for i in dico:
    print(str(i)+" -> " + str(dico[i]))

print(search(dico, "la"))

dico = dico_sans_pub(dico)
print()
for i in dico:
    print(str(i)+" -> " + str(dico[i]))
