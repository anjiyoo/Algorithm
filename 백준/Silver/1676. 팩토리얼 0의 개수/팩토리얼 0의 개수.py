N = int(input())
	
fac = 1

for i in range(2, N + 1):
    fac *= i

str_fac = str(fac)	

cnt = 0

for i in range(len(str_fac)):	
    if str_fac[-1 - i] != '0':	
        break
    cnt += 1
print(cnt)