n = int(input())
array = []
for i in range(n):
    array.append(int(input()))
    for j in range(i-1, 0, -1):
            if array[j-1] < array[j]:
                array[j-1], array[j] = array[j], array[j-1]
            else:
                break

for i in range(n):
    print(array[i], end=' ')