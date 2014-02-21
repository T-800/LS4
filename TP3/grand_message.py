#! /usr/bin/env python3
#TP3
#1.3 Tables d’associations
# Q2
from grandes_lettres import grandes_lettres


def grand_message(chaine):
    s = ""
    for i in range(5):
        for l in chaine:
            s += grandes_lettres[l][i] + "  "
        s += '\n'
    print(s)

grand_message('renaud ')
