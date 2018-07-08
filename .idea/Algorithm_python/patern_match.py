# -*- coding: utf-8 -*-

"""
parten match:
    function: patern_match(input_patern, match_str)
        If the patern of match_str matches patern, return true,else false.
        type: input_patern,  string, like "aba"
              match_str,     string, like "dog cat dog"
        For example: input_patern "aba", match_str "dog cat dog", matched.
"""

def patern_match(input_patern, match_str):
    if not input_patern or not match_str:
        return Exception("Null error")

    str_split = match_str.split(" ")

    if len(input_patern) != len(str_split):
        return Exception("Length error")

    mapping = dict()

    try:
        for ch, word in zip(input_patern, str_split):
            if ch not in mapping:
                mapping[ch] = word
            else:
                if mapping[ch] != word:
                    return False
        return True
    except Exception as e:
        print(e)

if __name__ == "__main__":
    input_patern = "aba"
    match_str = "dog cat dog"
    print(patern_match(input_patern, match_str))