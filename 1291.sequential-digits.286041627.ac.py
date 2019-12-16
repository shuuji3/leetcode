class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        min_length = len(str(low))
        max_length = len(str(high))
        sequential_digits_list = []

        for length in range(min_length, max_length+1):
            for sequential_digits in self.generate_sequential_digits(length):
                if low <= sequential_digits <= high:
                    sequential_digits_list.append(sequential_digits)
        return sorted(sequential_digits_list)

    def generate_sequential_digits(self, length: int) -> int:
        for start_digit in range(1, 10-length+1):
            sequential_digits = ''
            for i in range(length):
                sequential_digits += str(start_digit + i)
            yield int(sequential_digits)
