#input

aantal_mensen = input("hoveel mensen    :")
toegangsticket = 7.45
vip = 0.37
aantal_min = input("hoveel minuten x5   :")
sum1 = int(aantal_min) * 5

#som
print(int(aantal_mensen) * toegangsticket + int(aantal_mensen) * (vip * int(aantal_min)))
prijs = int(aantal_mensen) * toegangsticket + int(aantal_mensen) * (vip * int(aantal_min))


factuur = "Dagje uit met " +str(aantal_mensen) + " mensen in de speelhal met " + str(sum1) + " minuten VR kost " 
print (factuur)


