import matplotlib.pyplot as plt
import pandas as pd

# 解决中问问题
plt.rcParams['font.sans-serif'] = 'SimHei'
df = pd.read_excel('./酒店数据1.xlsx')
print(df['价格'].describe())
'''
min         67.000000
25%        247.000000
50%        418.000000
75%        766.000000
max      12926.000000
'''
df['价格等级'] = pd.cut(df['价格'], [0, 500, 1000, 3000, 13000], labels=['经济', '中档', '高档', '奢华'])
data = df['价格等级'].value_counts()
print(data)
x = data.index
y = data.values
# 设置画布的宽和高
plt.figure(figsize=(10, 6))
plt.title('各个价格等级酒店数量', fontsize=20)
plt.xlabel('价格等级', fontsize=16)
plt.ylabel('数量', fontsize=16)
plt.bar(x, y, color='r', label='数量')
# x坐标轴的字体
plt.tick_params(labelsize=10)
for a, b in zip(x, y):
    # 第一个参数：x轴的位置，第二个参数y轴的位置，第三个参数就是显示的值
    plt.text(a, b + 0.2, b, ha='center', va='bottom', fontsize=10)
plt.legend()
plt.show()
