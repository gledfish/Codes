import pandas as pd

data1 = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
data2 = [['Google',10],['Runoob',12],['Wiki',13]]

df1 = pd.DataFrame(data1)
df2= pd.DataFrame(data2)

print(df1, df2)
print(df1.loc[0], df2.loc[0])

