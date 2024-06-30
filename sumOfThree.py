class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        """x=(num-3)/3 => num=x+( x+1) + (x+2)"""
        if num%3==0:
            x=(num-3)//3
            return [x, x+1, x + 2]
        return []
