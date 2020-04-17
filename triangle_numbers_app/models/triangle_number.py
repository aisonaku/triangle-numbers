class TriangleNumber:
    def __init__(self, ordinal):
        self.__ordinal = ordinal
        self.__value = self._calculate_number()

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    def _calculate_number(self) -> int:
        return self.__ordinal * (self.__ordinal + 1) // 2

    def calculate_divisors(self) -> list:
        num = self.__value
        divisors = []
        for i in range(1, int(num / 2) + 1):
            if num % i == 0:
                divisors.append(i)
        divisors.append(num)
        return divisors