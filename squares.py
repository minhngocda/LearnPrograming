for x  in range(1,21):
    print(x)
oddnumber=list(range(1,20,2))
print(oddnumber)

y = [value*3 for value in range(1,11)]
print(y)

z = [number**3 for number in range(1,11)]
print(z)
    
money = list(range(1,1000001))
#print(money)
print(min(money))
print(max(money))
print(sum(money))