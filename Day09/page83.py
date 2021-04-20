def firstFunc():
    age = 15
    if age <10:
        price = 0
    elif age > 65:
        price = 5
    else:
        price = 10
    print("Your admission cost is $" + str(price) + ".")

def secondFunc():
#Do not use elif/else because I want to check all the value.
    requested_toppings = ['mushrooms', 'extra cheese']
    if 'mushrooms' in requested_toppings:
        print("Adding mushrooms.")
    if 'pepperoni' in requested_toppings:
        print("Adding pepperoni.")
    if 'extra cheese' in requested_toppings:
        print("Adding extra cheese.")
    print("\nFinished making your pizza!")
secondFunc()
#firstFunc()
#In summary, if you want only one block of code to run, use an if-elifelse chain. If more than one block of code needs to run, use a series ofindependent if statements.    