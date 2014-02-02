#! /usr/bin/env python3
"""LS4 TP1"""
#1.1 Variables et affections
# Question 1
ai = 1
i = 1
ai = 3
i = 3
ai = 6
#res
print("i = "+str(i))
print("ai = "+str(ai))
#res
a, b = 2, 4
c = a
b = a
c = b - 1
c = b - a
#res
print("a = "+str(a))
print("b = "+str(b))
print("c = "+str(c))
#res
#Question 2
x = 5
x = 5
y = 9
#methode 1
tmp = x
x = y
y = tmp
#methode 2
x, y = y, x
#1.2 Int et Float
# Question 1
print("type de 3/4 = "+str(type(3/4)))
print("type de 4/2 = "+str(type(4/2)))
print("type de 3//4 = "+str(type(3//4)))
print("type de 4//2 = "+str(type(4//2)))
print("type de 3.14 = "+str(type(3.14)))
print("type de 10. = "+str(type(10.)))
print("type de 1e10 = "+str(type(1e10)))
print("type de 3**2 = "+str(type(3** 2)))
print("type de 3**(1/2) = "+str(type(3** (1/2))))
#res
r = 19875+77569 % 7
#res
print("r = "+str(r))
#res
import math
print("i = "+str((math.sqrt(3)+56/9.0*math.fabs(-1/4))))
#Question 4
print(".1 +.1+ .1 == .3 = "+str(.1 +.1+ .1 == .3))
print("0.10000000000000001 == 0.1 = "+str(0.10000000000000001 == 0.1))
print("round(.1, 1)+round(.1, 1)+round(.1, 1) == round(.3, 1) = "+str(round(.1, 1)+round(.1, 1)+round(.1, 1) == round(.3, 1)))
print("round(.1+.1+.1, 1) == round(.3, 1) = "+str(round(.1+.1+.1, 1) == round(.3, 1)))
#1.3 Fonctions
#Question 2
def f(d):
    """f"""
    z = 0
    while d != 0:
        z = z + 3
        d = d -1
    return z
#res
print("f(0) = "+str(f(0)))
print("f(3) = "+str(f(3)))
print("f(5) = "+str(f(5)))
print("f(8) = "+str(f(8)))
#res
# Question 3
def f1(e):
    """f1"""
    g = 2*e
    e = e+3
    e = g - e
    return (e, g)
#res
print("f1(5) = "+str(f1(5)))
#res
def f2(h):
    """f2"""
    j = 2 * h
    h = j - h
    h = h + 3
    return (h, j)
#res
print("f2(5) = "+str(f2(5)))
#res

def f3(k):
    """f3"""
    k = k + 3
    l = 2 * k
    k = l - k
    return (k, l)
#res
print("f3(5) = "+str(f3(5)))
#res
# Question 4
Flag = True
def ff(m, n):
    """ff"""
    global Flag
    m = m-2
    Flag = (m > n)
    return (m, n, Flag)

#res
(a, b, c) = ff(7, 2)
print("a = "+str(a)+" b = "+str(b)+" c = "+str(c))
(r, s, t) = ff(2, 2)
print("r = "+str(r)+" s = "+str(s)+" t = "+str(t))
#res

Flag2 = True
def fff(o, p):
    """fff"""
    o = o - 2
    Flag2 = (o > p)
    return (o, p, Flag)

(a, b, c) = fff(7, 2)
(r, s, t) = fff(2, 2)
print("Flag = "+str(Flag))
print("a = "+str(a)+" b = "+str(b)+" c = "+str(c))
print("r = "+str(r)+" s = "+str(s)+" t = "+str(t))

def ffff(q, u):
    """fff"""
    q = q - 2
    Flag2 = (q > u)
    return (q, u, Flag)

(a, b, c) = ffff(7, 2)
(r, s, t) = ffff(2, 2)

print("Flag = "+str(Flag))
print("a = "+str(a)+" b = "+str(b)+" c = "+str(c))
print("r = "+str(r)+" s = "+str(s)+" t = "+str(t))

x = 5
def f(y):
    global x
    x = 2 * y
    y = x - 1
    return (x, y)

(a, b) = f(7)
(r, s) = f(0)
print("x = "+str(x))
print("a = "+str(a)+" b = "+str(b))
print("x = "+str(x))
print("r = "+str(r)+" s = "+str(s))

x = 5
def f(y):
    x = 2 * y
    y = x - 1
    return (x, y)
(a, b) = f(7)
(r, s) = f(0)

print("x = "+str(x))
print("a = "+str(a)+" b = "+str(b))
print("r = "+str(r)+" s = "+str(s))

def f(x):
    x = 2 * x
    y = x - 1
    return (x, y)
(a, b) = f(7)
(r, s) = f(0)
print("x = "+str(x))
print("a = "+str(a)+" b = "+str(b))
print("r = "+str(r)+" s = "+str(s))

def f(x):
    if x% 2 == 0:
        a = 0
    elif x % 4 == 0:
        a = 1
    else :
        a = 3
    return a

print("f(4) = "+str(f(4)))

def f(x):
    if x% 2 == 0:
        a = 0
    else :
        a = 1
    return a

print("f(4) = "+str(f(4)))

def f(x):
    if x% 2 == 0:
        a = 0
    if x % 4 == 0:
        a = 1
    return a

print("f(4) = "+str(f(4)))

def ordre(x,y,z):
    return (x<y and y<z)

print("ordre(2,4,6) = "+str(ordre(2,4,6)))
print("ordre(2,4,3) = "+str(ordre(2,4,3)))
print("ordre(8,4,6) = "+str(ordre(8,4,6)))

def max(x,y):
    if x > y:
        return x
    else :
        return y

print("max(2,4) = "+str(max(2,4)))
print("max(5,5) = "+str(max(5,5)))
print("max(8,2) = "+str(max(8,2)))

def sec_to_hms(x):
    return x//3600, (x%3600)//60, (x%3600)%60

print("sec_to_hms(3601) = "+str(sec_to_hms(3601)))
print("sec_to_hms(65) = "+str(sec_to_hms(65)))


def hms_to_sec(h,m,s):
    return (h*3600)+(m*60)+s

print("hms_to_sec(1,0,5) = "+str(hms_to_sec(1,0,5)))
print("hms_to_sec(1,0,5) = "+str(hms_to_sec(1,0,5)))

import time
def now():
    return time.strftime("%Y-%m-%d %H:%M:%S.", time.localtime())

print("now = "+now())


