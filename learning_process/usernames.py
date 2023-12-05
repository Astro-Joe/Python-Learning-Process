current_users = ['Joseph', 'John','Samuel', 'Tayo', 'Dayo'] 

flag = True

while flag:
    usr_name = input("Enter a username: ")
    
    if usr_name.title() not in current_users:
        print('Username available!')
        current_users.append(usr_name.title())
        flag = False
        
    else:
        print('Username UNAVAILABLE!\n')
 

print(current_users)

