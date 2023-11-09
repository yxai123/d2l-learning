import torch

x = torch.arange(12)
print(x)
print(x.shape)
print(x.numel())

x = x.reshape(3, 4)
print(x)
x = x.reshape(-1, 4)
print(x)
x = x.reshape(3, -1)
print(x)

x = torch.zeros((2, 3, 4))
print(x)
x = torch.ones((2, 3, 4))
print(x)

x = torch.randn(3, 4)
print(x)

x = torch.tensor([[2, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])
print(x)
