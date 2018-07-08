# -*- coding: utf-8 -*-
import base64

def safe_base64_decode(s):
    len_mode_4 = len(s)%4
    if len_mode_4 ==0:
        return base64.b64decode(s)
    else:
        return base64.b64decode(s+b'='*(4-len_mode_4))


# test:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='),safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'),safe_base64_decode('YWJjZA')
print('Pass')