# alien_0 = {"color": 'green', 'points': 5}
# alien_1 = {"color": 'yellow', 'points': 10}
# alien_2 = {"color": 'red', 'points': 15}
#
# aliens = [alien_0, alien_1, alien_2]
# print(aliens)
# for alien in aliens:
#     print(alien)

#外星人例子
aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)
print(f'创建了{len(aliens)}个外星人')


print()
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = "yellow"
        alien['points'] = 10
        alien['speed'] = 'medium'
for alien in aliens[:5]:
    print(alien)
print('....')

#pizza
pizza = {
    'crust': 'thick',                             #外壳：厚
    'toppings': ['mushrooms', 'extra cheese']     #配料：蘑菇，额外奶酪
}

print(f'you order a {pizza.get("crust")}-crust pizaa'
      'with the following toppings')
for topping in pizza['toppings']:                 #调用字典里value为列表是的方法
    print('\t' + topping)


#多个值关联一个键
favorite_languages = {
    'jen': ['python', 'java'],
    'sarch': 'c',
    'edward': 'java',
    'phil': 'python',
}
for name, languages in favorite_languages.items():
    print(f'{name.title()} like de is :')
    for language in languages:
        print(f'{language.title()}')       #非全列表循环字符串字母
print('===========================================================')

#user
users = {
    'aeinstrin': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    }
}

for username, user_info in users.items():
    print(f'{username} 的信息是：')
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(full_name)
    print(location)





