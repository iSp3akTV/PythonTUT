# Variabelele (i start to learn Python)


# Strings -----
nume = "Jantovan"
prenume = "Daniel"
Nume_complet = nume  +" "+ prenume

print("Salut "+Nume_complet)
# print(type(nume)) 


# ints  
age = 15
# print(type(age))
print("Tu ai: "+ str(age))
age += 1
print("Peste 4 luni vei avea: " + str(age))


# Floats
inaltime = 173.5
adidasi_inaltime = 1.5
# print(type(inaltime))
print("Inaltime ta este: "+ str(inaltime) + "cm")
print("adidasii tai au inaltimea de: " + str(adidasi_inaltime) + "cm" )
inaltime = inaltime + adidasi_inaltime
print("Inaltimea ta in adidasii este:" + str(inaltime)+"cm")


# Booleans
scolar = True
# print(type(scolar))
print("Esti elev la gimnaziu: " + str(scolar)) 
scolar = False
print("Peste un an, tot elev la gimnaziu ve fi: "+ str(scolar))