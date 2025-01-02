import matplotlib.pyplot as plt
import pandas as pd

# 解决中问问题
plt.rcParams['font.sans-serif'] = 'SimHei'
df = pd.read_excel('./酒店数据1.xlsx')
print(df['价格'].describe())
df['价格等级'] = pd.cut(df['价格'], [0, 500, 1000, 3000, 13000], labels=['经济', '中档', '高档', '奢华'])
data = df['价格等级'].value_counts()
plt.pie(x=data.values, labels=data.index, autopct='%.0f%%', shadow=True)
plt.show()
