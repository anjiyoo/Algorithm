# 2개의 정수값이 입력될 때 그 불 값이 하나라도 True일 때에만 True를 출력하는 프로그램을 작성해보자.

a, b = input().split()
print(bool(int(a)) or bool(int(b)))