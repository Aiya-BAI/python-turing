import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)
    dates, highs = [], []
    for row in reader:
        high = int(row[5])
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        highs.append(high)
        dates.append(current_date)
print(highs)
print(dates)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

# 设置图标标题并给坐标轴加上标签
ax.set_title('2018年7月每日最高温度', fontsize=24)
ax.set_xlabel('', fontsize=14)
ax.set_ylabel('温度', fontsize=14)
ax.tick_params(axis='both', which='major')

plt.show()


# for index, column_header in enumerate(header_row):
#     print(index, column_header)


