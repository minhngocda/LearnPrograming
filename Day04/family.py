family = ['husband', 'wife', 'kids']
# to print list family
print(family)
# to print first element in the list
print(family[0])
# to print second element with title menthod
print(family[1].title())
# to print -3 element with upper menthod, it is the third when return from the first item  
print(family[-3].upper())
#to print message from family
message= "I love my " + family[1].title() + "."
#to replace item number 2 with another one and add 1 more item to the end of the list
family[2] = 'Fiona'
family.append('Ducky')
print(family)
#to insert new item on 3rd place of the list
family.insert(3,'Katty')
print(family)
#to delete item number 3
del family[3]
print(family)

popped_family = family.pop()
print(family)
print("The last person in our family is " + popped_family)
