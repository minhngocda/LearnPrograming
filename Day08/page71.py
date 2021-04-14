buffet = ('banh bao xa xiu', 'dimsum','bingsu','banh troi nuoc','flan cot dua')

print("Thuc don hom nay gom co:")

for a in buffet:
    print(a)
update_menu = list(buffet)
update_menu[0]= 'sushi'
update_menu[1]= 'pizza'
buffet = tuple(update_menu)

print("\nThuc don da thay doi:")
for a in buffet:
    print(a)