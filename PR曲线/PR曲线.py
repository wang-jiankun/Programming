"""
笔试题--商汤
author：王建坤
date：2018-9-7
"""
# 输入样本的个数
n = int(input().strip())
# 输入样本数据，pos存正例的预测值，neg存负例的预测值
pos = []
neg = []
for i in range(n):
    lab, pre = map(float, input().strip().split())
    if lab == 1:
        pos.append(pre)
    else:
        neg.append(pre)

# 正例预测值排序
pos.sort(reverse=True)
t = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

# 正例的样本数
m = len(pos)

for j in t:
    # 判断为正/负例的阈值
    thresh = pos[int(m*j)-1]
    count = 0
    # 计算负例中的假正例FP
    for k in neg:
        if thresh <= k:
            count += 1

    # num = 0
    # for h in pos:
    #     if a <= h:
    #         num += 1
    #
    # print(int(num / (num + count) * 100 + 0.5))

    # 计算精确率precision
    print(int((m*j)/(m*j+count)*100+0.5))

# 输入输出样例
# 输入
# 20
# 1 0.999
# 1 0.998
# 1 0.997
# 1 0.996
# 1 0.995
# 1 0.991
# 1 0.992
# 1 0.993
# 1 0.994
# 1 0.990
# 0 0.001
# 0 0.002
# 0 0.003
# 0 0.004
# 0 0.005
# 0 0.008
# 0 0.010
# 0 0.110
# 0 0.201
# 0 0.111

# 输出
# 100
# 100
# 100
# 100
# 100
