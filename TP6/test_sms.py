#! /usr/bin/python3

from sms import *


m = memoire_SMS()
m.ajouter(555,"10 :05","Salut")
m.ajouter(555,"10 :07","Bonjour")
m.ajouter(444,"10 :10","Hello, ça va ?")
m.ajouter(444,"10 :13","Allo")

m1 = memoire_SMS()
m.copier(m1)
print(m1.nombre())
print(m1.message(3))
m.efface(3)
m.effacenum(555)
m2 = m.clone()
print(m2)

