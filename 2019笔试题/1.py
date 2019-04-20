# while True:
#     try:
#         t = int(input())
#         for _ in range(t):
#             n = int(input())
#             s = list(map(int, input().split()))
#
#     except:
#         break


# s_l = ['RmAPP', 'ResouceScheduler', 'ApplicationMasterLauncher', 'RmContainer']
# o_l = ['start', 'app_accepted', 'container_allocated', 'launched', 'finished', 'kill']


def func(m, n, k):
    if m + n == 0 or k == 1:
        return 1
    if k > m + n:
        return func(m, n, m+n)
    else:
        return func(m, n-1, k-1) + func(m-n, n)


m, n, k = map(int, input().split())
print(func(m, n, k))

