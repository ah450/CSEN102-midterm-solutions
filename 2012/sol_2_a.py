calories = eval(input())

# The '.0' is to force floating point division
# ie 10/3 is 3 10/3.0 or 10.0/3 is 3.3333~
# another method is to have had calories = float(input())
# instead of calories = eval(input())

dancingMins = calories / 250.0 * 52
yogaMins = calories / 250.0 * 90
ridingMins = calories / 250.0 * 30
rollerMins = calories / 250.0 * 18
phoneMins = calories / 250.0 * 120
horseMins = calories / 250.0 * 57

print("Dancing: ", dancingMins, " minutes")
print("Doing yoga: ", yogoMins, " minutes")
print("Riding a bike: ", ridingMins, " minutes")
print("Rollerblading: ", rollerMins, " minutes")
print("Standing while talking on the phone: " , phoneMins, " minutes")
print("Horseback riding: ", horseMins, " minutes")