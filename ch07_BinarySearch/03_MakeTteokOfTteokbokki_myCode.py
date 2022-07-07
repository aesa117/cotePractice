n, m = map(int, input().split())
array = list(map(int, input().split()))

max_height = max(array)
for i in range(max_height, 0, -1):
    sum = 0
    for j in range(n):
        if array[j] - i > 0:
            sum += array[j] - i
    if sum >= m:
        print(i)
        break

