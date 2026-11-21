class Solution(object):
    def containsNearbyDuplicate(self, nums, k):

        numbers = {}

        for index, num in enumerate(nums):
            if num in numbers and abs(index - numbers[num]) <= k:
                return True
            numbers[num] = index

        return False


