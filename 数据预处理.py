import pandas as pd
import numpy as np

df = pd.read_excel('./香港酒店数据.xlsx')
print(df.head())
# 删除第一行的空值
# 或者df.drop(0,inplace=True)
df = df[1:]
# 重置索引
df.index = range(0, len(df))
print(df.head())
# 删除Unnamed列
df = df.drop('Unnamed: 0', axis=1)
df.columns = ['名字', '类型', '城市', '地区', '地点', '评分', '评分人数', '价格']
print(df.head())
df1 = df[(df['类型'] == '休闲度假') & (df['地区'] == '湾仔')]
print(df1)
df2 = df[((df['地区'] == '观塘') | (df['地区'] == '油尖旺')) & (df['评分'] > 4)]
print(df2)
# df3 = df[(((df['地区'] == '观塘') | (df['地区'] == '油尖旺')) & (df['评分'] > 4)) | ((df['类型'] == '休闲度假') & (df['地区'] == '湾仔'))]
# print(df3)
# print('*' * 30)
# print(df3[df3['地区'].isnull()])
# print('*' * 30)
# print(df3[df3['类型'].isnull()])
df['类型'] = df['类型'].fillna('其他')
df['地区'] = df['地区'].fillna('其他')
df['评分'] = df['评分'].fillna(df['评分'].mean())
df = df.dropna(axis=0, subset=['价格', '评分人数'])
print(df)
df.drop_duplicates(inplace=True)
print(df)
df.index = range(0, len(df))
print('*' * 30)
print(df.isnull().sum())
print(df.dtypes)
df['评分人数'] = df['评分人数'].astype(np.int64)
print(df.dtypes)
df.to_excel('酒店数据1.xlsx', index=False)
