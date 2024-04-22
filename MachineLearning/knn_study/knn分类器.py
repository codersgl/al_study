# encoding=utf8
import numpy as np
from collections import Counter


class kNNClassifier(object):
    def __init__(self, k):
        """
        初始化函数
        :param k:kNN算法中的k
        """
        self.k = k
        # 用来存放训练数据，类型为ndarray
        self.train_feature = None
        # 用来存放训练标签，类型为ndarray
        self.train_label = None

    def fit(self, feature, label):
        """
        kNN算法的训练过程
        :param feature: 训练集数据，类型为ndarray
        :param label: 训练集标签，类型为ndarray
        :return: 无返回
        """

        # 将训练数据赋值给类属性self.train_feature
        self.train_feature = feature
        # 将训练标签赋值给类属性self.train_label
        self.train_label = label

    def predict(self, feature):
        """
        kNN算法的预测过程
        :param feature: 测试集数据，类型为ndarray
        :return: 预测结果，类型为ndarray或list
        """

        # 初始化预测结果列表
        predict_results = []

        # 遍历测试集中的每个样本
        for test_sample in feature:
            # 计算当前测试样本与训练集中每个样本的欧氏距离
            distance = [np.sqrt(np.sum((test_sample - train_sample) ** 2)) for train_sample in self.train_feature]

            # 获取距离最小的k个样本的索引
            k_neighbors = np.argsort(distance)[:self.k]
            # 获取这k个样本的标签
            k_labels = [self.train_label[i] for i in k_neighbors]
            # 对这k个标签进行投票，找出出现次数最多的标签
            most_common = Counter(k_labels).most_common(1)
            # 将出现次数最多的标签作为当前测试样本的预测结果
            predict_results.append(most_common[0][0])
        # 将所有测试样本的预测结果转换为numpy数组并返回
        return np.array(predict_results)
