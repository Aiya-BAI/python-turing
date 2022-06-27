# 在Python中，首字母大写的名称指的是类.这个类定义中的括号是空的，因为我们要从空白创建这个类

class Dog:

    """模拟小狗"""
    # 类中的函数称为方法，开头和末尾各有两个下划线，这是一种约定，旨在避免Python默认方法与普通方法发生名称冲突
    # 在这个方法的定义中，形
    # 参self必不可少，还必须位于其他形参的前面。为何必须在方法定义中包含形参self呢？因为
    # Python调用这个__init__()
    # 方法来创建Dog实例时，将自动传入实参self。每个与类相关联的方法
    # 调用都自动传递实参self，它是一个指向实例本身的引用，让实例能够访问类中的属性和方法。

    def __init__(self, name, age):

        """初始化属性name和age"""
        # 以self为前缀的变量都可供类中的所有方法使用，我们还可以通过类的任何实例来访问这些变量
        self.name = name
        self.age = age

    def sit(self):
        print(f'{self.name.title()} is now sitting')

    def roll_over(self):
        print(f'{self.name.title()} rolled over')

# 访问属性
my_dog = Dog('willie', 6)
print(f'name is {my_dog.name.title()}')
print(f'dog is {my_dog.age} years old')

# 调用方法
my_dog.sit()
my_dog.roll_over()
print()

young_dog = Dog('lucy', 3)
print(f'name is {young_dog.name.title()}')
print(f'dog is {young_dog.age} years old')
young_dog.sit()
young_dog.roll_over()


