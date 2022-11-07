import time

print("Üdvözöllek a programozói kérdéseknél! ")
print("------------------------------")
start = input("Megkezdhetjük a játékot? Y = igen, X = nem [visszalép a főmenübe]")

if start == "y" or start == "Y" : 
    print("A játék megkezdődött...")
    time.sleep(3)
else: 
    import main

    k1 = input("A HTML az programozási nyelv? ")
if k1 == "NEM" or k1 == "nem" : 
    print("A válaszod helyes, hisz a HTML az egy leíró nyelv és nem programnyelv!")
else: 
    print("A válaszod helytelen, hisz a HTML az egy leíró nyelv és nem programnyelv!")

print("Következő kérdés...")
time.sleep(2)
k2 = input("A css a ControlCascadSheets röviditése? ")
if k2 == "nem" or k2 == "nem":
    print("A válaszod helyes! CSS = Cascading Style Sheets ")
else: 
    print("A válaszod helytelen! CSS = Cascading Style Sheets")


    print("Következő kérdés...")
time.sleep(2)
k3 = input("A Python egy leíró nyelv?")

if k3 == "nem" or k3 == "NEM" : 
    print("A válaszod helyes! hisz a Python egy nagyon magas szintű programozási nyelv :) ")
else: 
    print("A válaszod helytelen! hisz a Python egy nagyon magas szintű programozási nyelv :)")
print("Következő kérdés...")
time.sleep(2)
k4 = input("A CSS egy programnyelv? ")
if k4 == "nem" or k4 == "NEM": 
    print("A válaszod helyes! hiszen a CSS egy stílusleíró nyelv :) ")
else: 
    print("A válaszod helytelen! hiszen a CSS egy stílusleíró nyelv :)  ")

print("Következő kérdés...")
time.sleep(2)
k5 = input("A JavaScripttel tudok weboldalt formázni? ")
if k5 == "nem" or k5 == "NEM" : 
    print("A válaszod helytelen, hisz tudok! ")
else: 
    print("A válaszod helyes! , ")
print("Köszönjük a játékot")
time.sleep(2)
print("Játék leaállítása és visszadobás a főmenübe... ")
time.sleep(4)
import main