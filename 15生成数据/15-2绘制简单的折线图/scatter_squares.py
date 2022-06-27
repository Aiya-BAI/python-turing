import matplotlib.pyplot as plt

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, s=10, c=(0, 0.8, 0))
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# 设置图标标题并给坐标轴加上标签
ax.set_title('平方数', fontsize=24)
ax.set_xlabel('值', fontsize=14)
ax.set_ylabel('值的平方', fontsize=14)

# 设置刻度标记大小
ax.tick_params(axis='both', which='major', labelsize=15)
ax.axis([0, 1100, 0, 1100000])

plt.show()
# plt.savefig('squares_plot2.png')
