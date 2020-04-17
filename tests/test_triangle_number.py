import pytest
from triangle_numbers_app.models.triangle_number import TriangleNumber


@pytest.mark.parametrize("input_ordinal, expected_number", [(1, 1), (5, 15), (10, 55)])
def test__calculate_number(input_ordinal, expected_number):
    triangle_number = TriangleNumber(input_ordinal)
    assert(triangle_number.value == expected_number)


@pytest.mark.parametrize("input_ordinal, expected_divisors", [(1, [1]), (5, [1, 3, 5, 15]), (10, [1, 5, 11, 55])])
def test_calculate_divisors(input_ordinal, expected_divisors):
    triangle_number = TriangleNumber(input_ordinal)
    assert(triangle_number.calculate_divisors() == expected_divisors)