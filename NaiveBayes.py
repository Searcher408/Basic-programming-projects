from sklearn.datasets import load_iris
import padndas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

data = load_iris() # 读入iris数据集
X, y, column_names = data['data'], data['target'], data['feature_names']
X = pd.DataFrame(X, columns = column_names)
X_train, X_val, y_train, y_val = train_test_split(X, y, random_state = 44) # 划分训练集和测试集

model = GaussianNB() # 调用朴素贝叶斯模型
model.fit(X_train, y_train) # 训练
acc = accuracy_score(y_val, model.predict(X_val)) # 预测
print(acc)