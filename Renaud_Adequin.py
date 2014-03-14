#! /usr/bin/env python3


def question1g(T):
    return T[7]+T[-1]
#

def question2a(n):
    return "a"*n+"b"*n
#

def question3b(T):
    return [i for i in T if i >= 6]
#


def question4d(path):

    f = open(path)
    Liste = f.readlines()

    l = []
    for ligne in Liste:
        mots = ligne.split(" ")
        for mot in mots:
            if 'd' in mot or 'D' in mot:
                l += [mot.replace('\n', '')]
    return l
#


def question5a(dic1, dic2):
    d3 =  {dic1.items() & dic2.items()}
    tmp = dic1.items()
    for (e,i) in tmp:
        if e in d3.keys():
            d3.add(a,i)
#



def question6b(chaine):
    return [i for i,j in enumerate(chaine) if j == 'b']
#


def question7c(T):
    L = [v for v in T if T.count(v)>=5]
    for i in L[::]:
        if L.count(i)>=2:
            L.remove(i)

    i = 0
    for t in L :
        i+= t
    return i
#

def question8a(l):
    return dict(zip(['d','f','b']), [ e for e in l for i in l])
#
