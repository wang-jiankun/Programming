"""
笔试题--迅雷--一个正数一个负数，组成17个数，相邻7个数和小于0，求17个数最大和
author：王建坤
date：2018-9-12
"""
# 输入正负数
pos, neg = map(int, input().strip().split())

# 计算正数个数
radio = (-neg)/(pos-neg)
pos_num = int(7*radio)

# 考虑最后3个数
if pos_num <= 3:
    res = 3*pos_num * pos + (2*(7-pos_num)+(3-pos_num))*neg
else:
    res = (2*pos_num+3) * pos + 2*(7-pos_num)*neg

print(res)