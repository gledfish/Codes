import json
from pyecharts.charts import Line
import pyecharts.options

f_us = open('美国.txt', 'r', encoding='utf-8')
us_data = f_us.read()
us_data = us_data.replace('jsonp_1629344292311_69436(', '')
us_data = us_data[:-2]

us_dict = json.loads(us_data)

us_trend_data = us_dict['data'][0]['trend']
us_x_data = us_trend_data['updateDate']
us_x_data = us_x_data[:314]

# 成功获取x日期数据

us_y_data = us_trend_data['list'][0]['data'][:314]

f_jp = open('日本.txt', 'r', encoding='utf-8')
jp_data = f_jp.read()
jp_data = jp_data.replace('jsonp_1629350871167_29498(', '')
jp_data = jp_data[:-2]

jp_dict = json.loads(jp_data)

jp_trend_data = jp_dict['data'][0]['trend']
jp_x_data = jp_trend_data['updateDate']
jp_x_data = jp_x_data[:314]
# 成功获取x日期数据

jp_y_data = jp_trend_data['list'][0]['data'][:314]

f_in = open('印度.txt', 'r', encoding='utf-8')
in_data = f_in.read()
in_data = in_data.replace('jsonp_1629350745930_63180(', '')
in_data = in_data[:-2]

in_dict = json.loads(in_data)

in_trend_data = in_dict['data'][0]['trend']
in_x_data = in_trend_data['updateDate']
in_x_data = in_x_data[:314]
# 成功获取x日期数据

in_y_data = in_trend_data['list'][0]['data'][:314]

line = Line()
line.add_xaxis(us_x_data)
line.add_yaxis('美国确诊人数',us_y_data, label_opts = pyecharts.options.LabelOpts(is_show = False))
line.add_yaxis('日本确诊人数',jp_y_data, label_opts = pyecharts.options.LabelOpts(is_show = False))
line.add_yaxis('日本确诊人数',in_y_data, label_opts = pyecharts.options.LabelOpts(is_show = False))

line.set_global_opts(
    title_opts= pyecharts.options.TitleOpts("2020年美日印三国确诊人数对比图", pos_left="center", pos_bottom="1%"),
    legend_opts= pyecharts.options.LegendOpts(is_show = True),
    toolbox_opts = pyecharts.options.ToolboxOpts(is_show=True),
    visualmap_opts=pyecharts.options.VisualMapOpts(is_show=True),

)
line.render()

f_in.close()
f_jp.close()
f_us.close()
