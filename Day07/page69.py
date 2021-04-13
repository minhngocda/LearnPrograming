def firstFunc():
    players = [ 'Nam', 'Ngoc', 'Min', 'Hien', 'Hung', 'Van']
    print(players[:3])
    print(players[2:])
    print(players[-3:])
def secondFunc():
    mypizza = ['nem', 'bun bo', 'cha la lot', 'pho']
    Nampizza = ['beef', 'pizza', 'chips','nuts']
    print(mypizza)
    mypizza.append('nem chua ran')
    print(Nampizza)
    Nampizza.append('chicken')
    print("My favorite Vietnamese food are:")
    for pizza in mypizza:
        print(pizza)
    for food in Nampizza:
        print("Nam loves " + food)
secondFunc()