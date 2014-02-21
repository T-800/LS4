#! /usr/bin/env python3
"""LS4 TP2"""
#1 Prendre le langage en main
#1.1 Structures de données Python
a = {}
print(type(a))

a = ()
print(type(a))

a = []
print(type(a))

a = ''
print(type(a))

a = 5, 3, 'bla', [1,2,3]
print(type(a))

a = 'bla'
print(type(a))

a = ['bla']
print(type(a))

a = {'bla'}
print(type(a))

t = [1, 3, 5, 8]
a = set(t)

t = [1, 3, 5, 8]
a = {e:i for i, e in enumerate(t)}
print(type(a))

d = {'mot':3, 'mots':4, 'maux':4}
a = {f for f in d.values()}
print(type(a))

a = [f for f in d.keys()][0]
print(type(a))

a = [(m,f) for m, f in d.items()][-1]
print(type(a))

a = 'bla', [1, 3], {'a', 'b'}
print(type(a))

t = 'bla', [1, 3], {'a', 'b'}
a, b, c = t
print(type(a))
print(type(b))
print(type(c))

t = 'bla', [1, 3], {'a', 'b'}
a = t[2]
print(type(a))
