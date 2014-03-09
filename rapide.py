#! /usr/bin/env python3

import random


def pivote(T, bg, bd):
    '''
        Le pivot est bg
    '''
    global TmpComp
    while bg < bd:
        # The partition use the first element of the range as pivot
        while bg < bd:
            TmpComp += 1
            if T[bg] > T[bd]:
                T[bg], T[bd] = T[bd], T[bg]
                break
            bd = bd - 1
        # The partition use the last element of the range as pivot
        while bg < bd:
            TmpComp += 1
            if T[bg] > T[bd]:
                T[bg], T[bd] = T[bd], T[bg]
                break
            bg = bg + 1
    return bg


def trirapide(T, bg=0, bd=-1):
    '''
        trirapide(T): tri rapide (quicksort) de la liste T
    '''
    if bd == -1:
        bd = len(T)-1
    if bg < bd:
        i = pivote(T, bg, bd)
        trirapide(T, bg, i)
        trirapide(T, i+1, bd)


def melange(n):
    T = [i for i in range(n)]
    for i in range(n):
        rand = random.randint(i, n-1)
        T[i], T[rand] = T[rand], T[i]
    return T

Tab = melange(100)
TmpComp = 0
print(Tab)
trirapide(Tab)
print("\n\n\n\n")
print(Tab)


print(TmpComp)
