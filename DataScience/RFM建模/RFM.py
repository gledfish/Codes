import pandas as pd
import numpy as np
def transform_label(x):
    if x == 111:
        label = '重要价值客户'
    elif x == 110:
        label = '消费潜力客户'
    elif x == 101:
        label = '频次深耕客户'
    elif x == 100:
        label = '新客户'
    elif x == 11:
        label = '重要价值流失预警客户'
    elif x == 10:
        label = '一般客户'
    elif x == 1:
        label = '高消费唤回客户'
    elif x == 0:
        label = '流失客户'
    return label

# 数据概览
df = pd.read_excel('PYTHON-RFM实战数据.xlsx')
df.head()
# 查看订单状态内容
df['订单状态'].unique()
# 查看数据类型和缺失情况
df.info()
# 数据清洗
df = df.loc[df['订单状态'] == '交易成功', :]  # 剔除退款
df = df[['买家昵称', '付款日期', '实付金额']]  # 关键字段提取
df.head()

#获得R值
r = df.groupby('买家昵称')['付款日期'].max().reset_index()
r['R'] = (pd.to_datetime('2019-7-1') - r['付款日期']).dt.days
r = r[['买家昵称', 'R']]
#获得F值
df['日期标签'] = df['付款日期'].astype(str).str[:10]
dup_f = df.groupby(['买家昵称', '日期标签'])['付款日期'].count().reset_index()
f = dup_f.groupby('买家昵称')['付款日期'].count().reset_index()
f.columns = ['买家昵称', 'F']
#计算M值

sum_m = df.groupby('买家昵称')['实付金额'].sum().reset_index()
sum_m.columns = ['买家昵称', '总支付金额']
com_m = pd.merge(sum_m, f, left_on='买家昵称',right_on='买家昵称', how = 'inner')
com_m['M'] = com_m['总支付金额'] / com_m['F']
rfm = pd.merge(r, com_m, left_on='买家昵称', right_on='买家昵称', how = 'inner')
rfm = rfm[['买家昵称', 'R', 'F','M']]

rfm['R-SCORE'] = pd.cut(rfm['R'], bins= [0, 30, 60, 90, 120, 1000000], labels = [5, 4, 3, 2 ,1], right=False).astype(float)
rfm['F-SCORE'] = pd.cut(rfm['F'], bins= [1, 2, 3, 4, 5, 1000000], labels = [1, 2, 3, 4, 5], right=False).astype(float)
rfm['M-SCORE'] = pd.cut(rfm['M'], bins= [0, 50, 100, 150, 200, 1000000], labels = [1, 2, 3, 4, 5], right=False).astype(float)

rfm['R是否大于均值'] = (rfm['R-SCORE'] > rfm['R-SCORE'].mean()) * 1
rfm['F是否大于均值'] = (rfm['F-SCORE'] > rfm['F-SCORE'].mean()) * 1
rfm['M是否大于均值'] = (rfm['M-SCORE'] > rfm['M-SCORE'].mean()) * 1
#客户分层
rfm['人群数值'] = (rfm['R是否大于均值'] * 100) + (rfm['F是否大于均值'] * 10) + (rfm['M是否大于均值'] * 1)
rfm['人群类型'] = rfm['人群数值'].apply(transform_label)
rfm.style.bar(subset= '人群类型', color = '#99ff66', align='mid')
print(rfm.head())
