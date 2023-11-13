import torch

A = torch.arange(20, dtype=torch.float32).reshape(5, 4)
x = torch.arange(4, dtype=torch.float32)

print(A)
print(x)
print(A.shape, x.shape, torch.mv(A, x))
