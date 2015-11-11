n = eval(input())
i = 1
j = 10
result = 0
#  Hint:
#  123456 % 10  is 6
# 123456 % 100 is 56
# the integer division of 123456 by 10 is 12345 (one digit removed)

while n > 0:
  n1 = n % 1-
  n = n/10
  n2 = n % 10
  n = n/10
  if n1 >= n2:
    result = result + (n2 * j) + (n1 * i)
     i = i * 100
     j = j * 100

print(result)