import random

def pin():
    x=random.randint(1,9)
    return x


for i in range(4):
    print(pin(), end=" ")