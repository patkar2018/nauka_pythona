koszyk = [
           {'name' : 'mleko', 'cena' : 10.0},
           {'name' : 'chleb', 'cena' : 5.0},
           {'name' : 'jajka', 'cena' : 8.0}
           ]


print(koszyk[0]['name'], koszyk[0]['cena'])
print(koszyk[1]['name'], koszyk[1]['cena'])
print(koszyk[2]['name'], koszyk[2]['cena'])

suma = 0

for poz in koszyk:
     suma = suma + poz['cena']

print(suma)

if suma >=21:
    print ("Promocja 10%!")
    suma = suma - (suma *10) /100

elif suma >= 19 and suma <21:
    print ("Promocja 5%")
    suma = suma - (suma *5) /100
else:
    print ("Bez Promocji!")

print("Do zaplacenia" + " " + str(suma))

#########sprawdza czy mleko i ser wystepuja###################################################
bylo_mleko = False
byl_ser = False

suma = 0

for poz in koszyk:
     suma = suma + poz['cena']
     nazwa_prod = poz['name']
     if nazwa_prod == 'mleko':
         bylo_mleko = True
     if nazwa_prod == 'ser':
         byl_ser = True

if bylo_mleko and byl_ser:
        suma = suma - (suma *10) /100
print (suma)
