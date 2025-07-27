class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        fp = sp = len(nums) - 1
        while fp > -1:
            while nums[fp] != val and fp > -1:
                fp -= 1
                if fp == -1:
                    return sp+1
            nums[fp] = nums[sp]
            fp -= 1
            sp -= 1
        return sp+1