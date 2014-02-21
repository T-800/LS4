#! /usr/bin/env python3
#TP3
#1.3 Tables d’associations
# Q2
from grandes_lettres import grandes_lettres


def ligne(num, lettre):
    return grandes_lettres[lettre][num]


print(ligne(0, 't'))
print(ligne(1, 't'))
print(ligne(2, 't'))
print(ligne(3, 't'))
print(ligne(4, 't'))
