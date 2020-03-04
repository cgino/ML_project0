# main file

from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression

import csv
import numpy as np

train = []
with open('task0_sl19d1/train.csv', 'r') as file:
    reader = csv.reader(file)
    #train = np.asarray(reader)
    for row in reader:
        train.append(row)

print(len(train))
print(train[0])

train_data = np.asarray(train)
print(train_data.shape)
y = train_data[:,1]
X = train_data[:,2:]

reg = LinearRegression().fit(X[1:,:], y[1:])

print(y[0:5])
print(X[0])
print(reg.score)

#RMSE = mean_squared_error(y, y_pred)**0.5
#print(train)