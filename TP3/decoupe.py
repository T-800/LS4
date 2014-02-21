#! /usr/bin/env python3
#TP3
#1.3 Tables d’associations
# Q2
from grandes_lettres import grandes_lettres

def decoupe(chaine):
    return chaine.strip().split(' ')



print(decoupe(" Voici une phrase. "))
print(decoupe("un-mot"))
print(decoupe(""))
