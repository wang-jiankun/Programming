"""
牛客网编程题--拆分数字串为两部分，每部分可加小数点也可以不加，求满足一定规则的组合数
author：王建坤
date：2018-8-8
"""
# 获取输入的数字串
input_num = input('输入：').strip()

# 求组合数
kinds = 0
for i in range(1, len(input_num)):
    left = input_num[0:i]
    left_kind = 0
    right = input_num[i:]
    right_kind = 0

    # 左边
    # 只有一位数只有一种组合
    if len(left) == 1:
        left_kind = 1
    else:
        # 多位数但都是0，不符合
        if int(left) == 0:
            continue
        # 第一位和最后一位都是0，不符合
        elif left[0] == '0' and left[-1] == '0':
            continue
        # 第一位为0最后一位不为0，只有一种组合
        elif left[0] == '0' and left[-1] != '0':
            left_kind = 1
        # 多位数，前后都不为0，有位数个数中组合
        else:
            left_kind = len(left)

    # 右边
    if len(right) == 1:
        right_kind = 1
    else:
        if int(right) == 0:
            continue
        elif right[0] == '0' and right[-1] == '0':
            continue
        elif right[0] == '0' and right[-1] != '0':
            right_kind = 1
        else:
            right_kind = len(right)

    # 总的组合数=左组合数*右组合数
    kinds += left_kind*right_kind

print(kinds)







