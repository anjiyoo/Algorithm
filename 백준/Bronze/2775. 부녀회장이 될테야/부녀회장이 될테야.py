T = int(input())

for i in range(T):
    k = int(input()) 
    n = int(input()) 
    B = [[i for i in range(15)]]
    
    for j in range(1,k+1):
        B.append([])
        for _ in range(n+1):
            B[j].append(sum(B[j-1][:_+1]))
            
    print(B[k][n])