age = input("How old are you?")  
age = str(age)
if age[-1] == "1":
    print("Happy " + age + "st Birthday!")
if age[-1] == "2":
    print("Happy " + age + "nd Birthday!")     
if age[-1] == "3":
    print("Happy " + age + "rd Birthday!")   
else:
    print("Happy " + age + "th Birthday!")     