#! /usr/bin/python3

from compte import *


Marie = CompteEpargneTemps("Marie", 30)
Ahmed = CompteEpargneTemps("Ahmed", 24)
Ahmed.afficher()
Ahmed.ajouter(10)
Ahmed.afficher()
Ahmed.enlever(20)
Marie.afficher()
del Marie
CompteEpargneTemps.nombre()
del Ahmed

