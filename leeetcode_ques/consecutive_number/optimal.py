class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        num_ones = 0
        max_ones = 0

        for num in nums:
            if num == 0:
                num_ones = 0
            else:
                num_ones += 1
                if num_ones > max_ones:
                    max_ones = num_ones

        return max_ones
