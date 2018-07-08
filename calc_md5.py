# -*- coding: utf-8 -*-

import hashlib,os
from collections import defaultdict

db = defaultdict(lambda:'None')

def get_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()

def register(username,password):
    db[username] = get_md5(password+username+'the-Salt')

def login(username,password):
    if db[username]=='None':
        print('invaild user name!')
        return False
    elif get_md5(password+username+'the-Salt') == db[username]:
        print('success!')
        return True
    else:
        print('invaild password!')
        return False

if __name__=='__main__':
    print('Register:')
    print('enter your user name:')
    r_name = input()
    print('enter your password:')
    r_password = input()
    register(r_name,r_password)
    print('Log:')
    print('enter your user name:')
    l_name = input()
    print('enter your password:')
    l_password = input()
    login(l_name,l_password)

