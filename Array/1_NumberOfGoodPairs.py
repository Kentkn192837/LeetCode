from collections import defaultdict
from typing import List

def numIdenticalPairs(nums: List[int]) -> int:
    resultDict = defaultdict(int)
    max_value = 0
    for i in range(len(nums) - 1):
        for j in range(i+1, len(nums)):
            print(f"i: {i}, j: {j}")
            if nums[i] == nums[j]:
                resultDict[nums[i]] += 1
                print(resultDict)
                max_value = max(max_value, resultDict[nums[i]])
    return max_value

print(numIdenticalPairs([1, 2, 3, 1, 1, 3])) # 4



# LeetCode 1512. Number of Good Pairs
# 模範解答
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        num_of_good_pairs = 0
        # 各数字の出現回数を格納するための辞書を初期化
        cnts = defaultdict(int)

        for i in range(len(nums)):
            cnts[nums[i]] += 1

        print(f"cnts.values(): {cnts.values()}")
        for cnt in cnts.values():
            # 組合せの計算 N * (N - 1) / 2
            num_of_good_pairs += cnt * (cnt - 1) // 2

        return num_of_good_pairs

print(Solution().numIdenticalPairs([1, 2, 3, 1, 1, 3])) # 4

"""
配列を先頭から見ていき、出現した数値をそれぞれ、
```
cnt[nums[i]] += 1
```
でカウントすればよいので、二重ループを使わずに、O(N) で解ける。

同じ数字の組み合わせを計算したいので、
cnts.values() で各数字の出現回数を取得し、
組み合わせの計算を行う。
"""
