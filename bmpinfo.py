# -*- coding: utf-8 -*-
import struct,os

def bmpinfo(file_path):
    if os.path.isfile(file_path):
        with open(file_path,'rb') as f:
            s = f.read(30)
            if len(s)<30:
                print('Not a bmp file!')
                return
            info = struct.unpack('<ccIIIIIIHH',s)
            print(info)
            if(info[0]==b'B'and info[1]==b'M'):
                print('这是Windows位图，Size:%d*%d，Num_Color:%s',(info[6],info[7],info[9]))
            else:
                print('Not a bmp file')
                return
    else:
        print('File not exists!')

if __name__=='__main__':
    print('Please input a bmp file\'s full path:')
    p = input()
    bmpinfo(p)
