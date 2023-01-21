import random
from typing import List


class Solution:
    # i = containsDuplicate([5, 6, 7])

    def __init__(self, nums: List[int]):
        self.nums = nums

    # def gen_list(self, length):
    #     for x in range(length):
    #         print(x + " ", end='')
    #     conta

    def containsDuplicate(nums: List[int]) -> bool:
        return False if len(set(nums)) == len(nums) else True


def runner(length) -> bool:
    myList = [random.randint(1, 10) for x in range(length)]
    print(list(myList))
    a = Solution
    print(a.containsDuplicate(myList))
