weight = eval(input())
targetWeight = eval(input())

months = 0

while weight > targetWeight:
  weight = weight - 5/100.0 * weight
  months = months + 1

print("The number of months the diet will last: ", months)
