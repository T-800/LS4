#! /usr/bin/env python3
#TP3
#1.2 Ensembles
# Q1
def ens(chaine):
    return {e for e in chaine}

print(ens("caracteres"))
print(ens(""))
