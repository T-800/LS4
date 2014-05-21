#! /usr/bin/python3


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

tmpCom = 0
T = [2, 4, 1, 9, 8, 3, 7, 12, 4, 0, 3, 56, 1 , 34, 2, 7, 3, 1, 3, 5, 8, 10, 2, 6, 7, 12, 67, 23, 55, 12, 4, 0, 2, 13, 54, 3, 9, 11, 2, 4, 1, 9, 8, 3, 7, 12, 4, 0, 3, 56, 1 , 34, 2, 7, 3, 1, 3, 5, 8, 10, 2, 6, 7, 12, 67, 23, 55, 12, 4, 0, 2, 13, 54, 3, 9, 11, 2, 4, 1, 9, 8, 3, 7, 12, 4, 0, 3, 56, 1 , 34, 2, 7, 3, 1, 3, 5, 8, 10, 2, 6, 7, 12, 67, 23, 55, 12, 4, 0, 2, 13, 54, 3, 9, 11, 2, 4, 1, 9, 8, 3, 7, 12, 4, 0, 3, 56, 1 , 34, 2, 7, 3, 1, 3, 5, 8, 10, 2, 6, 7, 12, 67, 23, 55, 12, 4, 0, 2, 13, 54, 3, 9, 11]
T = TriSelection(T)

print(T)
print(tmpCom)
#print(IndiceMin(T, 4))  # 5
#print(IndiceMin(T, 12)) # -1
