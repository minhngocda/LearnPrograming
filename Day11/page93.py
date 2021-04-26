"""users_name = []
if users_name:    
    for user in users_name :
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + user + ", thank you for logging in again!")
else:
    print("We need to find some users!")"""


current_users = ['admin','Sam','Mon','Tue','Thu']
current_users_1 = []
for i in current_users:
    current_users_1.append(i.lower())
    
#print(current_users_1)    
new_users = ['Fri','Sat','Sun','MON']
for us in new_users:
    if us.lower() in current_users_1:
        print(us + " has already been used, please choose new username.")
    else:
        print("Your username is available")