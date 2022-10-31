class Solution:
    
    #Swapping function
    def swap(self, nums, indx1, indx2):
        temp = nums[indx1]
        nums[indx1] = nums[indx2]
        nums[indx2] = temp
    
    #Reversing function for the pointers
    def reverse(self, nums, beg, end):
        while beg<end:
            self.swap(nums, beg, end)
            beg +=1
            end -=1
        
    #Permutation function
    def nextPermutation(self, nums: List[int]) -> None:
        if len(nums) == 1:
            return
        if len(nums) == 2:
            return self.swap(nums, 0, 1)
        dec = len(nums) - 2 #we use '-2' because we do not need to access the last element
        while dec>=0 and nums[dec]>=nums[dec+1]: #Putting the ascending order condition
            dec -= 1
        self.reverse(nums, dec+1, len(nums)-1)
        if dec == -1:
            return
        next_num = dec + 1
        while next_num < len(nums) and nums[next_num]<= nums[dec]:
            next_num +=1
        self.swap(nums, next_num, dec)
        
        
