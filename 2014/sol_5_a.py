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

i = 0
while i < n - 1:
  if a[i]  <= a[i + 1]:
    print(a[i])
    print(a[i + 1])
  i = i + 2
