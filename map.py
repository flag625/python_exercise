# -*- coding: utf-8 -*-
def normalize(name):
    if not name.istitle():
        lname=name.title()
        return lname
    return name

L1=['adam','LISA','barT']
L2=list(map(normalize,L1))
print(L2)
