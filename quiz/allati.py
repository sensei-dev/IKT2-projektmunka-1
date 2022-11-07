import time

print("Üdvözöllek az állati kérdéseknél!")
print("------------------------------")
start = input("Megkezdhetjük a játékot? Y = igen, X = nem [visszalép a főmenübe]")

if start == "y" or start == "Y" : 
    print("A játék megkezdődött...")
    time.sleep(3)
else: 
    import main
    
k1 = input("A macska emlős állat - e? ")
if k1 == "Igen" or k1 == "igen" : 
    print("A válaszod helyes!, a macksa emlős állat ")
else: 
    print("Helytelen, a macska az emlős állat!")

print("Következő kérdés...")
time.sleep(2)
k2 = input("A madarak emlősök?")
if k2 == "Nem" or k2 == "nem":
    print("A válaszod helyes! A madarak meszes héjú tojással szaporodnak ")
else: 
    print("A válaszod helytelen!  A madarak meszes héjú tojással szaporodnak ")


    print("Következő kérdés...")
time.sleep(2)
k3 = input("A bagolyfélék éjszakai állatok?")

if k3 == "igen" or k3 == "IGEN" : 
    print("A válaszod helyes! :) ")
else: 
    print("A válaszod helytelen!")
print("Következő kérdés...")
time.sleep(2)
k4 = input("A macskának 8 lába van? ")
if k4 == "Igen" or k4 == "Nem": 
    print("A válaszod helyes!")
else: 
    print("A válaszod helytelen! ")

print("Következő kérdés...")
time.sleep(2)
k5 = input("A kutya az meszes héjú tojással szaporodik? ")
if k5 == "nem" or k5 == "NEM" : 
    print("A válaszod helyes! ")
else: 
    print("A válaszod helytelen, mert a kutyák emlősök")
print("Köszönjük a játékot")
time.sleep(2)
print("Játék leaállítása és visszadobás a főmenübe... ")
time.sleep(4)
import main