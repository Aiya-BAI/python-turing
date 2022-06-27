unconfirmed_users = ['alice', 'brian', 'candace']
confirm_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f'verifying user: {current_user.title()}')
    confirm_users.append(current_user)

print(unconfirmed_users)
print(confirm_users)

pets = ['dog', 'cat', 'rabbit', 'dog', 'dog', 'cat', 'dog', 'catg', 'tiger', 'tiger']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)











