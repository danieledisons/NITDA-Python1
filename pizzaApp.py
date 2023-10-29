def orderPizza():
    print("Welcome to Pizza Palour")

    S = 15
    M = 20
    L = 25

    pepperoniforSmallPizza = 2
    pepperoniforMediumOrLargePizza = 3
    
    extraCheese = 1

    pizza_size = input("Reply with S / M / L \nWhat size of pizza will you like to order? \nWe have Small Pizza(S) = $15, Medium(M) = $20, Large(L) = $25 ").upper()

    print(pizza_size)

    pepperoni = input("Reply with Y / N \nDo you want pepperoni with your pizza?  ").upper()
    print(pepperoni)

    cheese = input("Reply with Y / N \nDo you want cheese with your pizza?  ").upper()
    print(cheese)

    if (pizza_size == "S" and pepperoni == "N" and cheese == "N"):
        result = 15
        print("The total price is: ", result)
        return result
    elif (pizza_size == "S" and pepperoni == "N" and cheese == "Y"):
        result = 15+1
        print("The total price is: ", result)
        return result
    elif (pizza_size == "S" and pepperoni == "Y" and cheese == "Y"):
        result = 15+2+1
        print("The total price is: ", result)
        return result
    elif (pizza_size == "L" and pepperoni == "Y" and cheese == "N"):
        result = 15+3
        print("The total price is: ", result)
        return result
    elif (pizza_size == "M" and pepperoni == "N" and cheese == "N"):
        result = 20
        print("The total price is: ", result)
        return result
    elif (pizza_size == "M" and pepperoni == "N" and cheese == "Y"):
        result = 20+1
        print("The total price is: ", result)
        return result
    elif (pizza_size == "M" and pepperoni == "Y" and cheese == "Y"):
        result = 20+3+1
        print("The total price is: ", result)
        return result
    elif (pizza_size == "M" and pepperoni == "Y" and cheese == "N"):
        result = 20+3
        print("The total price is: ", result)
        return result
    elif (pizza_size == "L" and pepperoni == "N" and cheese == "N"):
        result = 25
        print("The total price is: ", result)
        return result
    elif (pizza_size == "L" and pepperoni == "N" and cheese == "Y"):
        result = 25+1
        print("The total price is: ", result)
        return result
    elif (pizza_size == "L" and pepperoni == "Y" and cheese == "Y"):
        result = 25+3+1
        print("The total price is: ", result)
        return result
    elif (pizza_size == "L" and pepperoni == "Y" and cheese == "N"):
        result = 25+3
        print("The total price is: ", result)
        return result
        

orderPizza()



