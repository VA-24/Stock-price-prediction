import numpy as np
import pandas as pd
from sklearn import linear_model
import sklearn


stock_csv = ['WMT.csv', 'TSLA.csv', 'BA.csv', 'AAPL.csv']

for i in range (len(stock_csv)):
    data = pd.read_csv(stock_csv[i])
    data = data[["1. open", "2. high", "3. low", "4. close", "5. volume"]]
    print(data.head())

    predict = "4. close"

    x = np.array(data.drop([predict], 1))
    y = np.array(data[predict])
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = 0.1)


    linear = linear_model.LinearRegression()

    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)
    print(acc)


    print('Coefficient: ', linear.coef_)
    print('Intercept: ', linear.intercept_)

    predictions = linear.predict(x_test)

    for x in range(len(predictions)):
        print(predictions[x], x_test[x], y_test[x])


