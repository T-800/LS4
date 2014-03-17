#! /usr/bin/python3

class memoire_SMS():

    def __init__(self):
        self.liste_mess = []

    def __repr__(self):
        chaine = ""
        for elt in self.liste_mess:
            chaine += "Message reçu à {0} de {1} :\t {2}\n".format(elt[2], elt[1], elt[3])
        return chaine


    def ajouter(self,num,temps,texte):
        self.liste_mess += [(False, num, temps,texte)]

    def nombre(self):
        return len(self.liste_mess)

    def non_lu(self):
        indice = []
        for i,elt in enumerate(self.liste_mess):
            if not elt[0]:
                indice += [i]

        return indice

    def nombre_non_lu(self):
        liste = self.non_lu()
        return len(liste)

    def message(self, i):
        if len(self.liste_mess) < i-1 or i < 1:
            return None
        mess = self.liste_mess[i-1]
        return (mess[1],mess[2],mess[3])

    def efface(self,i):
        self.liste_mess[::] = self.liste_mess[:i-1] + self.liste_mess[i:]

    def effacenum(self, num):
        liste =  []
        for elt in self.liste_mess:
            if elt[1] != num:
                liste += elt
        self.liste_mess[::] = liste

    def remettreazero(self):
        self.liste_mess[::] = []

    def copier(self,mem,eff=False):
        mem.liste_mess += [self.liste_mess]
        if eff:
            self.remettreazero()

    def clone(self):
        mem = memoire_SMS()
        self.copier(mem)
        return mem







