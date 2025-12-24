T = int(input("whats the temptemperature T : "))
if T <= 0:
    print("freezing temperature")
elif  0< T < 100:
    print("liquid temperature")
else:
    print("boiling temperature")