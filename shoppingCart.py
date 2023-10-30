def shoppingCart():
    cart = []
    prices = []
    totalprice=0

    def addItem():
        order_item = input("\nWhat item do you want ?  ").upper()
        order_price = int(input("\nHow much is the item  "))
        prices.append(order_price)
        cart.append(order_item)
        print(f'\n{order_item}(${order_price}) has been added to the cart\n')
    
    def totalCost():
        totalprice = sum(prices)
        print(f'The total price is == {totalprice}')
        if (totalprice > 50 ):
            discount = 0.1
            discountedPrice = totalprice - totalprice*discount
            print(f'The total price with discount is {discountedPrice}')
        elif (totalprice > 100):
            discount = 0.25
            discountedPrice = totalprice - totalprice*discount
            print(f'The total price with discount is {discountedPrice}')
    

    # def applyDiscount():
    #     if (totalprice > 50 ):
    #         discount = 0.1
    #         discountedPrice = totalprice - totalprice*discount
    #         print(f'The total price with discount is {discountedPrice}')
    #     elif (totalprice > 100):
    #         discount = 0.25
    #         discountedPrice = totalprice - totalprice*discount
    #         print(f'The total price with discount is {discountedPrice}')

    while True:
        print("\nWelcome to the supermarket")
        print("\nPlease enter what items you want and the price")
        addItem()

        print(f"\nThe cart currently contains {cart} \n")
        print(f"\nThe prices currently contains {prices} of {type(prices)} \n")

        totalCost()

        # applyDiscount()

        finish_ordering = input(" Type OK if you are done ordering \n Type No if you arent done ordering  ")
        if finish_ordering == "OK" or finish_ordering == "Ok" or finish_ordering == "ok":
            break
            
    


shoppingCart()

