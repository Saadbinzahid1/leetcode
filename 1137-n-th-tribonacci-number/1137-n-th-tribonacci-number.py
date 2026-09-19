class Solution:
    def tribonacci(self, n: int) -> int:
        t_1 = 0
        t_2 = 1
        t_3 = 1

        for _ in range(n):
            t_1, t_2, t_3 = t_2, t_3, t_1 + t_2 + t_3
        
        return t_1