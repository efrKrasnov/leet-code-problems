class Solution:
    def countLargestGroup(self, n: int) -> int:
        sums_count = {}
        def sum_of_digits(number):
            sum_value = 0
            while number > 0:
                sum_value += number % 10
                number //= 10
            return sum_value
        
        for i in range(1, n+1):
            current_digit_sum = sum_of_digits(i)
            if sums_count.get(current_digit_sum) is None:
                sums_count[current_digit_sum] = 1
            else:
                sums_count[current_digit_sum] += 1
        counts = list(sums_count.values())
        max_counts = max(counts)
        return counts.count(max_counts)
            