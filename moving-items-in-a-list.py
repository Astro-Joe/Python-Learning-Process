unconfirmed_users = ['daniel', 'esther', 'tolu', 'dayo']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print('Verifying: ' + current_user.title())
    confirmed_users.append(current_user)
print('The following users have been confirmed: ')
for confirmed_user in confirmed_users:
    print(confirmed_user.title())