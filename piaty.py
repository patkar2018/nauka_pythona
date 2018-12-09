zwierzeta = ['psy', 'koty', 'krowy', 'konie']

print(zwierzeta[0])
print(zwierzeta[1])
print(zwierzeta[2])
print(zwierzeta[3])

for z in zwierzeta:
    print(z)

for idx in range (len (zwierzeta) ):
    print ("idx: " + str(idx) + " : " + zwierzeta[idx])
