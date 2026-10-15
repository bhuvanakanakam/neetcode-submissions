class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {} # have a track of the elements you already saw

        # for number1 in nums:
        #     number2 = target - number1
        #     if number2 in seen :
        #         return [seen[number2], nums[number1]]

        # using enumerate -> value and position

        for position, number1 in enumerate(nums):
            number2 = target - number1
            if number2 in seen:
                return [seen[number2], position]
            else :
                seen[number1] = position

        # approach 1 : nested for loop, checking with each element sum
        # Time - O(n^2)
