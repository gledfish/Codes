import numpy as np  
import matplotlib.pyplot as plt  
from mpl_toolkits.mplot3d import Axes3D  
  
# 均值和协方差矩阵  
mu = np.array([0, 0])  
sigma = np.array([[1, 0], [0, 1]])  
  
# 创建网格  
x = np.linspace(-3, 3, 100)  
y = np.linspace(-3, 3, 100)  
X, Y = np.meshgrid(x, y)  
  
# 计算二维正态分布的概率密度函数值  
Z = np.exp(-0.5 * ((X - mu[0]) ** 2 / sigma[0][0] + (Y - mu[1]) ** 2 / sigma[1][1]))  
  
# 创建一个3D图像  
fig = plt.figure()  
ax = fig.add_subplot(111, projection='3d')  
  
# 在3D图像中绘制二维正态分布曲面图  
ax.plot_surface(X, Y, Z, cmap='viridis')  
ax.set_xlabel('X')  
ax.set_ylabel('Y')  
ax.set_zlabel('Z')  
ax.set_title('2D Normal Distribution Surface')  
  
# 显示图像  
plt.savefig('main.jpeg')