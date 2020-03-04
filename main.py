# main file

from sklearn.metrics import mean_squared_error

import csv
import numpy as np

train = []
with open('task0_sl19d1/train.csv', 'r') as file:
    reader = csv.reader(file)
    #train = np.asarray(reader)
    for row in reader:
        print(row)

print(len(train))
#RMSE = mean_squared_error(y, y_pred)**0.5
print(train)