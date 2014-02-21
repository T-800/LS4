LS4 23/01/2014
Anne Micheli   anne.micheli@liafa.univ-paris-diderot.fr

### Introduction à Python
## 1) Langage de script
Définition : Un langage de script est un langage dans lequel un programme écrit n'a pas besoin d'être compilé pour être éxécuté.
Cela signifie qu'il éxéste un programme appelé interpréteur qui est capable de comprendre et d'éxécuter des programme écrit dans ce langage.

Un langage de script permet d'écrire de petit programme de façon simple et donc rappidement

Python est un langage de script avec un interpreteur interactif
Pour lancer linterpreteur :

    >>> pythonX.X             #(X.X est la version de python qu'on souhaite utiliser "dans ce cours la 3.1" )

## 2) Structure de donnés primitif
Les types primitifs de Python sont les:

* Boolean
* Entiers
* Flottans
* Complexes

### Variables :
Elles sont typées dynamiquement, lorsqu'une valeur est affecté a une variable interpréteur en deduit sont type.
La fonction :

    type(var):
donne le type de la variable var
ex :

    >>> a = 20
    >>> type(a)
       <class 'int'>
    >>> a = "chaine"
    >>> type(a)
       <class 'str'>

### Boolean :
Valeurs : `True, False`

Les tests utilises les opérateurs suivants :   `==, !=, >, >=, <, <=`

### Entiers :
Les entiers peuvent prendre des valeurs aussi grandes (petites) que l'on veut
L'affectation se fait a l'aide du symbole "=" de la droite vers la gauche
ex :

    >>> a = 3            # a est égal à 3
    >>> 3 = a            # Erreur
    >>> a, b = 3, 4    # a est égal à 3 et b est égal à 4

En python la variable a est differente de la variable A
### Flottans :
Les flottans sont codés comme en 'C' avec le Signe la Mantisse et l'Exposant.

    >>> f = (-1)^S * M * 2^(E-127)

ex:

    >>> a = 3.
    >>> b = 7e3             # b est égal à 7 * 10^3
    >>> c = 0.00004

## ATTENTION : Selon le calcul dont on obtient un flottant celui-ci peut être encodé de façon differente.
On ne peut dont pas tester l'egalité (inégalité) des flottant de façcon précise
ex :
    >>> (.1 + .1 + .1 ) == .3        #ce test dégalité revoi False

### Complexes :
    >>> a = 2+6j               # est equivalent à a = 2+6J

### Opérations :

* \+  addition
* \-  soustraction
* \*  mutiplication
* \** puissance
* /   division (renvoi un flottan)
* //  division entière (renvoi un entier)
* %   reste de la division entière

## 3)  Conditionnelles:
En python l'indentation est obligatoire elle est de 4 espaces

    IF :
       Structure :
          if (condition1) :
                Instruction1
                Instruction1
          elif (condition2) :
                Instruction3
          else :
                Instruction4
    Boucle WHILE :
       while (condition1) :
             Instruction1

## 4) Script
Soit le fichier main.py un programme python. Pour l'éxécuter :

    > pythonX.X main.py
