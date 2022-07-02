n = int(input())

count = 0

for h in range(0, n+1):
    for m in range(0, 60):
        for s in range(0, 60):
            if h % 10 == 3 or m % 10 == 3 or s % 10 == 3 or (m//10) == 3 or (s//10) == 3:
                count += 1

print(count)