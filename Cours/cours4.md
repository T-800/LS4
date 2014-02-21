LS4 13/02/2014
Anne Micheli   anne.micheli@liafa.univ-paris-diderot.fr

#Les Uplets (Tuple) :

Collection d'objets qui peuvent être distincts non mutable

##Déclaration :
    >>> u = 18, "salut", '4', ['a', 3]
    >>> u[1]                                           # renvoi "salut"

On peut itérer sur un uplet

    >>> type(u[3])                                     # renvoi "list"
    >>> u[3][0]                                          # renvoi 'a'

#Les ensembles (set):

Collection non ordonnée d'objet non mutable (mais on peut modifier l'ensemble) de types distincts. Tous les Objets de l'ensemble sont distincts.

##Déclaration :
    >>> s = {1, 2, 5, 3, 7}
    >>> s = set()
    >>> s                                              # renvoi set()

    >>> s2 = set(['a', 4, 18, 'bonjour'])
    >>> s2                                              # {'a', 4, 18, 'bonjour'}

    >>> s3 = set([(1, 2, 3)])
    >>> s3                                             # {(1,2,3)}

On peut modifier un ensemble :

    >>> s4.add(4)
    >>> s4.remove(4)


    >>> 2 in s4                                        # True
    >>> 'bonjour' not in s4                      # True

On peut réaliser
###l'union de deux ensemble : union, |

    >>> s = s1.union(s2)
    >>> s = s1 | s2

###l'intersection : intersection, &

    >>> s = s1.intersection(s2)

    >>> s = s1 & s2

###la diference: difference, -

    >>> s = s1.difference(s2)
    >>> s = s1 - s2


###la diference symetrique (ou éclusif): difference, -

    >>> s = s1.symmetric_difference(s2)

    >>> s = s1 ^ s2


#Les dictionnaires (dictionary) :
Un dico est un ensemble de couple clé, valeur où :
- les clés sont des types non mutable
- les valeur sont de n'importe quel type

##Déclaration:
    >>> dico = {'ensemble': {'set', 'together'}, 'uplet': 'tuple'}
    >>> dico = dict()
    >>> dico = {}

    >>> dico = dict(zip(['ensemble', 'uplet'], [{'set', 'together'},'tuple']))
    >>> dico = {c:v for (c,v) in zip(range(4), ['a','b','c','d'])}

##Acces et modification :

    >>> dico ['uplet']                             # tuple
    >>> dico ['liste'] = 'list'                    # ajout le couple liste:list
    >>> dico ['ensemble'] = 'ens'          #modifie l'entrée ensemble

##Les vues (views) :
la vue dict_keys est un objet faisant référence aux clés d'un dictionnaire

    >>> dico.keys()                  # objet dict_keys('ensemble', 'uplet','lste')

la vue dict_values est un objet faisant référence aux valeurs d'un dictionnaire

    >>> dico.values()                  # objet dict_values('ens','tuple','lst')

la vue dict_items est un objet faisant référence aux couples clés,valeurs d'un dictionnaire

    >>> dico.items()                  # objet dict_items(('ensemble','ens'),('uplet','tuple'),(liste,'lst'))


###les vues sont des objets itérables. De plus si on modifie le dictionnaire correspondant, les vues sont modifiers et inversement.

###Les opérateurs ensemblistes |,&,-,^ s'applique aux vues

