marka = 'Peugeot'
ilosc_drzwi = 5
pojemnosc = 1.3
##marka_l = marka.lower()
marka_c = marka.capitalize()
marka_s = marka.swapcase()


print ("Samochod " + marka +" " + "ma" + " " + str(ilosc_drzwi) + " " + "drzwi")
print(marka_c)
print ("Pojemnosc po zmianach: " + str(pojemnosc * 2))
print(marka_s)


if ilosc_drzwi > 3:
    print ("Duzy samochod")
else:
    print ("Maly")

if marka == 'Peugeot':
    print ("Francuski samochod")
else:
    print ("Inny")

if marka.startswith("Pe"):
    print ("Peugeot")
else:
    print("Inny")

if marka.endswith("t"):
    print ("Peugeot")
else:
    print("Inny")
