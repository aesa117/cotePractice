n, m = map(int, input().split())
k = list(map(int, input().split()))

count = 0
for i, val1 in enumerate(k):
    for j, val2 in enumerate(k[i+1:]):
        if val1 != val2:
            count += 1

print(count)