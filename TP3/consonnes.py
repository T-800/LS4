#! /usr/bin/env python3
#TP3
#1.2 Ensembles
# Q3


def consonnes(chaine):
    return { e for e in chaine if e not in ('a','e','i','o','u','y')}

print(consonnes("caractere"))
print(consonnes("ah"))
print(consonnes("ou"))
