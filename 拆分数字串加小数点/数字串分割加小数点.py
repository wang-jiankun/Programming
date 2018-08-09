"""
牛客网编程题--2018拼多多--拆分数字串为两部分，每部分可加小数点也可以不加，输出所有可能的组合
author：王建坤
date：2018-8-8
"""
# import re
# 多字符匹配分割
# re.split(" |!|\?|\.", a)
# re.split(r'[\s;,]',line)

inp = input('输入').strip()
inp = str(inp)
l = len(inp)

result = []

for i in range(1, l):
    front = inp[0:i]
    l_front = len(front)
    back = inp[i:]
    l_back = len(back)
    for j in range(1, l_front+1):
        front1 = front[0:j]+'.'+front[j:]
        front1 = front1.strip('.')
        if '.' in front1:
            front1 = front1.rstrip('0').strip('.')
        if '.' in front1:
            front1 = float(front1.strip('.'))
        else:
            front1 = int(front1.strip('.'))
        for k in range(1, l_back+1):
            back1 = back[0:k] + '.' + back[k:]
            back1 = back1.strip('.')
            # 去掉小数后多余的0
            if '.' in back1:
                back1 = back1.rstrip('0').strip('.')
            if '.' in back1:
                back1 = float(back1.strip('.'))
            else:
                back1 = int(back1.strip('.'))
            result.append([front1, back1])

print(result)

