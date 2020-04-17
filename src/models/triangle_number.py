class TriangleNumber:
    def __init__(self, ordinal):
        self.ordinal = ordinal

    def calculate_number(self) -> int:
        return self.ordinal * (self.ordinal + 1) // 2