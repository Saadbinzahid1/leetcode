class Solution:
    def fib(self, n: int) -> int:
        first_term, second_term = 0, 1

        for _ in range(n):
            first_term, second_term = second_term, first_term + second_term
        
        return first_term