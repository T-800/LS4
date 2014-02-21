#! /usr/bin/env python3
#TP3
#1.2 Ensembles
# Q2
def commun(chaine1, chaine2):
    return len({e for e in chaine1} & {e for e in chaine2})

print(commun("chaine", "caractere"))
print(commun("ah", "ah ah ah"))
