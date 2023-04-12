class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        final_sum = nums[0]
        for i in nums:
            cur_sum += i  
            if final_sum < cur_sum:
                final_sum = cur_sum
            if cur_sum < 0:
                cur_sum = 0
        return final_sum
