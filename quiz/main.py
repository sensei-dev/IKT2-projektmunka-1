print("Üdvözöllek a kvízek kvízében! ")
print("------------------------------")
print("Kérlek válaszd ki melyik témából szeretnél kérdéseket kapni!")
print("------------------------------")


print("Állati kérdések: X  // Tudományos kérdések: Y // Programozói kérdések : Z //")
print("------------------------------")
valasz = input("Kérlek írd be melyik kvízzel szeretnél játszani.")
print("------------------------------")

if valasz == "X" or valasz == "x" : 
    import allati
if valasz == "Y" or valasz == "y" :
    import tudomany
if valasz == "Z" or valasz == "z":
    import programozoi

