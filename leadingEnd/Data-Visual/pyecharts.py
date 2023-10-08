from pyecharts.charts import Line

import pyecharts.options
# 得到折线图对象
line = Line()  # 得到折线图对象
# 添加x轴数据
line.add_xaxis(['中国', '美国', '英国'])
# 添加y轴数据
line.add_yaxis("GDP", [30, 20, 10])

# 配置全局配置项
line.set_global_opts(
    title_opts= pyecharts.options.TitleOpts("GDP展示", pos_left="center", pos_bottom="1%"),
    legend_opts= pyecharts.options.LegendOpts(is_show = True),
    toolbox_opts = pyecharts.options.ToolboxOpts(is_show=True),
    visualmap_opts=pyecharts.options.VisualMapOpts(is_show=True),
)
# 生成图表
line.render()