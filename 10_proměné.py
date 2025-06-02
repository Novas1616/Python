#Vytvoř tři proměnné: jméno, věk a město.
#Proměnná jméno bude obsahovat tvojejuméno řetězec
#věk bude obsahovat tvůj věk (číslo) a město bude obsahovat tvoje město, kde žijeě ( řetězec
#Poté spočítej kolik ti bude za pět let.
#Nakonec vypiš větu ve formátu:Jmenuji se .....,je mi ... let a bydlím ve městě .... Za 58 let mi bude tolik.

print("Představení osoby")

jmeno = input("zadejte jméno:")
vek = int(input("zadejte věk:"))
bydliste = input("zadejte Město:")
vek_za_5_let = vek + 5

print("Jmenuji se:", jmeno + ",", "je mi", vek, "let a bydlim ve meste", bydliste, ".", "za 5 let mi bude", vek_za_5_let, "let.")
