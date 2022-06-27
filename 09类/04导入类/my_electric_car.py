from electric_car import ElectricCar as EC
# 使用别名

my_tesla = EC('tesla', 'model s', '2022')

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()








