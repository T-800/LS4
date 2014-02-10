#! /usr/bin/env python3
"""
my_name.py

Ceci est le module de {a completer par son nom}
Il affiche un avertissement
"""

auteur = "Adequin Renaud"


def copyright():
        """
        Retourne un message d'avertissement
        """
        return "Ne pas recopier"
        # Retourner la chaine de caractere 'Ne pas recopier'

# En utilisant print, Afficher sur la sortie standard l'auteur
# Afficher le message de Copyright

if __name__ == "__main__" :
      print(auteur+"\n" + copyright())
