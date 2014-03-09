#! /usr/bin/env python3


#TRIS

# Insertion
def Inserer(T, i):
    global tmpComp
    global tmpEc
    if i < 0 or i > len(T):
        return -1
    for indice in range(i, 0, -1):
        tmpComp += 1
        if T[indice-1] > T[indice]:
            T[indice-1], T[indice] = T[indice], T[indice-1]


def tri_insertion(T):
    for i in range(0, len(T)):
        Inserer(T, i)


# Selection

def IndiceMin(tab, i):
    global tmpCom
    if i < 0 or i > len(tab):
        return -1

    indice = i
    for pos in range(i, len(T)):
        tmpCom += 1
        if tab[indice] > tab[pos]:
            indice = pos
    return indice


def TriSelection(T):
    for i in range(len(T)):
        tmp = IndiceMin(T, i)
        T[i], T[tmp] = T[tmp], T[i]

    return T

# Fusion 1
def fusion(T, bg, m, bd):
    t1 = T[bg:m]
    t2 = T[m:bd+1]
    T3 = []

    while(len(t1) > 0 and len(t2) > 0):
        global TmpComp
        TmpComp += 1
        if t1[0] < t2[0]:
            T3 += [t1[0]]

            t1 = t1[1:]
        else:
            T3 += [t2[0]]
            t2 = t2[1:]

    if(len(t1) > 0):
        T3 += t1
    else:
        T3 += t2

    T[::] = T[:bg] + T3 + T[bd+1:]


def tri_fusion(T, bg=0, bd=-1):
    if bd == -1:
        bd = len(T)-1
    if bg != bd:
        milieu = (bg + bd)//2
        tri_fusion(T, bg, milieu)
        tri_fusion(T, milieu+1, bd)
        fusion(T, bg, milieu+1, bd)


# Fusion 2
def fusion(L1, L2) :
    if len(L1) == 0 :
        return L2
    elif len(L2) == 0 :
        return L1
    elif L1[0] < L2[0] :
        return [L1[0]] + fusion(L1[1:], L2)
    else :
        return [L2[0]] + fusion(L1, L2[1:])


def tri_fusion(T, debut, fin) :
    if fin - debut < 2 :
        return T[debut:fin]
    else :
        milieu = (debut + fin)//2
        gauche = tri_fusion(T, debut, milieu)
        droite = tri_fusion(T, milieu, fin)
        return fusion(gauche, droite)

## LISTES

L = []
L = [1, 2, 3, 4, 5]
L = [i * i for i in L if i % 2 == 0]  # liste des carrés des nombres pairs

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

L[2:8]          #  on  recupere    [3,4,5,6,7,8]
L[2:]           #   [3,4,5,6,7,8,9,10]
L[::]           #   [1,2,3,4,5,6,7,8,9,10]
L[::-1]         #   [10,9,8,7,6,5,4,3,2,1]
L[3]            #   4
L[8:4:-1]       #   [9,8,7,6]
L[-1]           #   10
L.extend(["toto", "titi"])       #   [1,2,3,4,5,6,7,8,9,10,"toto","titi"]
L.append(["toto", "titi"])       #   [1,2,3,4,5,6,7,8,9,10,["toto","titi"]]
L.insert(2, "pif")               #   [1,2,"pif",3,4,5,6,7,8,9,10]


# CHAINES
s = 'bonjour'
s[0] = 'B'         # ERREUR
s = 'B' + s[1:]    # OK
s = s.split(sep=None, maxsplit=-1)
s2 = "-".join(['chaine', 'de', 'charactere'])  # 'chaine-de-charactere'
s2 = s2.replace('-', ' ')                      # 'chaine de charactere'


# BOUCLE
range(deb, fin [,pas])
'''
On peur ajouter un else (optionnel) a la fin du for qui sera exécuté a la fin du "for"

for <element>   in  <sequence>  :
 instruction1
else    :
 instruction2

L'instruction "break" sort de la boucle "for" sans passer par le "else". En  revanche "continue"
passe à l'itteration suivante et execute le "else" s'il est présent
'''

L = [1, 2, 3, 4, 6, 5, 7, 8, 9]
for c in L:
    if c % 2 == 0:
        L.remove(c)         # [1,3,6,5,7,9] ERREUR

for c in L[::]:
    if c % 2 == 0:
        L.remove(c)         #[1,3,5,7,9]

[ f(e) for e in A ]

# TUPLE

u = 18, "salut", '4', ['a', 3]
u[1]          #   renvoi  "salut"

# ENSEMBLE

s = set()
s = {1, 2, 5, 3, 7}

s2 = set(['a', 4, 18, 'bonjour'])       #   {'a', 4, 18, 'bonjour'}

s3 = set([(1, 2, 3)])                   #   {(1,2,3)}

s4.add(4)
s4.remove(4)
'''
    Union           |
    Intersection    &
    Privé           -
    XOR             ^
'''

# DICTIONNAIRE

dico = {'ensemble': {'set', 'together'}, 'uplet': 'tuple'}
dico = dict(zip(['ensemble', 'uplet'], [{'set', 'together'}, 'tuple']))   # Attention à la taille des listes
dico.keys()          #   objet dict_keys('ensemble','uplet', 'lste')
dico.values()        #   objet dict_values('ens','tuple','lst')
dico.items()         #   objet dict_items(('ensemble','ens'), ('uplet', 'tuple'), (liste, 'lst'))

# Les opérateurs ensemblistes  |,&,-,^  s'applique aussi aux vues

# FICHIERS

# lecture
try:
    f = open('mon_fichier', 'r')
except IOError:
    printf("Erreur  ouverture   fichier")

# écriture
f = open('mon_fichier', 'w')


