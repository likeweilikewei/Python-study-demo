import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model

# Load the diabetes dataset  
diabetes = datasets.load_diabetes()  # load sklearn中自带的数据库

# print(np.shape(diabetes))
# print(diabetes)

# Use only one feature  
diabetes_X = diabetes.data[:, np.newaxis]
# print np.shape(diabetes_X)
print(diabetes_X)
diabetes_X_temp = diabetes_X[:, :, 2]
print(diabetes_X_temp)
# print np.shape(diabetes_X_temp)   //大小是442*1

# Split the data into training/testing sets  
diabetes_X_train = diabetes_X_temp[:-20]  # 前20个样本用来训练
diabetes_X_test = diabetes_X_temp[-20:]  # 后面的样本用来测试

# Split the targets into training/testing sets  
diabetes_y_train = diabetes.target[:-20]  # 标记也是和后面一样的
diabetes_y_test = diabetes.target[-20:]

# Create linear regression object  
regr = linear_model.LinearRegression()  # 调用线性模型中的线性回归

# Train the model using the training sets  
regr.fit(diabetes_X_train, diabetes_y_train)  # fit函数需要输入训练样本的特征和标记，这里的特征只有1维

# The coefficients  
print('Coefficients: \n', regr.coef_)  # 得到表示系数
# The mean square error  
print("Residual sum of squares: %.2f"
      % np.mean((regr.predict(diabetes_X_test) - diabetes_y_test) ** 2))  # 残差平方和  可以直接使用predict对测试样本预测
# Explained variance score: 1 is perfect prediction  
print('Variance score: %.2f' % regr.score(diabetes_X_test,
                                          diabetes_y_test))  # Returns the coefficient of determination R^2 of the prediction

# Plot outputs  
plt.scatter(diabetes_X_test, diabetes_y_test, color='black')
plt.plot(diabetes_X_test, regr.predict(diabetes_X_test), color='blue',
         linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()  