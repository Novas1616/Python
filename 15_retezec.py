text=input("Zadejte text:")

for i in range(1, len(text) +1):
    print(text[:i])

for i in range(len(text)-1,0,-1):
    print(text[:i])


