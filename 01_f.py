#Psaní vlastních funkcí
#jak to funguje? Funkce se definuje příkazem def,
#za nějž napíšeš jméno funkce, pak do závorky
#seznam argumentů, které funkce bere,
#a pak dvojtečku
#potom následuje odsazené tělo funkce - příkazy,
#které funkce provádí. Tělo může začít
#dokumentačním řetězcem, který posiluje
#co funkce dělá
#příkazem return pak můžeš z funkce vrátit
#nějakou hodnotu

def obvod_obdelnika(sirka, vyska):
    #vrátí obvod obdélníku daných rozměrů
    return 2* (sirka + vyska)