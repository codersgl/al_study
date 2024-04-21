n, q = map(int, input().split())
n_lis = [{} for _ in range(n)]  # 初始化为n个空字典的列表
for _ in range(q):
    lis = list(map(int, input().split()))
    # 存储操作
    if lis[0] == 1:
        i, j, k = lis[1] - 1, lis[2], lis[3]
        if k == 0:
            n_lis[i].pop(j, None)  # 如果k为0，则清空该格子
        else:
            n_lis[i][j] = k  # 更新或设置字典中的值
    else:
        # 查询操作
        i, j = lis[1] - 1, lis[2]
        if j in n_lis[i]:  # 确保该格子有存过东西
            print(n_lis[i][j])
