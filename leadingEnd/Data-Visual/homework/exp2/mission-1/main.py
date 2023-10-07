from pyecharts import options as opts
from pyecharts.charts import Line3D

import math

def create_spiral(accuracy):
    '''
生成螺旋曲线的数据点
accuracy:螺旋曲线上的点的数量，数量越多，点之间的距离越小
    '''
    data = []
    for t in range(0, accuracy):
        theta = t / accuracy * 10 * 2 * math.pi  # 角度范围从0到2π
        x = 5 * math.cos(theta)  # x坐标
        y = 5 * math.sin(theta)  # y坐标
        z = t / accuracy * 10 * math.pi  # z坐标，每旋转一周z坐标增加π
        data.append([x, y, z])
    return data

# 创建3D线图
if __name__ == "__main__":
    data = create_spiral(100000)
    line3d = (
        Line3D()
        .add(
            "3D螺旋线",
            data,
            xaxis3d_opts=opts.Axis3DOpts(type_="value"),
            yaxis3d_opts=opts.Axis3DOpts(type_="value"),
            zaxis3d_opts=opts.Axis3DOpts(type_="value"),
            grid3d_opts=opts.Grid3DOpts(width=100, height=100, depth=100),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="3D螺旋曲线图"), # 标题
            visualmap_opts=opts.VisualMapOpts(
                dimension=2,
                max_=3.15 * 10,  # z坐标最大值
                min_=0,  # z坐标最小值
                range_color=["green","blue","yellow","orange", "red"],
            )
        )
    )

# 保存为HTML文件或者在Jupyter Notebook中显示
line3d.render("exp2/mission-1/spiral.html")
