# file: library.py

# 模拟用户和图书库存
users = {"alice": {}, "bob": {}}
books = {"Python101": 3, "DataScience": 0, "MLBasics": 2}

def borrow_book(user, book):
    # 检查用户是否存在
    if user not in users:
        raise ValueError("用户不存在")

    # 检查图书是否存在
    if book not in books:
        raise ValueError("图书不存在")

    # 检查图书库存
    if books[book] <= 0:
        raise ValueError("图书库存不足")

    # 借书成功，库存减少
    books[book] -= 1
    return True
