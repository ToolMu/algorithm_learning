class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        out_dict = dict()
        for index, value in enumerate(nums):
            sub = target - value
            if sub in out_dict:
                return [out_dict[sub], index]
            else:
                out_dict[value] = index


if __name__ == "__main__":
    test_group = [{"nums": [2, 7, 5, 11], "target": 9, "result": [0, 1]}]
    solution = Solution()
    for test_item in test_group:
        print("+-------+")
        print("  nums: {}".format(test_item['nums']))
        print("  target: {}".format(test_item['target']))
        print("  result: {}".format(test_item['result']))
        print("  solution: {}".format(
            solution.twoSum(test_item['nums'], test_item['target'])))
