m = int(input())
i = 0
a = [ ]
while i < m:
  value = eval(input())
  a.append(value)
  i = i + 1

n = int(input())
b = [ ]
i = 0
while i < n:
  value = eval(input())
  b.append(value)
  i = i + 1

i = 0
j = 0
flag = True

if m > n:
  while i <= n and j <= m and flag:
    if a[j] < b[i]:
      j = j + 1
    elif a[j] == b[i]:
      i = i + 1
      j = j + 1
    elif a[j] > b[i]:
      flag = False

if i <= n or not flag:
  print("Mysterious No")
else:
  print("Mysterious Yes")

