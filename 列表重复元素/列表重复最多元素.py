"""
笔试题--美团--给定n个元素的数组，求子连续k个数中有任一元素出现超过t次的序列数。
author：王建坤
date：2018-9-6
"""
# 输入参数
n, k, t = map(int, input().strip().split())
# 输入数组
p = list(map(int, input().strip().split()))
# 序列数
num = 0
# 数组遍历
for i in range(n-k+1):
    temp = p[i:i+k]
    # 计算子序列中个元素的个数
    for j in temp:
        if temp.count(j) >= t:
            num += 1
            break

print(num)

