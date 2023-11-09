import os

import pandas

data_file = os.path.join('..', 'data', 'house_tiny.csv')
data = pandas.read_csv(data_file)
print(data)

inputs, outputs = data.iloc[:, 0:2], data.iloc[:, 2]
print(inputs)
print(outputs)
inputs = inputs.fillna(inputs.mean(numeric_only=True))
print(inputs)

inputs = pandas.get_dummies(inputs, dummy_na=True)
print(inputs)
