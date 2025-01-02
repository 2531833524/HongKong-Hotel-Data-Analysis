import matplotlib.pyplot as plt
import pandas as pd

# 解决中文问题
plt.rcParams['font.sans-serif'] = 'SimHei'
df = pd.read_excel('./酒店数据1.xlsx')
data = df['评分']
plt.hist(data, bins=20, edgecolor='k', alpha=0.5)
plt.title('酒店的评分频率')
plt.show()
