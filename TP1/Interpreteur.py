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
type(3/4)
type(4/2)
type(3//4)
type(4//2)
type(3.14)
type(10.)
type(1e10)
type(3** 2)
type(3** (1/2))
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
def f(y):
    """a"""
    z = 0
    while y != 0:
        z = z + 3
        y = y -1
    return z
#res
f(0)
f(3)
f(5)
f(8)
#res
# Question 3
def f1(x) :
    y = 2*x
    x= x+3
    x = y - x
    return (x,y)
print(f1(5))
def f2(x) :
    y = 2 * x
    x = y - x
    x = x + 3
    return (x,y)
print(f2(5))
def f3(x) :
    x = x + 3
    y = 2 * x
    x = y - x
    return (x,y)
f3(5)
Flag = True
def ff(x, y) :
    global Flag
    x = x-2
    Flag = (x>y)
    return (x,y,Flag)
(a,b,c) = ff(7,2)
print(a,b,c)
(r,s,t) = ff(2,2)
print(r,s,t)
