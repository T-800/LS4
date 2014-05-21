#! /usr/local/bin/python3.1
# -*- coding: utf-8 -*-
from fenetre import *


if __name__ == "__main__":
    root = Tk()

    interface = Interface(master=root)
    interface.master.title("Projet Python 2014")
    """interface.master.title("The Master")"""
    interface.pack(fill="both", expand=True)
    interface.mainloop()
