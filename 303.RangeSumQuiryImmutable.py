class NumArray:
    def __init__(self, nums: List[int]):
        self.pre_fix=[0]
        for num in nums:
            self.pre_fix.append(self.pre_fix[-1]+num)
    def sumRange(self, left: int, right: int) -> int:
        left=self.pre_fix[left]
        right=self.pre_fix[right+1]
        return right-left

