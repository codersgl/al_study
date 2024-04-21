# 导入相关模块
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

# 1.获取数据集
iris = load_iris()

# 2.数据基本处理
# 2.1 数据分割
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=22, test_size=0.2)

# 3.特征工程
# 3.1 实例化一个转化器
transfer = StandardScaler()
# 3.2 调用fit_transform方法,数据标准化
x_train = transfer.fit_transform(x_train)
x_test = transfer.fit_transform(x_test)

# 4.机器学习(模型训练)
# 4.1 实例化一个估计器
estimator = KNeighborsClassifier(n_neighbors=5)
# 4.2 模型调优 -- 交叉验证，网格搜索'
param_grid = {'n_neighbors': [1, 3, 5, 7]}
estimator = GridSearchCV(estimator, param_grid=param_grid, cv=5)
# 4.3 进行模型训练
estimator.fit(x_train, y_train)

# 5.模型评估
# 5.1 输出预测值
y_pre = estimator.predict(x_test)
print("预测值是：\n", y_pre)
print("预测值和真实值对比：\n", y_pre == y_test)
# 5.2 输出准确率
score = estimator.score(x_test, y_test)
print("准确率是：\n", score)
# 5.3 查看交叉验证，网格搜索的一些属性
print("在交叉验证中，得到的最好结果是：\n", estimator.best_score_)
print("在交叉验证中，得到的最好模型参数是：\n", estimator.best_params_)
print("在交叉验证中，得到的最好的模型是：\n", estimator.best_estimator_)
print("在交叉验证中，得到的模型结果是：\n", estimator.cv_results_)
