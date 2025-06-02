from math import pi

a=float(input("Zadej délku poloosy 1:"))
b=float(input("Zadej délku poloosy 2:"))

def obsah_elipsy(a,b):
    return pi*a*b

print("obsah je", obsah_elipsy(a,b))