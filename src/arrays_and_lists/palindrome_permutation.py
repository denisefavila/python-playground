from collections import defaultdict


def check_palindrome_permutation(string: str) -> bool:
    """
    Given a string, write a function to check if it is a permutation of a palindrome.
    Reference: Cracking the Code Interview
    Linear solution O(n)
    """

    string = string.lower()

    char_counter = defaultdict(int)
    for char in string:
        count = char_counter[char]
        if count:
            char_counter[char] -= 1
        else:
            char_counter[char] += 1

    return sum(char_counter.values()) <= 1
