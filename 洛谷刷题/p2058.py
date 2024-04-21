# # input
# # 读取一个整数n，表示接下来要输入的时间戳和信息的数量
# n = int(input())
# # 初始化一个列表，用于存储所有时间戳和相关信息
# new_list = []
#
# # process and output
# # 初始化一个指针，用于在new_list中移动
# pointer = 0
#
# # 开始一个循环，循环n次，每次处理一个时间戳和信息
# for i in range(n):
#     # 为每个时间戳初始化一个临时的集合，用于存储该时间戳下的所有不同信息
#     temp_set = set()
#     # 读取一行输入，将其按空格分割并转换为整数列表
#     lis = list(map(int, input().split()))
#     # 提取时间戳t（时间戳是列表的第一个元素）
#     t = lis[0]
#     # 提取信息列表（从列表的第三个元素开始）
#     info = lis[2:]
#     # 将时间戳和信息添加到new_list中
#     new_list.append([t, info])
#     # 计算当前时间戳与一天前的时间差
#     difference = t - 86400
#     # 移动pointer，直到它指向的时间戳小于或等于当前时间戳减去一天
#     while pointer < len(new_list) and difference >= new_list[pointer][0]:
#         pointer += 1
#
#     # 遍历从pointer开始到new_list末尾的所有元素
#     for j in new_list[pointer:]:
#         # 将这些元素中的信息添加到temp_set中，自动去重
#         temp_set.update(j[1])
#
#     # 输出不同信息的数量
#     print(len(temp_set))

# 优化解
from collections import deque

# input
# 读取一个整数n，表示接下来要输入的时间戳和信息的数量
n = int(input())

# 初始化一个双端队列，用于存储所有时间戳和相关信息
new_deque = deque()

# process and output
# 初始化一个变量，用于记录一天前的时间戳
one_day_before = 0

# 开始一个循环，循环n次，每次处理一个时间戳和信息
for i in range(n):
    # 读取一行输入，将其按空格分割并转换为整数列表
    lis = list(map(int, input().split()))
    # 提取时间戳t（时间戳是列表的第一个元素）
    t = lis[0]
    # 提取信息列表（从列表的第三个元素开始）
    info = lis[2:]
    # 将时间戳和信息添加到new_deque中
    new_deque.append([t, info])

    # 清除deque中超过一天的时间戳和信息
    while new_deque and new_deque[0][0] <= t - 86400:
        new_deque.popleft()

    # 使用集合来存储当前时间戳下的所有不同信息
    temp_set = set()
    for _, info in new_deque:
        temp_set.update(info)

    # 输出不同信息的数量
    print(len(temp_set))
