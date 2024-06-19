#Temperaturumrechner und Glatteiswarner
print()
print("Temperaturüberwachung")
f = float(input("Fahrenheit:"))
c = (f - 32) * 5 / 9
if c <= 4:
    print("Achtung Glatteis!")
else:
    print("Gute Fahrt!")
print("Außentemperatur= ", round(c, 2), "°C", sep="")
