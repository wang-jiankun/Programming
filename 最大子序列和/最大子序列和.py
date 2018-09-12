N, M = map(int, input().strip().split())
values = list(map(int, input().strip().split()))

max_sum = 0
this_sum = 0

for k in range(N):
    this_sum += values[k]
    if this_sum > max_sum:
        max_sum = this_sum
    elif this_sum < 0:
        this_sum = 0
print(max_sum)

