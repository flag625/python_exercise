# -*- coding: utf-8 -*-
def is_palindrome(n):
    rn = int(str(n)[::-1])
    if rn == n:
        return n



output = filter(is_palindrome,range(1,1000))
print(list(output))

