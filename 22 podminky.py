from xml.sax.handler import property_interning_dict

hmotnost=int(input("Zadejte hmotnost"))
vyska=int(input("Zadejte výšku"))

x=(hmotnost/ vyska/100**2 )
if x < 18.5:
    print("podvaha")
elif 18.5 <= x < 24.9:
    print("Normalni vaha")
elif 25<=x<30:
    print("Nadvaha")
else:
    print("obezita")
print(x)