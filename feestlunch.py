croissantjes = input("hoeveel croissants    :")
prijsC = 0.39
stokbrood = input("hoveel stokbroden    :")
prijsS = 2.78
kortingsbonnen = input("hoveel kortngsbonnen    :") 
korting = 0.50

#Prijs

print(int(croissantjes) * prijsC + int(stokbrood) * prijsS - int(kortingsbonnen) * korting)
prijs = (int(croissantjes) * prijsC + int(stokbrood) * prijsS - int(kortingsbonnen) * korting)

#Factuur
print("De feestlunch kost " + str(prijs) + " euro voor de " + str(croissantjes) + " croissantjes en de " + str(stokbrood) + " stokbroden als de " + str(kortingsbonnen) + " kortingsbonnen nog geldig zijn! ")


