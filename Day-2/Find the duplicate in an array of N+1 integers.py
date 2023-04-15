class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sets = set()
        for i in nums:
            if i in sets:
                return i
            sets.add(i)
