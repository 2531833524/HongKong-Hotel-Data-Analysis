import pandas as pd

df = pd.read_excel('./酒店数据1.xlsx')
print(df.head())
print(df['评分'].dtypes)  # float64
# 评分按升序排序
print(df.sort_values(by='评分', ascending=True))
# 评分按降序排序
print(df.sort_values(by='评分', ascending=False))
# 按照价格进行排名
print(df.sort_values(by='价格', ascending=False))
# 计算油尖旺地区的均价
print(round(df[df['地区'] == '油尖旺']['价格'].mean(), 2))
# 对酒店数据进行描述性统计，并求所有价格的均值方差，最大最小值，中值。
print('*' * 60)
print(df['价格'].describe())
'''
count      397.000000
mean       681.659950  #均值
std        906.282671  #标准差
min         67.000000  #最小值
25%        247.000000  #上四分位数
50%        418.000000  #结合中位数
75%        766.000000  #下四分位数
max      12926.000000  #最大值
Name: 价格, dtype: float64
'''
# 计算评分和价格的相关系数，协方差
print('*' * 60)
print(round(df['评分'].corr(df['价格']), 2))  # 相关系数 0.2881887477836199
print(round(df['评分'].cov(df['价格']), 2))  # 协方差 126.41083185662454  正相关
# 按照评分降序排序，评分相同时按价格升序排序
print(df.sort_values(by=['评分', '价格'], ascending=[False, True]))
'''
211          香港李女士宾馆(家庭旅馆)(MS LI GUEST HOUSE)  地铁周边  香港  ...  4.9    7  351
333     香港新金冠宾馆(New Golden Crown Guest House)    客栈  香港  ...  4.9   10  395
317     香港尊贵旅馆(Hong Kong Premium Guest House)    其他  香港  ...  4.8   19  166
199                        香港鸣人宾馆(Naruto Inn)  地铁周边  香港  ...  4.8  921  190
75             香港和平客栈(HK Peaceful Guesthouse)    民宿  香港  ...  4.8  511  264
..                                        ...   ...  ..  ...  ...  ...  ...
332         香港欣欣宾馆(家庭旅馆)(YAN YAN GUEST HOUSE)  地铁周边  香港  ...  2.3    6  977
360           香港港龙酒店(Comfort Lodge Hong Kong)  地铁周边  香港  ...  2.2   18  492
280  香港经济型酒店  (家庭旅馆)(Hong Kong Budget Hostel)  地铁周边  香港  ...  2.0   29   67
282        巴黎旅馆(Paris Guest House (D2, 10/F))    其他  香港  ...  2.0    5   67
385             香港中 港酒店(家庭旅馆)(HK-China Hotel)  地铁周边  香港  ...  1.5    7  429
'''
# 计算出，评分小于3分的酒店和占比。
df2 = df[df['评分'] < 3]
print(len(df2))
# 12
per = str(round(((len(df2) / len(df)) * 100), 2)) + '%'
print(per)
# 0.030226700251889168
# 统计出酒店评分大于等于4分的酒店价格的均值
print(round(df[df['评分'] >= 4]['价格'].mean(), 2))
# 计算出每个地区的酒店占总酒店数量的比列。
print('*' * 60)
print(df['地区'].value_counts())
per = round((df['地区'].value_counts() / len(df))*100, 2)
print(per.astype(str)+'%')
'''
油尖旺      46.6%
其他      14.11%
湾仔      10.33%
中西区      8.31%
九龙城      5.29%
东区       4.03%
离岛       2.77%
荃湾       1.76%
观塘       1.76%
葵青       1.26%
南区       1.26%
沙田       1.01%
屯门        0.5%
元朗        0.5%
罗湖区      0.25%
深水埗区     0.25%
Name: 地区, dtype: object
'''
# 找出酒店评分人数排名前20的酒店，并计算他们的价格均值。
print('*' * 60)
print(df.sort_values(by='评分人数', ascending=False)[:20]['价格'].mean())
# 查看酒店分布的类型数量和地区数量，并统计各个类型和地区包含的酒店数量
# 查看类型和类型数量
print(df['类型'].unique())
print(len(df['类型'].unique()))
print(df['地区'].unique())
print(len(df['地区'].unique()))
# 统计各个类型和地区包含的酒店数量
print(df['类型'].value_counts())
print(df['地区'].value_counts())
