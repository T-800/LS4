#! /usr/bin/python3


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


T = [2, 4, 1, 9, 8, 3, 7]
#print(Inserer(T, 0))  # [2, 4, 1, 9, 8, 3, 7]
#print(Inserer(T, 1))  # [2, 4, 1, 9, 8, 3, 7]
#print(Inserer(T, 2))  # [1, 2, 4, 9, 8, 3, 7]
#print(Inserer(T, 3))  # [1, 2, 4, 9, 8, 3, 7]
#print(Inserer(T, 4))  # [1, 2, 4, 8, 9, 3, 7]
#print(Inserer(T, 5))  # [1, 2, 3, 4, 8, 9, 7]
tmpComp = 0
tmpEc = 0
tri_insertion(T)
print(T)
print(tmpEc)
print(tmpComp)
