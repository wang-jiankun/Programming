"""
牛客网编程题--按规则取卡片最少多少次取完
author：王建坤
date：2018-8-8
"""
# 此程序未能考虑所有情况，待改进

# 获取卡片的个数
num = int(input('输入：').strip())

# 获取正整数序列
num_list = input().strip().split()
num_list = list(map(int, num_list))

# 从左到右按照升序/降序抽取卡片,取得次数最少
count = 0
flag = -1
while len(num_list) > 0:
    if len(num_list) == 1:
        count += 1
        del num_list[0]
        break
    else:
        greater_count = 0
        less_count = 0
        greater_list = num_list.copy()
        less_list = num_list.copy()

        # 降序取卡片，获得卡片数和剩余卡片列表
        h = 0
        k = 1
        while h < len(greater_list)-1 and k < len(greater_list):
            if greater_list[h] > greater_list[k]:
                del greater_list[h]
                greater_count += 1
                h = k - 1
            else:
                k += 1
        del greater_list[h]

        # 升序取卡片，获得卡片数和剩余卡片列表
        h = 0
        k = 1
        while h < len(less_list) - 1 and k < len(less_list):
            if less_list[h] < less_list[k]:
                del less_list[h]
                less_count += 1
                h = k - 1
            else:
                k += 1
        del less_list[h]

        # 选择能取得最多卡片的排序方式
        if greater_count > less_count:
            # 降序标志
            flag = 0
            num_list = greater_list.copy()
        else:
            # 升序标志
            flag = 1
            num_list = less_list.copy()
    count += 1
    print(num_list)
print(count)
