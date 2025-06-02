# příkazy if se dají zanořovat. V odsazeneém kousky může



stastna = input("Jsi šťastná?")
bohata = input("Jsi bohatá?")

if stastna == "ano":
 # Tenhle kus kodu se probede, když je "šťastná"
    if bohata == "ano":
        print("Gratuluji!")
    else:
        print("Zkus míň utrácet")
else:
# Tenhle kus kodu se provede, když není "Šťastná"
    if bohata == "ano":
        print("Zkus se víc usmívat!")
    else:
        print("To je mi líto")