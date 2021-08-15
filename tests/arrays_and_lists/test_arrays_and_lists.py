
import pytest

from arrays_and_lists.check_permutation import check_permutation
from arrays_and_lists.one_edit import check_one_edit
from arrays_and_lists.palindrome_permutation import check_palindrome_permutation
from arrays_and_lists.string_compression import string_comprehension


class TestCheckPermutation:

    @pytest.mark.parametrize(
        "string1, string2",
        [['ab', 'ac'], ['aaab', 'aab']]
    )
    def test_with_false_permutation(self, string1, string2):
        result = check_permutation(string1, string2)
        assert not result

    @pytest.mark.parametrize(
        "string1, string2",
        [['ab', 'ba'], ['dog', 'god'], ['1234', '4321'], ['dog', 'dog']]
    )
    def test_with_true_permutation(self, string1, string2):
        result = check_permutation(string1, string2)
        assert result


class TestCheckPalindromePermutation:

    @pytest.mark.parametrize("input",
                             ['Tact  Coa', 'abab', 'aba', "a-bba", 'Able was I ere I saw Elba'])
    def test_true_palindrome_permutation(self, input: str):
        result = check_palindrome_permutation(input)
        assert result

    @pytest.mark.parametrize("input", ['code', 'denise', 'Not a Palindrome'])
    def test_false_palindrome_permutation(self, input: str):
        result = check_palindrome_permutation(input)
        assert not result


class TestOneEdit:

    @pytest.mark.parametrize(
        "string1, string2",
        [['pale', 'ple'], ['pales', 'pale'], ['pale', 'bale']]
    )
    def test_true_one_edit(self, string1, string2):
        result = check_one_edit(string1, string2)
        assert result

    @pytest.mark.parametrize(
        "string1, string2",
        [['pale', 'bake'], ['pale', 'le']]
    )
    def test_false_one_edit(self, string1: str, string2:str ):
        result = check_one_edit(string1, string2)
        assert not result


class TestStringComprehension:

    @pytest.mark.parametrize(
        "string, expected_string",
        [
            ['aabcccccaaa', 'a2b1c5a3'],
            ['abcd', 'abcd'],
            ['ddee', 'ddee'],
            ['ddeee', 'd2e3']
        ]
    )
    def test_string_comprehension(self, string: str, expected_string: str):
        result = string_comprehension(string)
        assert result == expected_string
