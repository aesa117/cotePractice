#N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())

#N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() #입력받은 수들 정렬하기
first = data[n-1] #가장 큰 수
second = data[n-2] #두 번째로 큰 수

result = 0

while True:
    for i in range(k): #가장 큰 수로 K번 더하고 두 번째로 큰 수를 한 번 더함!
        if m == 0: #m이 0이 되면 반복문을 나감
            break
        result += first
        m -= 1
    if m == 0: #마찬가지로 m이 0이 되면 반복문 나감
        break
    result += second
    m -= 1

print(result)



