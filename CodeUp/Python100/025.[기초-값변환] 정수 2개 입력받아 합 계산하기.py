# 정수 2개를 입력받아 합을 출력하는 프로그램을 작성해보자.

a, b = input().split()
c  = int(a) + int(b)  # input()으로 받는 값은 문자열이어서 int를 사용해 정수로 형변환
print(c)