from math_series import __version__
from math_series.math_series import fibonacci, lucas, sum_series

def test_version():
    assert __version__ == '0.1.0'

# fibonacci tests

def test_fib_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_fib_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_fib_two():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def test_fib_six():
    actual = fibonacci(6)
    expected = 8
    assert actual == expected

# lucas

def test_luc_zero():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_luc_one():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_luc_two():
    actual = lucas(2)
    expected = 3
    assert actual == expected

def test_luc_six():
    actual = lucas(6)
    expected = 18
    assert actual == expected

# Sum Series

# Sum Series without optional params added

def test_sum_series_zero():
    actual = sum_series(0)
    expected = 0
    assert actual == expected

def test_sum_series_one():
    actual = sum_series(1)
    expected = 1
    assert actual == expected

def test_sum_series_two():
    actual = sum_series(2)
    expected = 1
    assert actual == expected

def test_sum_series_six():
    actual = sum_series(6)
    expected = 8
    assert actual == expected

# Sum Series with optional -Lucas- arguments 2 and 1

def test_sum_series_luc_zero():
    actual = sum_series(0, 2, 1)
    expected = 2
    assert actual == expected

def test_sum_series_luc_one():
    actual = sum_series(1, 2, 1)
    expected = 1
    assert actual == expected

def test_sum_series_luc_two():
    actual = sum_series(2, 2, 1)
    expected = 3
    assert actual == expected

def test_sum_series_luc_six():
    actual = sum_series(6, 2, 1)
    expected = 18
    assert actual == expected

# Sum Series with optional -Other- arguments

def test_sum_series_other_zero_eight():
    actual = sum_series(0, 8)
    expected = 8
    assert actual == expected

def test_sum_series_other_one_three_five():
    actual = sum_series(1, 3, 5)
    expected = 5
    assert actual == expected

def test_sum_series_other_two_two_one():
    actual = sum_series(2, 2, 1)
    expected = 3
    assert actual == expected

def test_sum_series_other_six_two_six():
    actual = sum_series(6, 2, 6)
    expected = 58
    assert actual == expected

def test_sum_series_other_seven_nine_six():
    actual = sum_series(7, 9, 6)
    expected = 150
    assert actual == expected


