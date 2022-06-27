alien_0 = {'color': 'green', 'points': '5'}
print(alien_0['color'])
print(alien_0['points'])
print(alien_0)

alien_0["x_position"] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0["color"] = "yellow"
print(alien_0)

del alien_0["points"]
print(alien_0)

print('======================================')
#多个对象组成的字典
favorite_languages = {
    'jen': 'python',
    'sarch': 'c',
    'edward': 'java',
    'phil': 'python',
}
print(favorite_languages)
print(f"phil 最喜欢的语言是{favorite_languages['phil'].title()}")

# print(favorite_languages['jan'])
print(favorite_languages.get('jen', '没有这个键'))
print(favorite_languages.get('jan', '没有这个键'))
print(favorite_languages.get('jan'))

print(favorite_languages.items())
print(type(favorite_languages))
print(type(favorite_languages.items()))
print()

#遍历键值对 items()
for name, language in favorite_languages.items():
    print(f'{name.title()}: {language}')
print()

#遍历键  key()
for name in favorite_languages.keys():
    print(f'{name.title()}')
for name in favorite_languages:
    print(f'{name.title()}')
print(favorite_languages.keys())
print(type(favorite_languages.keys()))

print()
friends = ['jen', 'phil']
for name in favorite_languages.keys():
    print(f'hello,{name.title()}')
    if name in friends:
        language = favorite_languages.get(name)
        print(f'\ti love {language}')

print()
for name in sorted(favorite_languages.keys()):
    print(name.title())

#遍历值  value()
print()
for value in favorite_languages.values():
    print(value)
print(favorite_languages.values())
print(type(favorite_languages))

print()
for value in set(favorite_languages.values()):
    print(value)
print(type(set(favorite_languages.values())))




