"""
x = int(input("Nhap so can tinh giai thua:"))
def fact(x):
    if x==0:
        return 1
    return x * fact(x-1)
print (fact(x))
n = int(input("Nhap n:"))
dictionary = {}
for i in range(1,n+1):
    dictionary[i] = i*i    
print(dictionary)

"""

def fibonancy(k):
    if k==0:
        return 0
    if k==1:
        return 1
    return fibonancy(k-1) + fibonancy(k-2)

def printfibonancy(k):
    for i in range(k+1):
        print(fibonancy(i))
printfibonancy(15)        