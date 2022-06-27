import pizza

from pizza import make_pizza

import pizza as p

from pizza import make_pizza as m

from pizza import *  #不需要使用句点表示法，，不建议

# 最佳的做法是，要么只导入你需要使用的函数，要么导入整个模块并使用句点表示法

pizza.make_pizza(16, 'alshdg')
pizza.make_pizza(32, 'alksdhf', ';alkdhg', 'akjdsh')

make_pizza(16, 'alshdg')
make_pizza(32, 'alksdhf', ';alkdhg', 'akjdsh')

p.make_pizza(14, 'ladh')

m(235, 'alkjhd')

