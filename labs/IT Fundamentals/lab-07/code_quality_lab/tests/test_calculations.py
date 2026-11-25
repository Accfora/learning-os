import pytest

from calculations import (
    analyze,
    calculate_average,
    count_positive,
    find_max,
)


def test_calculate_average():
    assert calculate_average([10, 20, 30]) == 20
    assert calculate_average([-10, 0, 10]) == 0
    assert calculate_average([5]) == 5


def test_find_max():
    assert find_max([1, 5, 3]) == 5
    assert find_max([-10, -5, -20]) == -5
    assert find_max([42]) == 42


def test_count_positive():
    assert count_positive([-1, 0, 1]) == 1
    assert count_positive([-5, -10, 0]) == 0
    assert count_positive([1, 2, 3, 4]) == 4


def test_average_empty_list():
    with pytest.raises(ValueError):
        calculate_average([])


def test_analyze_numbers_positive():
    assert analyze([10, 20, 30]) == (10, 30, 20.0)


def test_analyze_numbers_negative():
    assert analyze([-30, -10, -20]) == (-30, -10, -20.0)


def test_analyze_numbers_mixed():
    assert analyze([-10, 0, 10]) == (-10, 10, 0.0)


def test_analyze_numbers_single():
    assert analyze([7]) == (7, 7, 7.0)


def test_analyze_numbers_equal_values():
    assert analyze([4, 4, 4]) == (4, 4, 4.0)


def test_analyze_numbers_empty():
    with pytest.raises(ValueError):
        analyze([])
