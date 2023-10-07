from sklearn.cluster import KMeans  
import numpy as np  
import matplotlib.pyplot as plt  
  
# 创建一个包含2维数据的numpy数组  
X = np.array([[1, 2], [1, 4], [1, 0],  
              [10, 2], [10, 4], [10, 0],[2,5], [4, 10],[2, 6], [4, 6]])  
  
# 创建KMeans实例，设置聚类数量为3  
kmeans = KMeans(n_clusters=3, random_state=0)  
  
# 使用KMeans进行聚类  
kmeans.fit(X)  
  
# 输出聚类结果  
print(kmeans.labels_)  
  
# 预测新数据点的类别  
print(kmeans.predict([[0, 0], [12, 3], [5,8], [9, 1], [10, 2]]))  
  
# 输出聚类中心  
print(kmeans.cluster_centers_)  
  
# 可视化结果  
plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap='viridis')  
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red') # 将聚类中心用红色标出  
plt.savefig("machine-learning/src/k-means/k-means.jpg")
