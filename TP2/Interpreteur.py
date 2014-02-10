#! /usr/bin/env python3
"""LS4 TP2"""
# 1 Prendre le langage en main
#1.1 Chaînes de caractèeres
# Question 1
h = "Hello "
w = "World "
hw = h + w + "!"
l = len(h)
hhh = 3*h
lll = len(hhh)
print("hw = "+hw)
print("l = "+str(l))
print("hhh = "+hhh)
print("lll = "+str(lll))
s = "Tranches ou Slices"
t = s[1:4]
c = s[0]
u = s[0::3]
uu = s[0:3]
uuu = s[-3:0]
uuuu = s[-3:]
r = s[-1::-1]
rr = s[-1:0:-1]
rrr = s[::-1]
print("t = "+t)
print("c = "+c)
print("u = "+u)
print("uu = "+uu)
print("uuu = "+uuu)
print("uuuu = "+uuuu)
print("r = "+r)
print("rr = "+rr)
print("rrr = "+rrr)
s = 'Test'
b = 'e' in s
bb = 's' not in s
print("b = "+str(b))
print("bb = "+str(bb))

# Question 2
def prefixe(s, n):
    if len(s) < n :
        return False
    else :
        return s[:n]
print("prefix('',0) = "+prefixe('',0))
print("prefix('prefix',3) = "+str(prefixe('prefix',3)))
print("prefix('a',1) = "+str(prefixe('a',1)))
print("prefix('a',3) = "+str(prefixe('a',3)))

def suffixe(s,n):
    if len(s) < n :
        return False
    else :
        return s[n+1:]
print("suffix('',0) = "+suffixe('',0))
print("suffix('suffixe',3) = "+suffixe('suffixe',3))
print("suffix('a',0) = "+suffixe('a',0))
print("suffix('a',3) = "+str(suffixe('a',3)))
print("suffix('a',3) = "+str(suffixe('a',3)))

def miroir(s):
    return s[::-1]

print("miroir('reflet') = "+miroir('reflet'))

def palindrome(s):
    return s == s[::-1]
print("palindrome('mon nom') = "+str(palindrome('mon nom')))
print("palindrome('mon nom') = "+str(palindrome('mon nom')))
print("palindrome('my name') = "+str(palindrome('my name')))

def centre(s):
    if len(s) % 2 == 0 :
        return s[len(s)//2-1:len(s)//2+1:]
    else :
        return s[len(s)//2]

print("centre('ab') = "+str(centre('ab')))
print("centre('abc') = "+str(centre('abc')))
print("centre('centre') = "+str(centre('centre')))

def pairs(s):
    return s[::2]

print("pairs('ma chaine') = "+str(pairs('ma chaine')))
print("pairs('') = "+str(pairs('')))
print("pairs('abc') = "+str(pairs('abc')))

# Question 3
s = "on peut iterer sur les chaines"
t = ''
for c in s:
    t = t + ' ' + c

print("t = "+t)

s = "iterer sur les caracteres et les indices des chaines"
for i,c in enumerate(s):
    if c == 'e':
        j = i
k = s.index('e')

print("s[j] = "+s[j])
print("s[j+1] = "+s[j+1])
print("s[k] = "+s[k])
print("s[k+2] = "+s[k+2])
# Question 4
# 1
def sans_e(s):
    tmp = ''
    for c in s:
        if c != 'e':
            tmp = tmp + c
    return tmp
print("sans_e('Test') = "+sans_e('Test'))
print("sans_e('Bonjour') = "+sans_e('Bonjour'))
print("sans_e('eee') = "+sans_e('eee'))
print("sans_e('') = "+sans_e(''))
# 2
def compte_espace(s):
    cmt = 0
    for c in s:
        if c == ' ':
            cmt = cmt + 1
    return cmt

print("compte_espace('un espace') = "+str(compte_espace('un espace')))
print("compte_espace('pasd'esapce') = "+str(compte_espace("pasd'esapce")))
print("compte_espace(' espace au debut') = "+str(compte_espace(" espace au debut")))
print("compte_espace('espace a la fin ') = "+str(compte_espace("espace a la fin ")))
#Question 5
def palindrome_espace(s):
    tmp = ''
    tmp = s.replace(' ','')
    return tmp == tmp[::-1]
print("palindrome_espace('a man a plan a canal panama') = "+str(palindrome_espace('a man a plan a canal panama')))
print("palindrome_espace('le sel') = "+str(palindrome_espace('le sel')))
print("palindrome_espace('le poivre') = "+str(palindrome_espace('le poivre')))

# 1.2 Tableaux Mutables
#Question 1

L = [0,1,2,3,4,5]
a1 = L[0]
a2 = L[-1]
S1 = L[2:3]
S2 = L[1:]
S3 = L[-1::-1]

print("a1 = "+str(a1))
print("a2 = "+str(a2))
print("S1 = "+str(S1))
print("S2 = "+str(S2))
print("S3 = "+str(S3))

M = ['a','b','c','d']
v1 = M[3]
M.append('e')
M.extend([1,2,3])
del(M[3])
v2 = M[3]

for i,e in enumerate(M):
    v3 = i

print("M = "+str(M))
print("v1 = "+str(v1))
print("v2 = "+str(v2))
print("v3 = "+str(v3))

N = [1,2,3]
NN = ['a','b']
i = id(N)
ii = id(NN)
j = id(N+NN)
N[-1:]=NN
j1 = id(N)

for e in NN:
    N.append(e)

j2 = id(N)
N.extend(NN)
j3 = id(NN)

b1 = (i==ii)
b2 = (i==j)
b3 = (ii==j)
b4 = (i==j1)
b5 = (i==j2)
b6 = (i==j3)

print("N = "+str(N))
print("NN = "+str(NN))
print("b1 = "+str(b1))
print("b2 = "+str(b2))
print("b3 = "+str(b3))
print("b4 = "+str(b4))
print("b5 = "+str(b5))
print("b6 = "+str(b6))
# Question 2
tab = [1, 34, 5, 4, 7, 8, 93]
t1 = [2*i for i in tab]
t2 = [i for i in tab if i%2 == 0]
t3 = [2*i for i in tab if i%2 == 0]

print("t1 = "+str(t1))
print("t2 = "+str(t2))
print("t3 = "+str(t3))

tab = 'ceci est un tableau de mots'.split()
t = [u+v for u in tab for v in tab if u != v]

print("tab = "+str(tab))
print("t = "+str(t))

alphabet = 'ab'
mots_longueur_3 = [i+j+k for i in alphabet for j in alphabet for k in alphabet]

print("mots_longueur_3 = "+str(mots_longueur_3))
# Question 3
# 1
def somme(t):
    tmp = 0
    for i in t:
        tmp = tmp + i
    return tmp

print("somme([1,2,3]) = "+str(somme([1,2,3])))
print("somme([]) = "+str(somme([])))
print("somme([0,4,4,4]) = "+str(somme([0,4,4,4])))
#2
def carre(t):
    return [i*i for i in t]

print("carre([1,2,3]) = "+str(carre([1,2,3])))
print("carre([]) = "+str(carre([])))
print("carre([0,4,4,4]) = "+str(carre([0,4,4,4])))
#3
def pair(t):
    return [c for i,c in enumerate(t) if i% 2 == 0]

print("pair([1,2,3,4,5,6,7]) = "+str(pair([1,2,3,4,5,6,7])))
print("pair([]) = "+str(pair([])))
print("pair([0,1,2,3,4,4,4]) = "+str(pair([0,1,2,3,4,4,4])))

#4
def ma_map(fonc, T):
    return [fonc(c)for c in T]

print("ma_map(sans_e, ['un mot', 'un autre', 'et encore un autre'] = "+str(ma_map(sans_e, ["un mot", "un autre", "et encore un autre"])))
print("ma_map(len, [[],[1,2,3],['bla']]) = "+str(ma_map(len, [[],[1,2,3],["bla"]])))

# 5
def occ(c, chaine):
    return [i for i,a in enumerate(chaine) if a == c]
print("occ('h','ma chaine') = "+str(occ('h','ma chaine')))
print("occ('c','une phrase avec 'c'') = "+str(occ('c','une phrase avec "c"')))
print("occ('c','une phrase sans') = "+str(occ('c','une phrase sans ')))
# 1.3
# Question 1
def f(n):
    u = 1
    for x in range(n):
        u = u*(x+1)
    return u

print("f(0) = "+str(f(0)))
print("f(2) = "+str(f(2)))
print("f(3) = "+str(f(3)))
print("f(5) = "+str(f(5)))

# Question 2
T = []
n = 1
for i in range(n):
    if i != 0:
        T.append(i)

for i in range(1,13,2*n):
    for j in range(0,n):
        T.append([i,j])

for i in range(1, len(T), 5):
    for j in range(0, i, 2):
        for k in range(0, i, 2):
            if (i > j) and (j > k):
                T.append([i, j, k])

print("T = "+str(T))

# Question 3
import math
def pi_2_6a(n):
    tmp = 0
    for i in range(1,int(n)):
        tmp = tmp + 1/math.pow(i,2)
    return tmp
def pi_2_6d(n):
    tmp = 0
    for i in range(int(n),0,-1):
        tmp = tmp + 1/math.pow(i,2)
    return tmp

T = []
for i in range(1,6):
    T.append(pi_2_6a(math.pow(10,i))-pi_2_6d(math.pow(10,i)))

print(str(T))

# Question 4
c = 0
s = 0
l = [i for i in range(10)]

for k in l:
    c += 1
    s += k

m = s/c

print("c = "+str(c))
print("s = "+str(s))
print("l = "+str(l))
print("m = "+str(m))

def double(l):
    tmp = []
    for c in l:
        tmp.append(c)
    for c in l:
        tmp.append(c)
    return tmp


print("double([]) = "+str(double([])))
print("double([1,2,3]) = "+str(double([1,2,3])))
print("double([0,0]) = "+str(double([0,0])))

# 2 Programmer et Tester
# 2.1 Scripts et modules
