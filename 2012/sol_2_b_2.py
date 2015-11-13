weight = eval(input())
currentDay = eval(input())
currentMonth = eval(input())
currentYear = eval(input())
weddingDay = eval(input())
weddingMonth = eval(input())
weddingYear = eval(input())

yearsDifference = weddingYear - currentYear
monthDifference = weddingMonth - currentMonth
daysDifference = weddingDay - currentDay
totalDaysDifference = yearsDifference * 12 * 30 + monthDifference * 30 + daysDifference
months = totalDaysDifference / 30
while months > 0:
  weight = weight - 5.0 /100 * weight
  months = months - 1

print("The number of days left to the wedding: " , totalDaysDifference)
print("The weight of the lady during her wedding day: " , weight)