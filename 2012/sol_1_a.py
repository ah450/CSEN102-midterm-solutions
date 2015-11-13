age = eval(input())
gender = input()

if gender == 'male':
  maxHeartRate = 220 - age
else:
  maxHeartRate = 226 - age

healthZoneFrom = 50 * maxHeartRate / 100
healthZoneTo = 60 * maxHeartRate / 100
fatBurningZoneTo = 70 * maxHeartRate / 100
aerobicZoneTo = 80 * maxHeartRate / 100
anaerobicZoneTo = 90 * maxHeartRate / 100

print("Health Zone: Between ", healthZoneFrom, " and ", healthZoneTo)
print("Fat-burning zone: to " , fatBurningZoneTo)
print("Aerobic zone: to " , aerobicZoneTo)
print("Anaerobic zone: to " , anaerobicZoneTo)
print("Maximum heart rate / Red zone: to ", maxHeartRate)
