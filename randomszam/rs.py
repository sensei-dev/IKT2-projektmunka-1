import random

a = random.randint(1,10)
#1 - 10 közötti számok lehetnek csak 
print("Gondoltam egy számot, 1 és 10 között")
szam = int(input("Szerinted melyik számra gondoltam?"))
while (szam!=a):
    szam=int(input("Szerinted melyik számra gondoltam?"))
print("A keresett szám:", szam)