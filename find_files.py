import os
import sys

def find_file(spath,search_name):
    for name in os.listdir(spath):
        spath_name = os.path.join(spath,name)
        if os.path.isdir(spath_name):
            print('%s has %s'%(spath_name,list(os.listdir(spath_name))))
            find_file(spath_name,search_name)
        elif os.path.isfile(spath_name) and os.path.basename(name).find(search_name)!=-1:
            print('find file: %s'%spath_name)
        else:
            print('not find!')



find_file('C:/Users/dell-pc/Desktop/a','d')
