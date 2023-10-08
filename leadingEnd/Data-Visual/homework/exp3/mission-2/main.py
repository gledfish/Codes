import json
from pyecharts import options as opts
from pyecharts.charts import Map, Timeline


if __name__ == "__main__":
    
    # 导入处理好的数据
    with open('exp3/mission-2/data_dict.json', 'r', encoding='utf-8') as file:
        data_dict_everyDay = json.load(file)
    # print(data_dict_everyDay["2020-04-18"])
    # 绘图
    try:
        tl = Timeline()

        for date, value in data_dict_everyDay.items():
            my_map = (
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
                .add("2020年1月24日~2020年4月18日确诊人数变化图", [list(z) for z in value.items()], "china")
            )
            tl.add(my_map, date)
    # 渲染
        tl.render("exp3/mission-2/timeline_map.html")
    except:
        print("渲染失败")
