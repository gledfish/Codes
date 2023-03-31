
import os
import pandas as pd
import time

pd.set_option('display.float_format', lambda x:'%.2f' % x)
os.chdir('D:\\数据分析\\Python批量处理excel表格\\excel_data')
name = '垂钓装备&绑钩器.xlsx'
df = pd.read_excel(name)
# print(df.head())
# df['日期'].unique()
df['销售额'] = df['访客数'] * df['转化率'] * df['客单价']
df_sum = df.groupby('品牌')['销售额'].sum().reset_index()
df_sum['行业'] = name.replace('.xlsx','')

# 处理多个表格
start = time.time()

result = pd.DataFrame()

for name in os.listdir():
    df = pd.read_excel(name)
    df['销售额'] = df['访客数'] * df['转化率'] * df['客单价']
    df_sum = df.groupby('品牌')['销售额'].sum().reset_index()
    df_sum['行业'] = name.replace('.xlsx', '')
    result = pd.concat([result, df_sum])

final = result.groupby('品牌')['销售额'].sum().reset_index().sort_values('销售额', ascending = False)

end = time.time()
print(end - start)


