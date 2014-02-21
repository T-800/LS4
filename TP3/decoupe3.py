#! /usr/bin/env python3
#TP3
#1.3 Tables d’associations
# Q2


def decoupe(chaine):
    chaine = chaine.replace('.', ' ')
    chaine = chaine.replace(',', ' ')
    chaine = chaine.replace(';', ' ')
    chaine = chaine.replace(':', ' ')
    chaine = chaine.replace('?', ' ')
    chaine = chaine.replace('!', ' ')
    chaine = chaine.replace('-', ' ')
    chaine = chaine.replace('(', ' ')
    chaine = chaine.replace(')', ' ')
    chaine = chaine.replace('(', ' ')
    return chaine.strip().lower().split(' ')


print(decoupe(" Voici une phrase. "))
print(decoupe("un-mOt"))
print(decoupe(""))
