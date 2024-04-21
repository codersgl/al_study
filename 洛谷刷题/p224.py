"""
这道题主要考察的是找出数学规律的能力，
自己可以通过画出几个棋盘来，
推导出正方形和长方形的数学公式
"""

# input two positive integers n, m
n, m = map(int, input().split())
# initialize two variable
a = 0  # rectangle
b = 0  # square
if n >= m:
    for i in range(m):
        b += (n - i) * (m - i)
else:
    for i in range(n):
        b += (n - i) * (m - i)
if n < m:
    for i in range(n):
        t = m * (m + 1) // 2
        a += (i + 1) * (t - (m - n + i + 1))
else:
    for i in range(m):
        t = n * (n + 1) // 2
        a += (i + 1) * (t - (n - m + i + 1))
# output
print(b, a)
