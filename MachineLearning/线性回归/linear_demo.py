# 导入数据
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 读取CSV文件中的训练和测试数据
train_data = pd.read_csv(r"D:\ALL_code\al_study_file\al_study\MachineLearning\线性回归\linear_data01\train.csv")
test_data = pd.read_csv(r"D:\ALL_code\al_study_file\al_study\MachineLearning\线性回归\linear_data01\test.csv")

# 分离训练数据的特征和标签
X_train = train_data.iloc[:, :-1].values  # 特征列
y_train = train_data.iloc[:, -1].values  # 标签列

# 分离测试数据的特征和标签
X_test = test_data.iloc[:, :-1].values
y_test = test_data.iloc[:, -1].values


# 定义一个线性回归模型
class LinearRegression:
    def __init__(self, learning_rate, num_iterations):
        """
        初始化线性回归模型参数
        :param learning_rate: 学习率，控制模型更新的步长
        :param num_iterations: 迭代次数，即训练轮数
        """
        self.learning_rate = learning_rate
        self.num_iterations = num_iterations
        self.W = None  # 权重
        self.b = None  # 偏置

    def fit(self, X, y):
        """
        根据训练数据集X和标签y训练模型
        :param X: 训练数据集的特征，形状为[n_samples, n_features]
        :param y: 训练数据集的标签，形状为[n_samples,]
        """
        n_samples, n_features = X.shape
        self.W = np.zeros(n_features)  # 初始化权重为零向量
        self.b = 0  # 初始化偏置为零

        # 进行梯度下降迭代
        for _ in range(self.num_iterations):
            # 计算当前权重和偏置下的预测值
            y_pred = np.dot(X, self.W) + self.b

            # 计算权重和偏置的梯度
            dw = (1 / n_samples) * np.dot(X.T, (y_pred - y))
            db = (1 / n_samples) * np.sum(y_pred - y)

            # 更新权重和偏置
            self.W -= self.learning_rate * dw
            self.b -= self.learning_rate * db

    def predict(self, X):
        """
        根据特征X进行预测
        :param X: 特征数据，形状为[n_samples, n_features]
        :return: 预测结果，形状为[n_samples,]
        """
        return np.dot(X, self.W) + self.b


# 创建模型实例并设置学习率和迭代次数
model = LinearRegression(learning_rate=0.01, num_iterations=1000)

# 使用训练数据拟合模型
model.fit(X_train, y_train)

# 在测试数据上预测结果
y_pred_test = model.predict(X_test)

# 计算测试集上的均方误差
mse = np.mean((y_pred_test - y_test) ** 2)
print(f"Test set Mean Squared Error: {mse}")

# 如果特征只有一个，可视化实际值和预测值
if X_test.shape[1] == 1:
    plt.scatter(X_test, y_test, color='blue', label='Actual')  # 绘制实际值
    plt.plot(X_test, y_pred_test, color='red', label='Predicted')  # 绘制预测值
    plt.xlabel('Feature')  # 设置x轴标签
    plt.ylabel('Target')  # 设置y轴标签
    plt.title('Linear Regression Prediction')  # 设置标题
    plt.legend()  # 显示图例
    plt.show()  # 显示图形
