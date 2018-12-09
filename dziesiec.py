produkty = {'S1222': 'sukienka trojkat',
            'P1222' : 'spodnie krata',
            'x212' : 'konsola do gier'}

##igla = 'x212'
spodnie = 'P1222'

if spodnie in produkty:
    print("Znalazlem{0}".format(spodnie))
else:
    print("Brak w magazynie {0}".format(spodnie))
