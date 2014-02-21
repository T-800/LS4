#! /usr/bin/env python3
#TP3
#1.3 Tables d’associations
# Q1
def freq(chaine):
    return {e:chaine.count(e) / len(chaine)\
                         for e in chaine}

print(freq("caracteres"))
print(freq("Une chaine"))
