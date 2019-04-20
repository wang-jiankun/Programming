"""
腾讯实习笔试编程题
date: 2019-4-7
"""
# # 第一题（AC）
# import math
#
# n, k = map(int, input().strip().split())
#
# res = 0
# use = 0
#
# for i in range(1, k+1):
#     if 2**i >= n:
#         use = i
#         break
#
# if use == 0:
#     res = math.ceil(n/(2**k)) + k
# else:
#     res = use + 1
#
# print(res)

# # 第二题（AC）
# n = int(input())
# s = list(map(int, input().split()))
#
# res = 0
# for i in range(len(s) - 1):
#     s[i + 1] += s[i]
#     if s[i] > 0:
#         res += s[i]
#     elif s[i] < 0:
#         res += -s[i]
#
# print(res)


# 第三题（通过20%，后面补充完不确定对不对）
# n, k = map(int, input().strip().split())
#
# s = list(map(int, input().split()))
# s.sort()
#
# res = 0
# for i in range(k):
#     if s[n-1]-res == 0:
#         print(0)
#         break
#
#     num_min = s[i] - res
#     if num_min == 0:
#         continue
#     print(num_min)
#     res += num_min

