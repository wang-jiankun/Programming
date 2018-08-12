"""
牛客网编程题--字节跳动--球迷群体统计
author：王建坤
date：2018-8-7
"""
# 已经遍历过的点
exist_list = []
# 地图
dt = []
# 球迷群组个数
count = 0
# 最大的球迷群体人数
max_num = 0

# M行N列
M, N = map(int, input().strip().split())

# 每个位置的标记
for i in range(M):
    temp = list(map(int, input().strip().split()))
    dt.append(temp)


# 遍历当前点的四周
def found(j, k, temp_stack):
    for x, y in [(j-1, k-1), (j-1, k), (j-1, k+1), (j, k+1), (j+1, k+1), (j+1, k), (j+1, k-1), (j, k-1)]:
        if (0 <= x <= M - 1) and (0 <= y <= N - 1) and (x*M+y+1 not in exist_list) and (dt[x][y] == 1):
            temp_stack.append([x, y])
    # return temp_stack


# 遍历地图
for j in range(M):
    for k in range(N):
        # 该点属于新群体的标记
        flag = 0
        # 该群体的人数
        num = 0
        # 如果该点已经遍历过或者值为0，跳过
        if (j*M+k+1 in exist_list) or (dt[j][k] == 0):
            continue
        # 否则该点可以划分新群体
        else:
            exist_list.append(j*M+k+1)
            flag = 1
            num += 1
            x = j
            y = k
            print("center:", x+1, y+1)
            # 存放相邻球迷的栈
            find_stack = []
            # 循环寻找相邻的球迷
            while True:
                found(x, y, find_stack)
                # 如果栈为空，跳出
                if find_stack == []:
                    break
                else:
                    current = find_stack.pop()
                    x, y = current[0], current[1]
                    if x*M+y+1 not in exist_list:
                        num += 1
                        if num > max_num:
                            max_num = num
                    exist_list.append(x * M + y + 1)

        if flag == 1:
            count += 1

print(count, max_num)

"""
10 10
0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 0 1 0 0 0
0 1 0 0 0 0 0 1 0 1
1 0 0 0 0 0 0 0 1 1
0 0 0 1 1 1 0 0 0 1
0 0 0 0 0 0 1 0 1 1
0 1 1 0 0 0 0 0 0 0
0 0 0 1 0 1 0 0 0 0
0 0 1 0 0 1 0 0 0 0
0 1 0 0 0 0 0 0 0 0
"""



