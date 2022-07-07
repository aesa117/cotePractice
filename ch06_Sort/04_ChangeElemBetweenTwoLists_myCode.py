n, k = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in range(k):
    a_value, b_value = min(A), max(B)
    a_index, b_index = A.index(a_value), B.index(b_value)
    A[a_index], B[b_index] = b_value, a_value

sum = 0
for i in range(len(A)):
    sum += A[i]

print(sum)