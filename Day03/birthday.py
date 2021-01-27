age = int(input("How old are you?"))

if age < 0 or age > 130:
    print("your age is not available")
elif age == 1 or age == 21 or age == 31 or age == 41 or age == 51 or age == 61 or age == 71 or age == 81 or age == 91 or age == 101 or age == 121:
    print("Happy " + str(age) + "st Birthday!")
elif age == 2 or age == 22 or age == 32 or age==42 or age==52 or age==62 or age ==72 or age==82 or age==92 or age==102 or age==122:
    print("Happy " + str(age) + "nd Birthday!")
elif age == 3 or age == 23 or age == 33 or age==43 or age==53 or age==63 or age ==73 or age==83 or age==93 or age==103 or age==123:
    print("Happy " + str(age) + "rd Birthday!")
else: print("Happy " + str(age) + "th Birthday!")