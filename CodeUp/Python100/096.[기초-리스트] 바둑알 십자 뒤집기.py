# 바둑판(19 * 19)에 흰 돌(1) 또는 검정 돌(0)이 모두 꽉 채워져 놓여있을 때,
# n개의 좌표를 입력받아 십(+)자 뒤집기한 결과를 출력하는 프로그램을 작성해보자.

a = []
for i in range(20):
    a.append([])
    for j in range(20):
        a[i].append(0)

for i in range(19):
    b = input().split()
    for j in range(19):
        a[i+1][j+1] = int(b[j])

n = int(input())
for i in range(n):
    x,y = map(int,input().split())
    for j in range(1,20):
        if a[j][y] == 0: a[j][y] = 1
        else: a[j][y] = 0
        
        if a[x][j] == 0: a[x][j] = 1
        else: a[x][j] = 0

for i in range(1,20):
    for j in range(1,20):
        print(a[i][j],end = ' ')
    print()