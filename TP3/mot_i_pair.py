#! /usr/bin/env python3
#TP3
#1.3 Tables d’associations
# Q2


def mot_i_pair(chaine):
    for p in '.,;:?!-()':
        chaine = chaine.replace(p, ' ')
    ch = chaine.strip().lower().split(' ')
    ch = " ".join(c for c in ch if c != '')
    ch = ch.split(' ')
    return [e for i, e in enumerate(ch) if (i + 1) % 2 == 0]


print(mot_i_pair(" Voici une phrase. "))
print(mot_i_pair("un-mOt"))
print(mot_i_pair("Oh, le petit chat est mort."))
