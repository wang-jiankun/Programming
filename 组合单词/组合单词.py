"""
笔试题--拼多多--从已知的单词中挑选字母组合成字典序最小的新单词
author：王建坤
date：2018-8-30
"""
# N：词的个数 L：词的长度
N, L = map(int, input('输入:').strip().split())

# 词列表
words = []
for i in range(N):
    words.append(input().strip())

# 取出每个单词的每个位置的字符组成一个列表，去重排序后，组成大列表
ch = []
for j in range(L):
    temp = []
    for k in range(N):
        temp.append(words[k][j])
    # 去重
    temp = list(set(temp))
    # 排序
    temp.sort()
    ch.append(temp)

print(ch)

# for h in range(L):