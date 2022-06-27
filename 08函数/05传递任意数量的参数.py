def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print(toppings)


make_pizza('pepero')
make_pizza('ksadf', 'lakhd ', 'jkdh')

# 返回元组
def make_pizza1(size, *toppings):
    print(f'{size}的披萨，配料是{toppings}')


make_pizza1(12,'lkdsh', 'lkahdsf ', 'kjadhf')

# 返回字典
def make_pizza2(color, size, **toppings):
    """创建一个字典"""
    pizza2 = {}
    pizza2['color'] = color
    pizza2['size'] = size
    for key, value in toppings.items():
        pizza2[key] = value
    return pizza2

print(make_pizza2('red', 13, topping1='lakdsjf', topping2='akjdhg'))
print(make_pizza2('red', 13))

print('\n')


# 例子三明治
def make_sandwichs(*toppings):
    print(toppings)


make_sandwichs('laskhdg', 'lakshg', 'lashd')


# 例子汽车
def car_info(made, xinghao, **others):
    car = {'made': made, 'xinghao': xinghao}
    for key, value in others.items():
        car['key'] = value
    return car

print(car_info('china', 'changcheng', color='red', tow_package=True))










