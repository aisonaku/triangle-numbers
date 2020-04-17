import pytest
from triangle_numbers_app.controllers.triangle_numbers_actions_controller import TriangleNumbersActionsController

@pytest.mark.parametrize("input_divisors_counter, expected_number", [(1, 1), (3, 6), (4, 6)])
def test_get_num_with_divisors_count(input_divisors_counter, expected_number):
    triangle_number, divisors = TriangleNumbersActionsController().get_num_with_divisors_count(input_divisors_counter)
    assert(triangle_number.value == expected_number)
