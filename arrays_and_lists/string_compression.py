from collections import defaultdict


def string_comprehension(string: str) -> str:
    """
    Implement a method to perform basic string compression using the counts
    of  repeated  characters.  For  example,  the  string aabcccccaaa  would become  a2blc5a3.  If the
    "compressed" string would not become smaller than the original string, your method should return
    the original string. You can assume the string has only uppercase and lowercase letters (a - z).
    """

    compressed_string_list = []
    counter = 1

    idx = 1
    while idx < len(string):
        last_char = string[idx-1]
        if string[idx] != last_char:
            compressed_string_list.append(last_char+str(counter))
            counter = 0
        counter += 1
        idx += 1

    # add last repeated character
    if counter:
        compressed_string_list.append(string[-1] + str(counter))

    return min(string, ''.join(compressed_string_list), key=len)
