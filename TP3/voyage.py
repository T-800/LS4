#! /usr/bin/env python3
#TP3
#1.3 Tables d’associations
# Q2


train = {"Paris": ["Lyon", "Marseille", "Bordeaux", "Nantes",
                   "Toulouse", "Lille", "Nancy"],
                   "Lyon": ["Marseille", "Nancy", "Paris"],
                   "Marseille": ["Toulouse", "Lyon", "Paris"],
                   "Bordeaux": ["Nantes", "Toulouse"],
                   "Nantes": ["Paris"],
                   "Toulouse": ["Marseille", "Bordeaux"],
                   "Lille": ["Paris", "Nancy"],
                   "Nancy": ["Lille", "Lyon"]}


def voyage(a, b):
    ens = [[a, x, b] for x in train[a] if b in train[x]]
    if b in train[a]:
        ens.append([a, b])
    return ens

print(voyage("Paris", "Toulouse"))
print(voyage("Toulouse", "Paris"))
print(voyage("Nantes", "Toulouse"))
print(voyage("Lille", "Lyon"))
