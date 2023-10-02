
import pyecharts.options as opts
from pyecharts.charts import Bar3D
import pandas as pd


# 数据预处理
def dataHandle(data):
    # 数据拼接
    data_list = data.values.tolist()
    year_data = []
    date_data = []
    fixed_data = []
    for i in range(len(data_list)):
        year_data.append(data_list[i][0][:4])
        date_data.append(data_list[i][0][5:7] + "/" + data_list[i][0][8:])
        fixed_data.append([year_data[i], date_data[i], data_list[i][1]])
    
    # 日期去重
    unique_date = []    
    for item in date_data:
        if item not in unique_date:
            unique_date.append(item)
    return unique_date, fixed_data
    

if __name__ == "__main__":
    # 数据导入
    data = pd.read_csv('exp1/dataset.csv')
    # print(data.head())
    result_tuple = dataHandle(data)
    unique_date = result_tuple[0]
    fixed_data = result_tuple[1]
# 数据可视化
    my_chart = (
        Bar3D()
            .add(
                series_name="温度",
                data=fixed_data,
                xaxis3d_opts=opts.Axis3DOpts(type_="category", data=[str(i) for i in range(1981, 1991)]),
                yaxis3d_opts=opts.Axis3DOpts(type_="category", data=unique_date),
                zaxis3d_opts=opts.Axis3DOpts(type_="value", data=[str(i) + "°C" for i in range(0, 22)]),
                # 设置样式
                shading="color",
                grid3d_opts=opts.Grid3DOpts(depth=200),
                # 通过改变 depth 让图在美观和实用之间转换
            )
            .set_global_opts(
                visualmap_opts=opts.VisualMapOpts(max_=30),
                title_opts=opts.TitleOpts(title=" 温度示意图 "),
            )
            .render("exp1/exp1.html")
)
