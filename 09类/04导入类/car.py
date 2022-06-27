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











