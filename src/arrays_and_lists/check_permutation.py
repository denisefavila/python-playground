from collections import defaultdict


def check_permutation(str1: str, str2: str) -> bool:
    """
    Given two strings, write a method to decide if one is a permutation of the other.
    Implementing using a hashtable to count chars.
    Reference: Cracking the Code Interview
    Linear solution O(n)
    """

    str1 = str1.lower()
    str2 = str2.lower()

    if len(str1) != len(str2):
        return False

    char_counter = defaultdict(int)
    for char in str1:
        char_counter[char] += 1

    for char in str2:
        char_counter[char] -= 1

    return not any(char_counter.values())
