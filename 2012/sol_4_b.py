 n = eval(input())
 i = 0
 A = [ ]
 while i < n:
  A[i] = eval(input())

i = 0
maxValue = -1

while i < n:
  if maxValue < A[i]:
    maxValue = A[i]
  i = i + 1

i = 0
# A list of length maxValue where each element is a negative one
B = [-1] * maxValue
while i < n:
  B[A[i]] = A[i]
  i = i + 1

i = 0
# In order to print them on one line
# We must construct a new string
# and use print that at the end
# since each print statement
# forces a new line
output = ''
while i < maxValue:
  if B[i] != -1:
    output = output + str(B[i])
  i = i + 1
print(output)