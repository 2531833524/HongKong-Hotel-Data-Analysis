import matplotlib.pyplot as plt
import pandas as pd

# 解决中问问题
plt.rcParams['font.sans-serif'] = 'SimHei'
df = pd.read_excel('./酒店数据1.xlsx')
print(df['评分人数'].describe())
'''
min          1.000000
25%         96.000000
50%        869.000000
75%       3283.000000
max      45463.000000
'''
df['热门等级'] = pd.cut(df['评分人数'], [0, 100, 1000, 5000, 50000], labels=['鲜为人知', '略有耳闻', '小有名气', '人尽皆知'])
r1_mean = df[df['热门等级'] == '鲜为人知']['评分'].mean()
r2_mean = df[df['热门等级'] == '略有耳闻']['评分'].mean()
r3_mean = df[df['热门等级'] == '小有名气']['评分'].mean()
r4_mean = df[df['热门等级'] == '人尽皆知']['评分'].mean()
labels = ['鲜为人知', '略有耳闻', '小有名气', '人尽皆知']
x = labels
y = [r1_mean, r2_mean, r3_mean, r4_mean]
# 设置画布的宽和高
plt.figure(figsize=(10, 6))
plt.title('各个热门等级酒店评分均值', fontsize=20)
plt.xlabel('价格等级', fontsize=16)
plt.ylabel('评分均值', fontsize=16)
plt.bar(x, y, color='r', label='评分均值')
# x坐标轴的字体
plt.tick_params(labelsize=10)
for a, b in zip(x, y):
    # 第一个参数：x轴的位置，第二个参数y轴的位置，第三个参数就是显示的值
    plt.text(a, b, round(b, 2), ha='center', va='bottom', fontsize=10)
plt.legend()
plt.show()
