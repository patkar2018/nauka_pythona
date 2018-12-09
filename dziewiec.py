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
stan_reguly = {'mleko' : False,
                'ser': False}
suma = 0

for poz in koszyk:
     suma = suma + poz['cena']
     nazwa_prod = poz['nazwa']
     if nazwa_prod == 'mleko' or nazwa_prod == 'ser':
         stan_reguly[nazwa_prod] = True

if stan_reguly['mleko']:
    print ("Znizka")
    suma = suma - (suma *10) /100
print (suma)
