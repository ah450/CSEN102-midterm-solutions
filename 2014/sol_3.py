a = eval(input())
b = eval(input())
c = eval(input())

aa = a % 10
bb = b % 10
cc = c % 10

if aa >= 5:
  a = 10 + a - aa
else:
  a = a - aa

if bb >=5:
  b = 10 + b - bb
else:
  b = b - bb

if cc >= 5:
  c = 10 + c - cc
else:
  c = c -cc

sum = a + b + c

print(sum)