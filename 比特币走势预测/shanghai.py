import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.tsa.arima_model import ARMA
import warnings
from itertools import product
from datetime import datetime

if __name__ == '__main__':
    warnings.filterwarnings('ignore')
    data = pd.read_csv('shanghai_1990-12-19_to_2019-2-28.csv', encoding='utf-8')
    # print(data.info())
    # print(data.head())
    data.Timestamp = pd.to_datetime(data.Timestamp)
    data.index = data.Timestamp
    data_month = data.resample('M').mean()
    # print(data_month)
    plt.subplot(211)
    plt.plot(data.Price)
    plt.subplot(212)
    plt.plot(data_month.Price)
    plt.show()
    ps = range(0,3)
    qs = range(0,3)
    parameters = product(ps, qs)
    parameters_list = list(parameters)
    best_aic = float('inf')
    result = []
    for param in parameters_list:
        try:
            model = ARMA(data_month.Price, order=(param[0],param[1])).fit()
        except ValueError:
            print('参数错误',param)
            continue
        aic = model.aic
        if aic < best_aic:
            best_model = model
            best_aic = aic
            best_param = param
        result.append([model.aic, param])
    predict_y = best_model.predict(start=0, end=348)
    predict_y = pd.DataFrame(predict_y)
    print(predict_y)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.suptitle('沪市指数(月)',fontsize=20)
    plt.plot(data_month.Price, 'r-', label='实际金额')
    plt.plot(predict_y[0], 'y--', label='预测金额')
    plt.xlabel('时间')
    plt.ylabel('沪市指数')
    plt.legend()
    plt.show()