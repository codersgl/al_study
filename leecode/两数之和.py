"""考虑使用哈希表（或Python中的字典）来减少时间复杂度。
基本思路是遍历数组一次，对于每个元素，检查target减去该元素的值是否已经在哈希表中。
如果在，那么直接返回这两个数的索引；如果不在，就把这个元素和它的索引加入到哈希表中。
这样可以将时间复杂度从O(n^2)降低到O(n)。"""


def twoSum(nums: list, target: int) -> list:
    num_dict = {}  # 创建一个字典来存储数字和对应的索引
    for index, num in enumerate(nums):  # 遍历数组中的每个数字和它们的索引
        complement = target - num  # 计算目标值与当前数字的差值
        if complement in num_dict:  # 如果差值在字典中，返回它们的索引
            return [num_dict[complement], index]
        num_dict[num] = index  # 如果差值不在字典中，将当前数字和索引添加到字典
