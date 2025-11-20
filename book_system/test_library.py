# file: test_library.py
import pytest
from library import borrow_book, users, books

def test_borrow_normal():
    books["Python101"] = 3  # 重置库存
    assert borrow_book("alice", "Python101") is True
    assert books["Python101"] == 2

def test_user_not_exist():
    with pytest.raises(ValueError):
        borrow_book("charlie", "Python101")

def test_book_not_exist():
    with pytest.raises(ValueError):
        borrow_book("alice", "UnknownBook")

def test_book_out_of_stock():
    books["DataScience"] = 0
    with pytest.raises(ValueError):
        borrow_book("alice", "DataScience")

def test_multiple_borrows():
    books["MLBasics"] = 2
    assert borrow_book("bob", "MLBasics") is True
    assert books["MLBasics"] == 1
    assert borrow_book("bob", "MLBasics") is True
    assert books["MLBasics"] == 0
    with pytest.raises(ValueError):
        borrow_book("bob", "MLBasics")
