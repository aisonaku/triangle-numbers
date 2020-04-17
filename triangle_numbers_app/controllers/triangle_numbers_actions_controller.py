from triangle_numbers_app.models.triangle_number import TriangleNumber
from triangle_numbers_app.controllers.output_controller import OutputController

class TriangleNumbersActionsController:
    def print_all_nth_number_divisors(self, ordinal):
        num = TriangleNumber(ordinal)
        divisors = num.calculate_divisors()
        OutputController().output_result(num.value, divisors, 1, ordinal)

    def print_num_with_divisors_count(self, min_divisors_count):
        num, divisors = self.get_num_with_divisors_count(min_divisors_count)
        OutputController().output_result(num.value, divisors, 2, min_divisors_count)

    def get_num_with_divisors_count(self, min_divisors_count) -> [TriangleNumber, list]:
        i = 1
        while True:
            num = TriangleNumber(i)
            divisors = num.calculate_divisors()
            if len(divisors) >= min_divisors_count:
                return num, divisors
            i += 1