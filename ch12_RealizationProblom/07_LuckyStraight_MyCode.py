n = list(map(int, input()))

mid = len(n) // 2
left = n[:mid]
right = n[mid:]

sum_left = 0
for i in left:
    sum_left += i

sum_right = 0
for i in right:
    sum_right += i

print('LUCKY' if sum_left == sum_right else 'READY')