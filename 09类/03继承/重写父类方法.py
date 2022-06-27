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
    def fill_gas_tank(self):
        print('super mothod')


class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f'car has a {self.battery_size}-kWh')

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f'this car can go about {range} miles')


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print('this car does not need a gas tank')


my_electricCar = ElectricCar('benci', 'gls', '2022')

print(my_electricCar.get_descriptive_name())
my_electricCar.fill_gas_tank()

my_electricCar.battery.describe_battery()
my_electricCar.battery.get_range()

my_electricCar.battery.battery_size = 100
my_electricCar.battery.get_range()
















