class Restaurant:

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe_restaurant(self):
        print(f'name is {self.name.title()}')
        print(f'type is {self.type}')

    def open_restaurant(self):
        print(f'{self.name}餐馆正在营业')


class IceCreamStand(Restaurant):
    def __init__(self, name, type):
        super().__init__(name, type)
        self.flavors = ['qiangkeli', 'apple', 'banana']

    def describe_ices(self):
        for ice in self.flavors:
            print(f'冰激凌有{ice}口味')


ice = IceCreamStand('bai', 'ice')
ice.describe_restaurant()
ice.describe_ices()










