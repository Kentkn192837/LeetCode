class Solution:
    '''
    Example
    nums: [2,7,10,15]
    target: 9
    Output: [0,1]
    numsから足してtargetになる値のインデックス番号のリストで返す
    '''
    def twoSum(self, nums, target):
        comp = {}
        for key, value in enumerate(nums):
            search = target - value
            print(search not in comp)
            if search not in comp:
                comp[value] = key
            else:
                return [comp[search], key]

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument('nums', type=int, nargs='+')
    parser.add_argument('target', type=int)

    args = parser.parse_args()
    print(args.nums)
    print(Solution().twoSum(args.nums, int(args.target)))
