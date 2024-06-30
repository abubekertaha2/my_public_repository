class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """my_dict={num: False for num in nums}
        longest=0
        next_num=num+1
        while next_num in my_dict 
        set_num=set(nums)
        length=0
        for n  in set_num:
            if (n-1) not in set_num:
                res=0
                while(n+res) in set_num:
                    res+=1
                length=max(res,length)
        return length"""
        num_dict = {}
        for num in nums:
            num_dict[num] = True
    
        longest_seq = 0
        for num in nums:
            if num - 1 not in num_dict:
                current_num = num
                count= 0
                while current_num  in num_dict and num_dict[current_num]:
                    num_dict[current_num] = False  
                    current_num += 1
                    count += 1
                longest_seq = max(longest_seq, count)
        return longest_seq
