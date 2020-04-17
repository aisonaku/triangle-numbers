import time
from models.triangle_number import TriangleNumber

class TriangleNumbersActionsController:
    def print_all_nth_number_divisors(self, ordinal):
        triangle_number = self._get_nth_number(ordinal)
        divisors = self._calculate_divisors(triangle_number)
        print(str(triangle_number) + ": " + ', '.join(map(str, divisors)))

    def print_num_with_divisors_count(self, min_divisors_count):
        i = 0
        while True:
            num = TriangleNumber(i)
            divisors = self._calculate_divisors(num)
            if len(divisors) >= min_divisors_count:
                print(str(num) + ": " + ', '.join(map(str, divisors)))
                return

    def _get_nth_number(self, ordianl) -> int:
        num = TriangleNumber(ordianl)
        return num.calculate_number()

    def _calculate_divisors(self, num) -> list:
        divisors = []
        for i in range(1, int(num / 2) + 1):
            if num % i == 0:
                divisors.append(i)
        divisors.append(num)
        return divisors