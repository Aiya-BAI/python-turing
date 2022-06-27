import matplotlib.pyplot as plt

imput_value = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(imput_value, squares, linewidth=3)


# 设置图标标题并给坐标轴加上标签
ax.set_title('平方数', fontsize=24)
ax.set_xlabel('值', fontsize=14)
ax.set_ylabel('值的平方', fontsize=14)

# 设置刻度标记的大小
ax.tick_params(axis='both', labelsize=14)

# 汉字字体，优先使用楷体，找不到则使用黑体
plt.rcParams['font.sans-serif'] = ['Kaitt', 'SimHei']
# 正常显示负号
plt.rcParams['axes.unicode_minus'] = False

plt.show()

