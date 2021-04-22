requested_toppings = ['mushrooms', 'extra cheese', 'chilli', 'pepper']
out_of_stock = ['chilli', 'extra cheese']
if requested_toppings: #to check if the requested_toppings is empty list
    for topping in requested_toppings:
            if topping in out_of_stock: 
                print("Sorry, we are out of " + topping +" right now.")
            else:
                print("Adding " + topping + ".")
    print ("\nFinish making your pizza.") 
else:
    print("Are you sure you want a plain pizza?")