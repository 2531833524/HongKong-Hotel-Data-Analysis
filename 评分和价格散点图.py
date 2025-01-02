import matplotlib.pyplot as plt
import pandas as pd

# 解决中问问题
plt.rcParams['font.sans-serif'] = 'SimHei'
df = pd.read_excel('./酒店数据1.xlsx')
x = df['价格']
y = df['评分']
plt.figure(figsize=(10,8))
plt.scatter(x, y, color='c')
plt.title('酒店价格与评分')
plt.xlabel('价格')
plt.ylabel('评分')
plt.show()
