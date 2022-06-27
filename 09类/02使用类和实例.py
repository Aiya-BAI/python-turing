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


my_new_car = Car('audi', 'a4', '2016')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.odometer_reading = 23
my_new_car.read_odometer()


my_new_car.update_odometer(45)
my_new_car.read_odometer()

print()
my_new_car1 = Car('benci', 'e300l', '2019')
my_new_car1.read_odometer()
my_new_car1.increasent_odometer(45)
my_new_car1.increasent_odometer(34)
my_new_car1.read_odometer()


# 就餐人数
print('++++++++++++++++++++就餐人数+++++++++++++++++++++')


class Restaurant:
    def __init__(self):
        self.number_served = 0

    def set_number_served(self, num):
        print(f'就餐人数{num}')

    def increment_number_served(self, num):
        num += num
        print(f'递增就餐人数{num}')


restaurant = Restaurant()
print(restaurant.number_served)

restaurant.set_number_served(34)
restaurant.increment_number_served(45)

# 尝试登录次数
class User:
    def __init__(self):
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


print(f'\n=====================尝试登录次数===============')
user = User()

i = 0
while i < 10:
    user.increment_login_attempts()
    i += 1
print(user.login_attempts)

user.reset_login_attempts()
print(user.login_attempts)









