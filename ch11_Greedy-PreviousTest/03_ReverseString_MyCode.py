str = list(map(int, input()))

count1 = 0
check = False
# 0으로 전부 만드는 횟수
for s in str:
    if s == 1: # 첫번째 1이 나오는 시점
        check = True
    if s == 0 and check == True:
        check = False
        count1 += 1

count2 = 0
# 1로 전부 만드는 횟수
for s in str:
    if s == 0: # 첫번째 1이 나오는 시점
        check = True
    if s == 1 and check == True:
        check = False
        count2 += 1

print(count1 if count1 < count2 else count2)