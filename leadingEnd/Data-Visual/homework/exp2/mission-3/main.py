import math
import numpy as np
from pyecharts import options as opts
from pyecharts.charts import Scatter3D

def create_data(radius, points_num):
    ''' 
    生成球面数据点,返回一个二维列表,包含x, y, z三个列表
    radius:半径
    points_num:数据点的数量
    '''
    phi = np.linspace(0, 2 * np.pi, points_num) # 
    theta = np.linspace(0, np.pi, points_num)
    phi, theta = np.meshgrid(phi, theta)
    x = radius * np.sin(theta) * np.cos(phi)
    y = radius * np.sin(theta) * np.sin(phi)
    z = radius * np.cos(theta)
    return [x, y, z]

if __name__ == "__main__":
    radius = 5
    points_num = 100
    x, y, z = create_data(radius, points_num)
    # 创建3D散点图
    scatter3d = (
        Scatter3D()
        .add(
            "球",
            [list(z) for z in zip(x.reshape(-1), y.reshape(-1), z.reshape(-1))],
            grid3d_opts=opts.Grid3DOpts(width=100, height=100, depth=100),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts("球"),
            visualmap_opts=opts.VisualMapOpts(
                max_=radius,  # 球面半径
                range_color=["blue", "yellow","orange","red"],
            )
        )
    )

    # 保存为HTML文件或者在Jupyter Notebook中显示
    scatter3d.render("exp2/mission-3/main.html")
