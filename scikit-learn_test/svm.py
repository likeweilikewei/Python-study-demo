#! /user/bin/env python
# -*- coding=utf-8 -*-


# 导入svm和数据集
from sklearn import svm,datasets
# 调用SVC()
clf = svm.SVC()
# 载入鸢尾花数据集
iris = datasets.load_iris()
X = iris.data
print('x:', type(X))
print('x:', X)
print(len(X))
y = iris.target
print('test_y:', type(y))
print('test_y:', y)
print(len(y))
# fit()训练
clf.fit(X,y)
# predict()预测
pre_y = clf.predict(X[5:10])
print(pre_y)
print(y[5:10])
# 导入numpy
import numpy as np
test = np.array([[5.1,2.9,1.8,3.6]])
# 对test进行预测
test_y = clf.predict(test)
print(test_y)
