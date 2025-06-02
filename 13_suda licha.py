import random

def kostka():
    n = random.randint(1, 6)
    return n

for i in range(10):
    print("Na KOSTCE PADLA", kostka()*1)
