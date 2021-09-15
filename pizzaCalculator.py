#Ashanthe Gunawardena, Pizza calculator

print("Welkom bij Pizzeria San Fransisco")
print("Pizza Medium €9.99 \ Pizza Small €6.99 \ Pizza Large €11.99")

pizzas =["Pizza Medium", "Pizza Small", "Pizza Large"] 
prijs = [9.99, 6.99, 11.99]

#Pizza prijs en soort
print("---------------------------------------------")

myorderFood=[]
myorderCost=[]

order = input("Wilt u bestellen?    ")
if order == "Nee":
    exit ()
else:
    print ("Dank u wel")  
print(" ")
print(" ")

nextorder = True
while nextorder==True:
    food0rder = input("Kies uw Pizza    ")
    if food0rder == "Pizza Medium":
        myorderFood.append(pizzas[0])
        myorderCost.append(prijs[0])

    elif food0rder=="Pizza Small":
        myorderFood.append(pizzas[1])
        myorderCost.append(prijs[1])
        
    elif food0rder == "Pizza Large":
        myorderFood.append(pizzas[2])
        myorderCost.append(prijs[2])

    else:
        print ("niet op de kaart")
    finished = input("Bent u klaar met uw bestelling J?N    ")
    if finished =="N":
        nextorder = True
    else:
        nextorder = False
    print (myorderFood)
    print (myorderCost)
print("")
print("-------------------------------------------------")







