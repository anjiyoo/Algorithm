# 정수 2개(a, b)를 입력받아 a를 b번 곱한 거듭제곱을 출력하는 프로그램을 작성해보자.

a, b = input().split()
c = int(a)**int(b)  # **는 거듭제곱
print(c)