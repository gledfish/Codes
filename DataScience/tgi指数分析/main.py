import pandas as pd

df = pd.read_excel('TGI指数案例数据.xlsx')

gp_user = df.groupby('买家昵称')['实付金额'].mean().reset_index()


def if_high(x):
    """判断是否为高客单"""
    if x > 50:
        return '高客单'
    else:
        return '低客单'


gp_user['客单类别'] = gp_user['实付金额'].apply(if_high)
#按照昵称去重
df_dup = df.loc[df.duplicated('买家昵称') == False, :]
# 合并字段
df_merge = pd.merge(gp_user, df_dup, left_on='买家昵称', right_on='买家昵称', how='left')

df_merge = df_merge[['买家昵称', '客单类别', '省份', '城市']]

result = pd.pivot_table(df_merge, index=['省份', '城市'], columns='客单类别', aggfunc = 'count')

tgi = pd.merge(result['买家昵称']['高客单'].reset_index(), result['买家昵称']['低客单'].reset_index(),
               left_on=['省份', '城市'], right_on=['省份', '城市'], how='inner')
tgi['总人数'] = tgi['高客单'] + tgi['低客单']
tgi['高客单占比'] = tgi['高客单'] / tgi['总人数']
tgi = tgi.dropna()
total_percentage = tgi['高客单'].sum() / tgi['总人数'].sum()

tgi['高客单TGI指数'] = tgi['高客单占比'] / total_percentage * 100
tgi = tgi.sort_values('高客单TGI指数', ascending = False)
print(tgi.loc[tgi['总人数'] > tgi['总人数'].mean(), :].head(10))
