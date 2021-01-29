guest_list=['Anna', 'Ben', 'Cynthia','Diana','Elon']
guest_list.append('Fiona')
guest_list.insert(2,'Gene')
pop_guest = guest_list.pop(4)
for x in range(len(guest_list)):
    print("Hello " + guest_list[x] + ", I want you to join my party at 8p.m today")
print("Sorry that you can not come " + pop_guest)