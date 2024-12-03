# 격자판의 세로(h), 가로(w), 막대의 개수(n), 각 막대의 길이(l),
# 막대를 놓는 방향(d:가로는 0, 세로는 1)과
# 막대를 놓는 막대의 가장 왼쪽 또는 위쪽의 위치(x, y)가 주어질 때,

# 격자판을 채운 막대의 모양을 출력하는 프로그램을 만들어보자.

h, w = input().split()
h = int(h)
w = int(w)

p = []
for i in range(h+1):
    p.append([])
    for j in range(w+1):
        p[i].append(0)

n = int(input())
for i in range(n):
    l, d, x, y = input().split()
    l = int(l)
    d = int(d)
    x = int(x)
    y = int(y)
    if d == 0:
        for j in range(l):
            p[x][y+j] = 1
    else:
        for j in range(l):
            p[x+j][y] = 1

for i in range(1, h+1):
    for j in range(1, w+1):
        print(p[i][j], end=' ')
    print()
