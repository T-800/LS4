#! /usr/bin/env python3


import tkinter
import time

def afficher(canvas, tab):
    for i,elt in enumerate(tab):
       canvas.create_rectangle(i*20,400 , i*20+20, 400-(10*elt+10), fill='grey',outline="black", width=2)

def Inserer(T, i,canvas):
    if i < 0 or i > len(T):
        return -1
    for indice in range(i, 0, -1):
        if T[indice-1] > T[indice]:
            T[indice-1], T[indice] = T[indice], T[indice-1]

            canvas.delete("all")
            afficher(canvas,T)
            canvas.after(250, canvas.update())


def tri_insertion(T,canvas):
    for i in range(0, len(T)):
        Inserer(T, i,canvas)





def pivote(T, bg, bd,canvas):
    '''
        Le pivot est bg
    '''
    while bg < bd:
        while bg < bd:
            if T[bg] > T[bd]:
                T[bg], T[bd] = T[bd], T[bg]
                canvas.delete("all")
                afficher(canvas,T)
                canvas.after(500, canvas.update())
                break
            bd = bd - 1
        while bg < bd:
            if T[bg] > T[bd]:
                T[bg], T[bd] = T[bd], T[bg]
                canvas.delete("all")
                afficher(canvas,T)
                canvas.after(500, canvas.update())
                break
            bg = bg + 1
    return bg


def tri_rapide(T,canvas, bg=0, bd=-1):
    '''
        tri_rapide(T): tri rapide (quicksort) de la liste T
    '''
    if bd == -1:
        bd = len(T)-1
    if bg < bd:
        i = pivote(T, bg, bd,canvas)
        tri_rapide(T,canvas, bg, i)
        tri_rapide(T,canvas, i+1, bd)


























fenetre = tkinter.Tk()
quitter = tkinter.Button(fenetre, text="Quitter", command=fenetre.destroy).pack()
canvas = tkinter.Canvas(fenetre,width=400,height=400,background="white")
canvas.pack()
T = [10,20,3,1,19,29,14,38,11,24,5,17,32,34,8,15,35,25,18,22]

for i in range(400):
    for j in range(400):
        canvas.create_rectangle(i*10, j*10, i*10+10, j*10+10)
afficher(canvas,T)
tri_insertion(T, canvas)
tkinter.mainloop()

