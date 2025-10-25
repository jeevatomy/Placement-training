
n, k = map(int, input().split())
times = [int(input()) for _ in range(n)]

gifts = 0

for i in range(1, n):
    if times[i - 1] - times[i] >= k:
        gifts += 1

print(gifts)
