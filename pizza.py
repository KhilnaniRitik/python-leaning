print("Hey welcome to Pizzaria #6, don't ask what happened to the others...\nWe do free pizzas with unlimited toppings.") 

print("The toppings we have include: \nPepperoni,\nItalian Sausage,\nMushrooms,\nBell peppers,\nOlives and,\nOnions")

A = True
while A == True:
    toppcount = int(input("Anyway, how many do you want? "))
    if toppcount <= 3:
        print("Ok, we can do that on 1 pizza.")
        #pizza = input("Which toppings would you like?")
        A = False
    elif toppcount <= 6:
        print("Ok, we can do that on 2 pizzas.")
        A = False
    else:
        print("Sorry, the maximum we can do is 6 toppings. Please try again")
        A = True


print("We can do that on", toppcount/3 "pizzas")