#! /usr/bin/env python3
#TP3
#1.3 Tables d’associations
# Q2


def mots_pairs(chaine):
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
    chaine = chaine.replace('  ', ' ')
    ch = chaine.strip().lower().split(' ')
    return [e for e in ch if len(e) % 2 == 0]


print(mots_pairs(" Voici une phrase. "))
print(mots_pairs("un-mOt"))
print(mots_pairs("Oh, le petit chat est mort."))
