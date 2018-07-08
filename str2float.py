# -*- coding:utf-8 -*-
from functools import reduce
def char2num(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
def str2float(s):
    def fn_int(x,y):
        return x * 10 + y
    def fn_dec(x,y):
        return x*0.1+y
    L = s.split('.',1)
    return reduce(fn_int,map(char2num,L[0]))+ reduce(fn_dec,map(char2num,L[1][::-1]))/10

print('str2float(\'123.456\')=',str2float('123.456'))