n = int(input())
array = []

for i in range(n):
    name, score = map(str, input().split())
    score = int(score)
    array.append([name, score])

def second(data):
    return data[1]

array.sort(key=second)

for arr in array:
    print(arr[0], end=' ')