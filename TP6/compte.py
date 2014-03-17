#! /usr/bin/python3

class CompteEpargneTemps():

    nombre_employes = 0
    def __init__(self, nom, solde=0):
        self.nom = nom
        self.solde = solde
        CompteEpargneTemps.nombre_employes +=1

    def __del__(self):
        print("Le Compte de {0} est supprimé".format(self.nom))
        CompteEpargneTemps.nombre_employes -=1

    def ajouter(self, add):
        self.solde += add

    def enlever(self, moins):
        self.solde -= moins

    def afficher(self):
        print("{0} vous avez fait {1} heure(s)".format(self.nom,self.solde))

    def nombre():
        print("Il y a {0} employé(s)".format(CompteEpargneTemps.nombre_employes))
