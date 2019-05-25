from sklearn.datasets import load_boston
from sklearn.ensemble import AdaBoostRegressor
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == "__main__":
    data = load_boston()
    print(data.keys())
    train_x, test_x, train_y, test_y = train_test_split(data.data, data.target, test_size=0.3)
    mses = []
    for n in range(1,200):
        regressor = AdaBoostRegressor(n_estimators=n)
        regressor.fit(train_x, train_y)
        predict_y = regressor.predict(test_x)
        mse = mean_squared_error(test_y, predict_y)
        # print('均方误差 = ', round(mse, 2))
        mses.append(round(mse, 2))
    plt.plot(range(1,200), mses)
    plt.show()

    # dtc_regressor = DecisionTreeRegressor()
    # dtc_regressor.fit(train_x, train_y)
    # predict_dtr = dtc_regressor.predict(test_x)
    # mse = mean_squared_error(test_y, predict_dtr)
    # print('决策树均方误差 = ', mse)
    #
    #
    # knn_regressor = KNeighborsRegressor()
    # knn_regressor.fit(train_x, train_y)
    # predict_knr = knn_regressor.predict(test_x)
    # mse = mean_squared_error(test_y, predict_knr)
    # print('KNN均方误差 = ', mse)