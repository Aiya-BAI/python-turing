#人们
people_0 = {
    'first_name': 'bai',
    'last_name': 'yunce',
    'age': 25,
    'city': 'changli',
}
people_1 = {
    'first_name': 'sun',
    'last_name': 'jingyao',
    'age': 24,
    'city': 'tianjin',
}
people_2 = {
    'first_name': 'bai',
    'last_name': 'yang',
    'age': 26,
    'city': 'changli',
}
people = [people_0, people_1, people_2]
for p in people:
    print(f"全名：{p['first_name']} {p['last_name']}")
    print(f"年龄：{p['age']}")
    print(f"住址：{p['city']}\n")

#favorite_places
favorite_places = {
    'baiyunce': ['changli', 'beijing', 'tianjin'],
    'sunjingyao': ['changli', 'tianjin', 'qinhuangdao'],
    'baiyang': ['qinhuangdao', 'tangshan'],
}

for name, places in favorite_places.items():
    print(f"{name}喜欢的地方：")
    for place in places:
        print(f'\t{place}')

#城市
cities = {
    'changli': {
        'country': 'china',
        'population': 100000,
        'fact': 'cl',
    },
    'tianjin': {
        'country': 'china',
        'population': 200000,
        'fact': 'tj',
    },
    'beijing': {
        'country': 'china',
        'population': 500000,
        'fact': 'bj',
    },
}

print()
for city, city_infos in cities.items():
    print(f'{city}里边有:')
    for name, city_info in city_infos.items():
        print(f'\t{name}：{city_info}')











