from models.triangle_number import TriangleNumber
from controllers.output_controller import OutputController

class TriangleNumbersActionsController:
    def print_all_nth_number_divisors(self, ordinal):
        num = self._get_nth_number(ordinal)
        divisors = self._calculate_divisors(num)
        OutputController().output_result(num, divisors, 1, ordinal)

    def print_num_with_divisors_count(self, min_divisors_count):
        i = 1
        while True:
            num = TriangleNumber(i).calculate_number()
            divisors = self._calculate_divisors(num)
            if len(divisors) >= min_divisors_count:
                OutputController().output_result(num, divisors, 2, min_divisors_count)
                return
            i += 1

    def _get_nth_number(self, ordinal) -> int:
        num = TriangleNumber(ordinal)
        return num.calculate_number()

    def _calculate_divisors(self, num) -> list:
        divisors = []
        for i in range(1, int(num / 2) + 1):
            if num % i == 0:
                divisors.append(i)
        divisors.append(num)
        return divisors
