# Tc=(5/9)*(Tf-32)
#  Tf=(9/5)*Tc+32

#  Temperature converter
#
# Enter a temperature: 20
# Convert to (F)ahrenheit or (C)elsius? F
#
# 20 C = 68 F

temperature = int(input("Enter a temperature: "))
convertTo = input("Convert to: (F)ahrenheit or (C)elsium? ")

if convertTo is "F":
    convertedTemperature = (9/5) * (temperature-32)
    print("{} C = {} F".format(temperature,convertedTemperature))
elif convertTo is "C":
    convertedTemperature = (5/9) * (temperature-32)
    print("{} F = {} C".format(temperature, convertedTemperature))
else:
    print("Wrong input.")
