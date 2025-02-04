from collections import Counter

N = int(input())
org_list = list(map(str,input().split()))

M = int(input())
new_list = list(map(str,input().split()))

Cnt = Counter(org_list)

for num in new_list:
    if num in Cnt:
        print(Cnt[num],end=' ')
    else:
        print(0,end=' ')