# 정수 2개(a, b) 를 입력받아 a를 b로 나눈 나머지를 출력해보자.

a, b = input().split()
c = int(a) % int(b)  # %는 나머지 출력
print(c)