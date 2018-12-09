produkt = ['mleko', 'chleb', 'jajka']
cena = [1, 5, 8]
suma = 0

for indeks in range (len(produkt)):

    print(produkt[indeks] + " cena" + " " +str(cena[indeks]) + " zl")

for c in cena:
    suma = suma + c
    print suma

if suma >=16:
    print ("Promocja 10%!")
    suma = suma - (suma *10) /100

elif suma >= 13:
    print ("Promocja 5%")
    suma = suma - (suma *5) /100
else:
    print ("Bez Promocji!")

print("Do zaplacenia" + " " + str(suma))
