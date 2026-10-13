class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numberlist = set()
        # set because it can store unique 
        for number in nums:
            if number in numberlist:
                return True
            numberlist.add(number)
        return False