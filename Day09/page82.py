buffet = ('banh bao xa xiu', 'dimsum','bingsu','banh troi nuoc','flan cot dua')
request = 'bingsu'
print ("New request " + request.upper())
if request in buffet:
    print ("\nThank you, wait a minute")
else:
    print ("\nSorry, we don't have " + request + " for today")
        