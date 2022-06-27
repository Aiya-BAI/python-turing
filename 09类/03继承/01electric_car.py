class Car:
    """一次模拟汽车"""

    def __init__(self, make, model, year):

        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0    #里程


    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name

    def read_odometer(self):
        print(f'this car has {self.odometer_reading} miles')

    def update_odometer(self, mileage):
        """改里程"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('里程不能往回调')

    def increasent_odometer(self, mileage):
        """将里程表读数增加指定的量"""
        self.odometer_reading += mileage

# 创建子类时，父类必须包含在当前文件中，且位于子类前面
# 定义子类时，必须在圆括号内指定父类的名称

class ElectricCar(Car):
    """电动汽车独特之处"""
    def __init__(self, make, model, year):
        # super() 是一个特殊函数，让你能够调用父类的方法。父类也称为超类 （superclass），名称super 由此而来
        super().__init__(make, model, year)
        self.battety_size = 75


    """电动车独特之处"""
    def describe_battery(self):
        print(f'car has a {self.battety_size}-kWh')

my_benci = ElectricCar('benci', 'gls450', 2021)
print(my_benci.get_descriptive_name())
my_benci.describe_battery()








