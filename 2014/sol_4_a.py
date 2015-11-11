n = int(input())

i = 0
a = [ ]
# Read values from user
while i < n:
  prompt = "Enter element %d" % i
  # prompt = Enter element 0
  # prompt = Enter element 1
  # ...
  value = eval(input(prompt))
  a.append(value)
  i = i + 1

flag = False
if n >= 3:
  i = 0
  while i < n - 1 and not flag:
    if a[i + 1] - a[i] == 3 and a[i + 2] -  a[i] == -1:
      flag = True
    i = i + 1

print(flag)

