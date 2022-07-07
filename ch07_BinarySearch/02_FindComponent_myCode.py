def check(list_n, data):
    start, end = 0, len(list_n) - 1
    while start <= end:
        mid = (start + end) // 2
        if list_n[mid] == data:
            return True
        elif list_n[mid] > data:
            end = mid - 1
        else:
            start = mid + 1
    return False

n = int(input())
list_n = list(map(int, input().split()))
for i in range(n):
    list_n[i] = int(list_n[i])
list_n.sort()

m = int(input())
list_m = list(map(int, input().split()))
for i in range(m):
    list_m[i] = int(list_m[i])

for i in range(m):
    if check(list_n, list_m[i]) == False:
        print("no", end=' ')
    else:
        print("yes", end=' ')

