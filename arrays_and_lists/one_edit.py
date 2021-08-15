

def one_char_insertion(string1: str, string2: str) -> bool:
    count_insertions = 0
    idx_1 = 0
    idx_2 = 0

    while idx_1 < len(string1):
        if string2[idx_2] != string1[idx_1]:
            if count_insertions == 1:
                return False

            count_insertions += 1
            idx_2 += 1

        return True


def one_char_replacement(string1: str, string2: str) -> bool:
    count_replacements = 0
    for idx, char in enumerate(string1):
        if string2[idx] != char:
            if count_replacements == 1:
                return False

            # count replacement
            count_replacements += 1

    return True


def check_one_edit(string1: str, string2: str) -> bool:
    """
   There  are  three  types  of  edits  that  can be  performed  on  strings:
   insert  a  character, remove a character, or  replace a character.
   Given  two strings, write a  function to check if they are  one edit (or zero edits) away.
   """

    string1 = string1.lower()
    string2 = string2.lower()

    len_diff = len(string1) - len(string2)

    if abs(len_diff) > 1:
        return False

    if len_diff == 1:
        #  If diff size > 1, we need to check one-char insert.
        return one_char_insertion(string1, string2)
    elif len_diff == -1:
        #  If diff size > 1, we need to check one-char insert.
        return one_char_insertion(string2, string1)
    else:
        # If same size, we need to check one-char replacement.
        return one_char_replacement(string1, string2)
