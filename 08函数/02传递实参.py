def describe_pet(animal_type, pet_name):
    """显示宠物信息"""
    print(f'i have a {animal_type}')
    print(f"my {animal_type}'s name is {pet_name.title()}")


describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
describe_pet(pet_name='willie', animal_type='dog')
print()


# 由于给animal_type指定了默认值，
# 无需通过实参来指定动物类型，因此在函数调用中只包含一个实参——宠物的名字。然而， Python
# 依然将这个实参视为位置实参，因此如果函数调用中只包含宠物的名字，这个实参将关联到函数
# 定义中的第一个形参。这就是需要将pet_name放在形参列表开头的原因所在
def describe_pet1(pet_name, animal_type='dog'):
    """显示宠物信息"""
    print(f'i have a {animal_type}')
    print(f"my {animal_type}'s name is {pet_name.title()}")


describe_pet1(pet_name='marry')
describe_pet1('marry')


#例子
def make_shirt(size='大号', string=' i love python'):
    """显示shirt信息"""
    print(f'尺码是：{size}')
    print(f'印花是：{string}')

make_shirt()
make_shirt('中号')







