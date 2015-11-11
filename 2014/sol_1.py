firstYear = eval(input())
secondYear = eval(input())
oldPrice = eval(input())
newPrice = eval(input())

CPI = newPrice - oldPrice
CPI = CPI / oldPrice
CPI = CPI * 100
print("The price of the item in year", firstYear, "is", oldPrice)
print("The price of the item in year", secondYear, "is", newPrice)
print("The CPI is", CPI, "%")