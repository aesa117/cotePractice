data = list(map(int, input()))

result = data[0]
for d in data[1:]:
    plus = result + d
    mul = result * d
    if plus > mul:
        result = plus
    else:
        result = mul

print(result)