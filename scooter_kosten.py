
def bereken_maandkosten(km_per_maand):

    getal1 = verzekering_per_maand = 23
    getal2 =benzine_kosten_per_liter = 1.54
    getal3 =liter_per_kilometer = 0.2
    maandkosten = (km_per_maand * liter_per_kilometer * benzine_kosten_per_liter) + verzekering_per_maand
    print(maandkosten)
invoer = "";
while not isinstance(invoer, float):
    try:
            invoer = input("Voer een getal in: ")
            invoer = float(invoer)
            print("Ja, de invoer " + str(invoer) + " is een getal, want ik kan het omzetten naar een float")
    except ValueError:
                 print(invoer + " is geen geldig getal!")

bereken_maandkosten(int(invoer))
