n = int(input())
maps = []

for _ in range(n):
    maps.append(list(map(int,input())))

def dfs(x,y):
    global cnt
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if maps[nx][ny] == 1:
                maps[nx][ny] = 0
                cnt += 1
                dfs(nx,ny)
    return cnt 

li = []
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            cnt = 1
            maps[i][j] = 0
            cnt = dfs(i,j)
            li.append(cnt)

print(len(li))
li.sort()

for num in li:
    print(num)