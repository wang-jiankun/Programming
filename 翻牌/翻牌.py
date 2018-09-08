"""
笔试题 -- 网易 -- 矩阵翻牌
author：王建坤
date：2018-9-8
"""
# n 组测试样例
n = int(input().strip())

for i in range(n):
    # 行和列
    row, col = map(int, input().strip().split())
    # 分为几种情况讨论，按照有几个相邻的格子+自己来考虑最终是否被翻转
    # 只有1行
    if row == 1:
        if col == 1:
            print(1)
        elif col == 2:
            print(0)
        else:
            print(col-2)
    # 只有1列
    elif col == 1:
        if row == 2:
            print(0)
        else:
            print(row-2)

    # 超过2行2列，四周都没被翻转，中间的都被翻转
    else:
        print((row-2)*(col-2))

