def dfs(s):   
    for i in range(n):
        if visited[i] == '0' and graph_list[s][i] == 1:
            visited[i] = '1'    
            dfs(i)  

n = int(input())
graph_list = []
for i in range(n):
    graph_list.append(list(map(int,input().split())))   

for i in range(n):
    visited = ['0' for _ in range(n)]  
    dfs(i)
    print(' '.join(visited))   