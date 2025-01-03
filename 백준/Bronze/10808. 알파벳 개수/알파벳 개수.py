inputString = input()
countArray = [0] * 26
for str in inputString:
  countArray[ord(str) - 97] += 1
print(*countArray)