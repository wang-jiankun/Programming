"""
牛客网编程题--输入字符串从左上角按顺时针输出空心的正方形
author：王建坤
date：2018-8-7
"""

# 获取输入求正方形边长
input_str = input('输入：').strip()
num = len(input_str)
length = int(num/4 + 1)

# 第一行
print(input_str[0:length])

# 中间行，中间为空格
if num > 2:
    j = 0
    for i in range(length-2):
        print(input_str[length+j]+' '*(length-2)+input_str[length+j+1])
        j += 2

# 最后一行
print(input_str[num-length:])
