import pytest
from palindrome import is_palindrome

def test_simple_palindrome():
    assert is_palindrome("aba") == True

def test_case_insensitive():
    assert is_palindrome("Level") == True

def test_with_spaces():
    assert is_palindrome("n u r s e s r u n") == True

def test_not_palindrome():
    assert is_palindrome("hello") == False

def test_invalid_input():
    with pytest.raises(TypeError):
        is_palindrome(123)
