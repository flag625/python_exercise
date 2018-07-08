# -*- coding: utf-8 -*-
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -x
n1=10
n2=-20
print(my_abs(n1),my_abs(n2))