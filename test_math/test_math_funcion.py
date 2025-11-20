import math
import pytest

def test_sqrt_positive():
    # 正常分支
    assert math.sqrt(9) == 3

def test_sqrt_negative():
    # 异常分支（sqrt 不能处理负数，应该抛异常）
    with pytest.raises(ValueError):
        math.sqrt(-1)

def test_factorial_branches():
    # factorial 两个逻辑：正常计算 & 异常输入
    assert math.factorial(5) == 120
    with pytest.raises(ValueError):
        math.factorial(-3)
