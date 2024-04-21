# 导入相关模块
from sklearn.model_selection import train_test_split, GridSearchCV
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
# 1.获取数据集
data = pd.read_csv("D:\ALL_code\\al_study_file\\al_study\MachineLearning\Cancer_Data.csv")

# 2.基本数据处理
# 2.4 确定特征值和⽬标值
headers = data.columns.tolist()
headers = headers[2:-1]
x = data[headers]  # 特征值是一个二维数组（或者 DataFrame）
y = data["diagnosis"]  # 目标值是一个一维数组（或者 Series）

# 2.5 分割数据集
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=2, test_size=0.2)


# 3.特征⼯程 -- 特征预处理(标准化)
transfer = StandardScaler()
x_train = transfer.fit_transform(x_train)
x_test = transfer.fit_transform(x_test)

# 4.机器学习 -- knn+cv
# 4.1 实例化一个训练器
estimator = KNeighborsClassifier()

# 4.2 交叉验证，网格搜索是实现
param_grid = {"n_neighbors": [3, 5, 7, 9, 11, 13, 15, 17, 19, 21]}
estimator = GridSearchCV(estimator=estimator, param_grid=param_grid, cv=10)

# 4.3 模型训练
estimator.fit(x_train, y_train)

# 5.模型评估
# 5.1 准确率输出
score_ret = estimator.score(x_test, y_test)
print("准确率为：\n",score_ret)
# 5.2 预测结果
y_pred = estimator.predict(x_test)
print("预测值是: \n", y_pred)
print(y_test == y_pred)
# 5.3 其他结果输出
print("最好的模型是：\n", estimator.best_estimator_)
print("最好的结果是：\n", estimator.best_score_)
print("所有的结果是：\n", estimator.cv_results_)