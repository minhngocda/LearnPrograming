age = input("How old are you?")

age=int(age)
if age < 0:
    print("Not valid")
    exit()    
age = str(age)
if age[-1] == "1" and age != "11" and age != "111" :
    print("Happy " + age + "st Birthday!")
elif age[-1] == "2" and age!= "12":
    print("Happy " + age + "nd Birthday!")     
elif age[-1] == "3":
    print("Happy " + age + "rd Birthday!")   
else:
    print("Happy " + age + "th Birthday!")     