from pyecharts import options as opts
from pyecharts.charts import Surface3D

import numpy as np
from scipy.stats import multivariate_normal

def generate_normal_distribution_data(mean, cov, x_range, y_range, num_points):
    '''
    生成二维正态分布的数据,返回包含三个数组的元组 (X, Y, Z)
    mean:均值
    cov:方差
    x_range:x的取值范围
    y_range:y的取值范围
    num_points:数据点的数量
    '''
    x = np.linspace(x_range[0], x_range[1], num_points)
    y = np.linspace(y_range[0], y_range[1], num_points)
    X, Y = np.meshgrid(x, y)
    pos = np.dstack((X, Y)) # 表示三维空间中的每个点
    rv = multivariate_normal(mean, cov)
    Z = rv.pdf(pos) # # 计算每个点的概率密度
    
    return X, Y, Z

if __name__ == "__main__":

    # 数据
    mean = [0, 0]
    cov = [[1, 0.5], [0.5, 1]]
    x_range = (-5, 5)
    y_range = (-5, 5)
    num_points = 400


    X, Y, Z = generate_normal_distribution_data(mean, cov, x_range, y_range, num_points)

    # 创建Surface3D图表
    surface = (
        Surface3D()
        .add(
            "二维正态分布",
            [list(x) for x in zip(X.ravel(), Y.ravel(), Z.ravel())],
            shading="color",
            grid3d_opts=opts.Grid3DOpts(width=100, height=100),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts("二维正态分布曲面图"),
            visualmap_opts=opts.VisualMapOpts(
                dimension=2,
                max_=Z.max(),
                min_=Z.min(),
                range_color=["green", "blue", "yellow", "orange", "red"],
            )
        )
        .set_series_opts(
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(width=0.5),
        )
    )

    # 保存为HTML文件或者在Jupyter Notebook中显示
    surface.render("exp2/mission-2/main.html")
