age = eval(input())
gender = input()
heartRate = eval(input())
if gender == 'male':
  maxHeartRate = 220 - age
if gender != 'male':
  maxHeartRate = 226 - age

healthZoneFrom = 50 * maxHeartRate / 100
healthZoneTo = 60 * maxHeartRate / 100
fatBurningZoneTo = 70 * maxHeartRate / 100
aerobicZoneTo = 80 * maxHeartRate / 100
anaerobicZoneTo = 90 * maxHeartRate / 100

# Note that because the restriction of not being able to use else statements
# our if conditions must be exclusive in order to prevent the triggering of
# more than one
if(healthZoneFrom <= heartRate <= healthZoneTo):
  print("Health Zone")

if(healthZoneTo <  heartRate <= fatBurningZoneTo):
  print("Fat-burning zone"

if(fatBurningZoneTo < heartRate <= aerobicZoneTo):
  print("Aerobic zone")

if(heartRate > aerobicZoneTo and heartRate <= anaerobicZoneTo):
  print("Anaerobic zone")

if(heartRate > anaerobicZoneTo):
  print("Red zone")