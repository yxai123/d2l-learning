import os

import pandas
import torch

data_file = os.path.join('..', 'data', 'house_tiny.csv')
data = pandas.read_csv(data_file)

inputs, outputs = data.iloc[:, 0:2], data.iloc[:, 2]
inputs = inputs.fillna(inputs.mean(numeric_only=True))
inputs = pandas.get_dummies(inputs, dummy_na=True)

X = torch.tensor(inputs.to_numpy(dtype=float))
y = torch.tensor(outputs.to_numpy(dtype=float))
print(X, y)
