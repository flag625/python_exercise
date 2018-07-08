# -*- coding: utf-8 -*-

"""
delect some ch in str:
    function: delect_ch(target_str)
        If the string has bits of "b" and "ac", remove them, return new string without "b" and "ac".
        type: targer_str,  string, like "daaabccc"
        method: using stack to catch matched bit.
        For example: target_str "daaabccc", return "d".
"""

def delect_ch(target_str):
    if not target_str:
        return Exception("Error: invalid input")

    result_stack = []

    try:
        for a in target_str:
            if a == 'b':
                continue
            if a == 'c':
                if result_stack[-1] == 'a':
                    result_stack.pop(-1)
                    continue
            result_stack.append(a)
    except Exceptin as e:
        print(e)

    result = "".join(result_stack)

    return result

if __name__ == "__main__":
    str = "aaccac"
    print(delect_ch(str))

