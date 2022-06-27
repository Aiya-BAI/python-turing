cars = []
if cars:
    for car in cars:
        print(car)
else:
    print("null")

availables = ['1', '2', '4','5', '6']
requests = ['2', '3', '4']
for request in requests:
    if request in availables:
        print(f'add {request}')
    else:
        print(f'sorry no {request}')


#检查用户名
current_users = ["a", "B", "c", "d", "e"]
new_users = ["b", "e", "f", "g", "h"]

# current_users_lower = []
# for current_user in current_users:
#     current_users_lower.append(current_user.lower())
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f'{new_user} 已经被占用')
    else:
        print(f'{new_user} 未被占用')





