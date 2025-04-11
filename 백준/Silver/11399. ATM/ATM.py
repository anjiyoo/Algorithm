N = int(input())  
P = list(map(int, input().split()))  
time = []  
t_sum = 0  

P.sort()  

for i in range(len(P)):
    t_sum += P[i]
    time.append(t_sum)


result = 0  
for j in time:
    result += j

print(result)