from math import pi
obsah=0
a=30

def obsah_elipsy(a,b):
    obsah=pi*a*b
    a=a+3
    return obsah

print(obsah_elipsy(a,20))
print(obsah)
print(a)

#pi je globalni
#obsah je lokalni
#a je lokalni i globalni
#b je lokalni