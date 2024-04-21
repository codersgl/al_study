"""
1、创建一个长度为n的列表模拟圈，并初始化为1到n的整数。
2、设置一个变量表示当前报数的位置，初始为0。
3、循环进行以下操作： a. 从当前报数位置开始报数，直到报数达到m。 b. 将报数到m的位置的人从圈中移除，并记录下这个人的编号。 c. 继续从下一个人开始报数，直到所有人都出圈。
4、输出按顺序出圈的人的编号。
"""


def josephus_problem(n, m):
    circle = list(range(1, n + 1))
    i = 0
    result = []

    while circle:
        i = (i + m - 1) % len(circle)  # 计算报数到m的人的位置
        result.append(circle.pop(i))  # 将报数到m的人移除并记录编号

    return result


# 测试样例
n, m = map(int, input().split())
print(*josephus_problem(n, m))
