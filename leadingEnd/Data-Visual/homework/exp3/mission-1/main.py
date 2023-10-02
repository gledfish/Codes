import openpyxl
import datetime
from pyecharts import options as opts
from pyecharts.charts import Map

def dataHandle(sheet, useless_row, useless_col):
    # 对表中数据进行预处理
    sheet.delete_cols(useless_col)
    sheet.delete_rows(useless_row)
    return sheet

def get_province(sheet,col):
    # 获得表中所有的省份，并返回省份：确诊人数的字典
    mySet = set()
    data_require = sheet[col]
    for cell in data_require:
        value = cell.value
        mySet.add(value)
    my_dict = {item: 0 for item in mySet}
    return my_dict 
    
def get_confirmed_cases(sheet,data_dict,date_tuple):
    # 获取确诊人数
    rawdata = []
    flag = 0  # 获取到数据的数量
    targetDate = datetime.datetime(date_tuple[0], date_tuple[1], date_tuple[2])
    # 获得截止到4月1日各省的累计确诊，如果4月1日数据丢失，则寻找最接近一天的数据
    while 1:
        for row in sheet.iter_rows(values_only=True):
            if row[6] == targetDate:
                rawdata.append(row)

        for i in rawdata:
            if data_dict[i[0]] == 0:
                data_dict[i[0]] += i[2]
                flag = flag+1
        if flag == len(data_dict):
            break
        else:
            targetDate = targetDate - datetime.timedelta(days=1)

    return data_dict
    
if __name__ == "__main__":
    # 导入工作簿
    workbook = openpyxl.load_workbook('exp3/mission-1/CityData.xlsx')
    # 导入工作表
    sheet = workbook.worksheets[0]
    # print(workbook.active)
# 数据处理
    # 去掉无关项
    row = 1
    col = 1
    sheet = dataHandle(sheet,row,col)
    data_dict = get_province(sheet,'A')
    data_dict = get_confirmed_cases(sheet,data_dict, (2020,4,1))


# 绘图
    c = (
        Map()
        # 全局配置项
        .set_global_opts(
            title_opts=opts.TitleOpts(title="确诊人数统计图"),
            visualmap_opts=opts.VisualMapOpts(
                max_=51000,
                is_piecewise=True,
                pieces=[
                    {"min": 0, "max": 10, "color": "#9ACD32"},
                    {"min": 10, "max": 100, "color": "#87CEEB"},
                    {"min": 100, "max": 200, "color": "#FFD700"},
                    {"min": 200, "max": 400, "color": "#FFA07A"},
                    {"min": 400, "max": 500, "color": "#FFA500"},
                    {"min": 500, "max": 51000, "color": "#FF0000"},
                ]
            ),
        )
        # 将data_dict作为数据映射到表中
        .add("截止到2020年4月1日的确诊人数", [list(z) for z in data_dict.items()], "china")

        # 渲染
        .render("exp3/mission-1/map_visualmap.html")
    )
