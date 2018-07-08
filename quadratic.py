# -*- coding: utf-8 -*-
import math
def quadratic(a,b,c):
    if not isinstance(a,(int,float)):
        raise TypeError('a is bad operand type')
    if not isinstance(b,(int,float)):
        raise TypeError('b is bad operand type')
    if not isinstance(c,(int,float)):
        raise TypeError('c is bad operand type')
    derta=b*b-4*a*c
    if derta >=0:
        x1=(-b+math.sqrt(derta))/(2*a)
        x2=(-b-math.sqrt(derta))/(2*a)
        return x1,x2
    else:
        return(None)
print(quadratic(2,3,1))
print(quadratic(1,3,-4))