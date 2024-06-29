from typing import List

class MySolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    result.append(i)
                    result.append(j)
        return result

print(MySolution().twoSum([2, 7, 11, 15], 9)) # [0, 1]


# 模範解答
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i, num in enumerate(nums):
            # 目標値から現在の数字を引いた結果を保持します
            complement = target - num

            # complementがハッシュテーブルに存在するかを確認します
            if complement in dic:
                # ある場合、そのインデックスと現在のインデックスを返します
                return [dic[complement], i]
            else:
                # ない場合、現在の数字とそのインデックスをハッシュテーブルに追加します
                dic[num] = i

print(Solution().twoSum([2, 7, 11, 15], 9)) # [0, 1]

"""
目標値から現在の数字を引いた結果を保持して、
その結果がハッシュテーブルに存在するかを確認することで、
O(N) で解ける。
"""
