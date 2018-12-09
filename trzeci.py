produkt = 'mleko'
suma = 150

if 100 < suma and suma<200:
    print ("Promocja 30%!")
    suma = suma - (suma *30) /100
elif suma >= 200:
    print ("Promocja 35%")
    suma = suma - (suma *35) /100
else:
    print ("Bez Promocji!")

print("Do zaplacenia" + str(suma))
