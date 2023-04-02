# -*- coding: utf-8 -*-
# @Time : 2022/10/7 15:48
# @Author : Andrew
# @File : Day10.7.py
# @Project : practice
from typing import List


# dict = {"a":1,"b":2}
# a = dict.items()
# for i in a:
#     if i[1] == 1:
#         print(i[0])
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            print(i, num)

            if target - num in hashtable:
                return [hashtable[target - num], i]
            print(nums[i])
            print(i)
            hashtable[nums[i]] = i
        return []


if __name__ == '__main__':
    a = Solution()
    b = a.twoSum([1, 2, 3, 4], 6)
    print(b)
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         hashtable = {}
#         for i,num in enumerate(nums):
#             if target - num in hashtable:
#                 return [hashtable[target-num],i]
#             hashtable[target-num]=i
