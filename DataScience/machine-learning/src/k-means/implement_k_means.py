import numpy as np
'''
基于欧式距离实现最基本的二维空间中的k_means算法(一轮)
算法设计思路
1. 挑选中心簇,即分类别
2. 对每个二维数据计算与中心簇的距离
3. 选取距离最小的簇即为结果
'''


def select_center(input_tuple, cluster_count=3):
    '''
    用随机数方法挑选中心簇
    input_tuple:所有的二维元组
    cluster_count:中心簇的个数
    输出由中心簇组成的字典
    '''
    # random_array = np.random.randint(0, len(input_tuple), cluster_count)

    dict_cluster = {input_tuple[0]:[],input_tuple[1]:[],input_tuple[2]:[2]}
    # for i, v in input_tuple:
    #     if i in random_array:
    #         dict_cluster[input_tuple[i]] = []

    return dict_cluster


def get_distance(input_tuple_1, input_tuple_2):
    '''生成欧式距离

    Args:
        input_tuple_1 (tuple): 输入的元组1
        input_tuple_2 (tuple): 输入的元组2

    Returns:
        float: 欧式距离
    '''
    x1 = np.array(input_tuple_1)  
    x2 = np.array(input_tuple_2)
    dist = np.linalg.norm(x1 - x2)
    return dist

def get_min_distance(dict_cluster, input_tuple):
    '''
    获得一个元组距离中心簇的最小距离,返回最小距离对应的簇
    dict_cluster:中心簇字典
    input_tuple:输入的元组
    '''
    distance_dict = {}
    flag = 0
    min_distance = 0
    # 获得距离数组
    for i, v in dict_cluster.items():
        distance = get_distance(i,input_tuple)
        distance_dict[input_tuple] = (i, distance)
    # 获得最小距离
    for i, v in distance_dict.items():
        if flag == 0:
            min_distance = v[1]
            target_cluster = i
            flag = 1
        elif flag == 1:
            if v[1] <= min_distance:
                min_distance = v[1]
                target_cluster = i
    
    return target_cluster

def add_cluster(dict_cluster,target_cluster, input_tuple):
    dict_cluster[target_cluster].append(input_tuple)
    return dict_cluster
    
    



if __name__ == "__main__":
    input_tuple = ((1, 2), (2, 4), (3, 7), (5, 6), (3, 8),
                   (6, 2), (7, 9), (9, 4), (3, 7), (8, 7))
    dict_cluster = select_center(input_tuple)
    print("簇:")
    print(dict_cluster)
    for item in input_tuple:
        target_cluster = get_min_distance(dict_cluster, item)
        print(target_cluster)
        dict_cluster = add_cluster(dict_cluster,target_cluster,item)

    # print(dict_cluster)
    # print(dict_cluster)
    # print(get_distance((0,0), (1,1)))

    
