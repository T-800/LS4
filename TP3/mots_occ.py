#! /usr/bin/env python3
#TP3
#1.3 Tables d’associations
# Q2


def mots_occ(chaine, mot):
    for p in '.,;:?!-()\n':
        chaine = chaine.replace(p, ' ')
    ch = chaine.strip().lower().split(' ')
    ch = " ".join(c for c in ch if c != '')
    ch = ch.split(' ')
    i = 0
    for m in ch:
        if m == mot:
            i += 1
    return i



s = """Il était une fois,

Dans la ville de Foix,

Une marchande de foie,

Qui vendait du foie...

Elle se dit : Ma foi,

C'est la première fois

Et la dernière fois,

Que je vends du foie,

Dans la ville de Foix"""

print(mots_occ(s, 'foie'))
print(mots_occ(s, 'foix'))
print(mots_occ(s, 'fois'))
print(mots_occ(s, 'foi'))
