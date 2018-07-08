def person(name,age,**kw):
    if'city'in kw:
        #有city参数
        pass
    if'job'in kw:
        #有job参数
        pass
    print('name:',name,'age:',age,'other:',kw)
extra={'city':'Beijing','job':'Engineer'}
person('Micheal',30,**extra)