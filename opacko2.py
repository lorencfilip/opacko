cisla = [3, 5, 8, 1, 2, 4, 6, 7,]
kokos = []

while True:
    for x in range(len(cisla)):
        print(f"cisla {x+1}: {cisla[x]}")

    def vypis_pole(prvek):
        for x in range(len(prvek)):
            print(f"cislo {x+1}: {cisla[x]}")

    prvek_minus = input("jake cislo chcete odebrat ? ")
    cisla.pop(prvek_minus)
    vypis_pole(cisla)

    kokos.append(prvek_minus)

    print("stav kokosu:")
    print(kokos)

    print("co dalsiho chcete odebrat")