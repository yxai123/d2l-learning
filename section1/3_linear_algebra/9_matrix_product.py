import torch

A = torch.arange(20, dtype=torch.float32).reshape(5, 4)
B = torch.ones(4, 3)

print(A)
print(B)

print(torch.mm(A, B))
