"""
牛客网编程题--求和某用户有最多共同好友的用户
author：王建坤
date：2018-8-7
"""

# 获取用户数N和需要判断的序号index
input_info = input('输入：').strip().split()
N, index = int(input_info[0]), int(input_info[1])
# print(N, index)

# 获取所有用户的好友列表
friend_list = []
for i in range(N):
    single_usr = input().strip().split()
    single_usr = list(map(int, single_usr))
    friend_list.append(single_usr)
# print(friend_list)

# 根据序号筛选得到与之不是好友的用户序号
match_list = []
for j in range(N):
    if index not in friend_list[j] and index != j:
        match_list.append(j)
# print(match_list)

# 一一对比得到共同好友数
max_num = 0
match_index = -1
for k in range(len(match_list)):
    count = 0
    for friend in friend_list[index]:
        if friend in friend_list[match_list[k]]:
            count += 1
    if count > max_num:
        max_num = count
        match_index = match_list[k]

print(match_index)
