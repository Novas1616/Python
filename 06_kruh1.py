#Vytvoř program, který si na vstupu važádá poloměr kruhu.
#Následně vypíše jeho obvod a obsah. Obvod se vypočítá jako 2*pi*r, obsah pi*r*r
pi = 3.14
poloměr = float(input("Zadej poloměr kruhu v cm: "))
print("Obvod kruhu s poloměrem", poloměr, "je", 2*pi*poloměr, "cm")
print("Obsah kruhu s poloměrem", poloměr, "je", pi*poloměr**2,"cm2")