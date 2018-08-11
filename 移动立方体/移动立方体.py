"""
牛客网编程题--网易--移动立方体使塔的最大高度差最小
author：王建坤
date：2018-8-7
"""
# import numpy as np

# 塔的数量n和最多移动的次数k
n, k = map(int, input('输入:').strip().split())
# 各个塔的高度
num = list(map(int, input('输入:').strip().split()))
# 升序排序返回下标
numb = sorted(enumerate(num), key=lambda x: x[1])
numb = [x[0] for x in numb]
# num = np.array(num)
# numb = num.argsort()

# 最小的高度差s和移动次数m
s = 0
m = 0
# 存放每次移动的信息
move_list = []
# 循环k次
for i in range(k):
    # 如果最大高度差小于等于1，表明不能更好了
    if num[numb[-1]]-num[numb[0]] <= 1:
        break
    else:
        # 最高的塔移动一块给最低的塔
        num[numb[0]] += 1
        num[numb[-1]] -= 1
        # 移动次数+1
        m += 1
        # 移动的信息:从第几个塔移到第几个塔
        move_list.append([numb[-1]+1, numb[0]+1])
        # 再次排序
        numb = sorted(enumerate(num), key=lambda x: x[1])
        numb = [x[0] for x in numb]

# 最大高度差
s = num[numb[-1]] - num[numb[0]]

print(s, m)
for j in move_list:
    print(j[0], j[1])


