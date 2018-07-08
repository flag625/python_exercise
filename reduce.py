# -*- coding: utf-8 -*-
from functools import reduce
def prod(L):
    return reduce(multi,L)
def multi(x,y):
    return x*y
print('3*5*7*9=',prod([3,5,7,9]))