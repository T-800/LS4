#! /usr/bin/env python3
#TP3
#1.3 Tables d’associations
# Q1
def occ(chaine):
    return {e:chaine.count(e) for e in chaine}

print(occ("caracteres"))
print(occ("Une chaine, une cannette"))
print(occ(""))
