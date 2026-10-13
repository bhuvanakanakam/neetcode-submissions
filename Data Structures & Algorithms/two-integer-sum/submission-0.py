class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for numberposition, number1 in enumerate(nums):
            number2 = target - number1
            if number2 in seen:
                    return [seen[number2], numberposition]
            seen[number1] = numberposition
        return[]