"""
牛客网编程题--拆分数字串为两部分，每部分可加小数点也可以不加，求满足一定规则的组合数
author：王建坤
date：2018-8-8
"""
# 获取输入的数字串
input_num = input('输入：').strip()

kinds = 0
for i in range(1, len(input_num)-1):
    left = input_num[0:i]
    left_kind = 0
    right = input_num[i:]
    right_kind = 0

    # 左边
    if len(left) == 1:
        left_kind = 1
    else:
        if int(left) == 0:
            continue
        elif left[0] == '0' and left[-1] == '0':
            continue
        elif left[0] == '0' and left[-1] != '0':
            left_kind = 1
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
            right_kind = len(left)

    # 组合数
    kinds += left_kind*right_kind

print(kinds)







