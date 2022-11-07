import time

print("Üdvözöllek a  tudományos  kérdéseknél! ")
print("------------------------------")
start = input("Megkezdhetjük a játékot? Y = igen, X = nem [visszalép a főmenübe]")

if start == "y" or start == "Y" : 
    print("A játék megkezdődött...")
    time.sleep(3)
else: 
    import main

    k1 = input("Albert Einstein 1979. március 14-én született? ")
if k1 == "NEM" or k1 == "nem" : 
    print("A válaszod helyes, hisz 1879. március 14-én született ")
else: 
    print("A válaszod helytelen, hisz 1879. március 14-én született")

print("Következő kérdés...")
time.sleep(2)
k2 = input("Nikola Tesla  1856. július 10-én született?  ")
if k2 == "nem" or k2 == "nem":
    print("A válaszod helyes! Hisz ekkor halt meg ")
else: 
    print("A válaszod helytelen! Hisz ekkor halt meg!" )


    print("Következő kérdés...")
time.sleep(2)
k3 = input("Csökkenő sorrendbe a Föld után a Jupiter következik? ")

if k3 == "nem" or k3 == "NEM" : 
    print("A válaszod helyes! ")
else: 
    print("A válaszod helytelen!")

    print("Következő kérdés...")
time.sleep(2)
k4 = input("A neptunusnak 1231 holdja van?")
if k4 == "nem" or k4 == "NEM": 
    print("A válaszod helyes! mert csak 14  ")
else: 
    print("A válaszod helytelen!")

print("Következő kérdés...")
time.sleep(2)
k5 = input("A Jupiter gázbolygó? ")
if k5 == "nem" or k5 == "NEM" : 
    print("A válaszod helytelen,  ")
else: 
    print("A válaszod helyes! , ")
print("Köszönjük a játékot")
time.sleep(2)
print("Játék leaállítása és visszadobás a főmenübe... ")
time.sleep(4)
import main