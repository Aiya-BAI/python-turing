class Restaurant:

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe_restaurant(self):
        print(f'name is {self.name.title()}')
        print(f'type is {self.type}')

    def open_restaurant(self):
        print(f'{self.name}餐馆正在营业')

restaurant = Restaurant('BAIYUNCE', '中餐')
restaurant.describe_restaurant()
restaurant.open_restaurant()







