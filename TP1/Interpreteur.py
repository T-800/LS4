"""LS4 TP1"""
#1.1 Variables et affections
# Question 1
ai = 1
i = 1
ai = 3
i = 3
ai = 6
#res
print(i)
print(ai)
#res
a, b = 2, 4
c = a
b = a
c = b - 1
c = b - a
#res
print(a)
print(b)
print(c)
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
print(type(3/4))
print(type(4/2))
print(type(3//4))
print(type(4//2))
print(type(3.14))
print(type(10.))
print(type(1e10))
print(type(3** 2))
print(type(3** (1/2)))
#res
r = 19875+77569 % 7
#res
print(r)
#res
import math
print((math.sqrt(3)+56/9.0*math.fabs(-1/4)))
#Question 4
print(.1 +.1+ .1 == .3)
print(0.10000000000000001 == 0.1)
print(round(.1, 1)+round(.1, 1)+round(.1, 1) == round(.3, 1))
print(round(.1+.1+.1, 1) == round(.3, 1))
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
print(f(0))
print(f(3))
print(f(5))
print(f(8))
#res
# Question 3
def f1(e):
    """f1"""
    g = 2*e
    e = e+3
    e = g - e
    return (e, g)
#res
print(f1(5))
#res
def f2(h):
    """f2"""
    j = 2 * h
    h = j - h
    h = h + 3
    return (h, j)
#res
print(f2(5))
#res

def f3(k):
    """f3"""
    k = k + 3
    l = 2 * k
    k = l - k
    return (k, l)
#res
print(f3(5))
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
print(a, b, c)
(r, s, t) = ff(2, 2)
print(r, s, t)
#res

Flag2 = True
def fff(o, p):
    """fff"""
    o = o - 2
    Flag2 = (o > p)
    return (o, p, Flag)

(a, b, c) = fff(7, 2)
(r, s, t) = fff(2, 2)
print(Flag)
print(a, b, c)
print(r, s, t)

def ffff(q, u):
    """fff"""
    q = q - 2
    Flag2 = (q > u)
    return (q, u, Flag)

(a, b, c) = ffff(7, 2)
(r, s, t) = ffff(2, 2)

print(Flag)
print(a, b, c)
print(r, s, t)
