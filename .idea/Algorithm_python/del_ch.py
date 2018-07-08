# -*- coding: utf-8 -*-

"""
delect some ch in str:
    function: delect_ch(target_str)
        If the string has bits of "b" and "ac", remove them, return new string without "b" and "ac".
        type: targer_str,  string, like "daaabccc"
        method: no using anothor space to catch matched bit.
        For example: target_str "daaabccc", return "d".
"""

def del_ch(target_str):
    if not target_str:
        return Exception("Error: invalid input")

    loc_marker = -1
    result = target_str.split()

    try:
        for i in range(len(result)):
            if result[i] == 'b':
                continue
            if result[i] == 'c':
                if result[loc_marker] == 'a':
                    loc_marker -= 1
                    continue
            loc_marker += 1
            result[loc_marker] = result[i]
    except Exceptin as e:
        print(e)

    result_s = "".join(result[:loc_marker])

    return result_s

if __name__ == "__main__":
    str = "aacbcac"
    print(del_ch(str))

