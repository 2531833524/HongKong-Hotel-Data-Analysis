import matplotlib.pyplot as plt
import pandas as pd

# 解决中问问题
plt.rcParams['font.sans-serif'] = 'SimHei'
df = pd.read_excel('./酒店数据1.xlsx')
data = df['地区'].value_counts()
print(data)
x = data.index
y = data.values
# 设置画布的宽和高
plt.figure(figsize=(10, 6))
plt.title('各个地区酒店数量', fontsize=20)
plt.xlabel('地区', fontsize=16)
plt.ylabel('数量', fontsize=16)
plt.bar(x, y, color='r', label='数量')
# x坐标轴的字体
plt.tick_params(labelsize=10)
# 调整x轴竖着显示
plt.xticks(rotation=90)
for a, b in zip(x, y):
    # 第一个参数：x轴的位置，第二个参数y轴的位置，第三个参数就是显示的值
    plt.text(a, b + 0.2, b, ha='center', va='bottom', fontsize=10)
plt.legend()
plt.show()
