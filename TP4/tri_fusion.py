#! /usr/bin/python3


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


TmpComp = 0
Ta = [2, 4, 1, 9, 8, 3, 7, 12, 4, 0, 3, 56, 1, 34, 2, 7, 3, 1, 3, 5, 8, 10,
      2, 6, 7, 12, 67, 23, 55, 12, 4, 0, 2, 13, 54, 3, 9, 11, 2, 4, 1, 9, 8, 3,
      7, 12, 4, 0, 3, 56, 1, 34, 2, 7, 3, 1, 3, 5, 8, 10, 2, 6, 7, 12, 67, 23,
      55, 12, 4, 0, 2, 13, 54, 3, 9, 11, 2, 4, 1, 9, 8, 3, 7, 12, 4, 0, 3, 56,
      1, 34, 2, 7, 3, 1, 3, 5, 8, 10, 2, 6, 7, 12, 67, 23, 55, 12, 4, 0, 2, 13,
      54, 3, 9, 11, 2, 4, 1, 9, 8, 3, 7, 12, 4, 0, 3, 56, 1, 34, 2, 7, 3, 1, 3,
      5, 8, 10, 2, 6, 7, 12, 67, 23, 55, 12, 4, 0, 2, 13, 54, 3, 9, 11]
tri_fusion(Ta)
print(Ta)

print(TmpComp)
