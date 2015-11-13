 n = eval(input())
 i = 0
 A = [ ]
 while i < n:
  A[i] = eval(input())

# Reset counter
i = 0
isSorted = True
while i < n  and isSorted:
  if A[i] > A[i + 1]:
    isSorted = False
  i = i + 1

if isSorted:
  print("The list is sorted")
else:
  print("The list is not sorted")