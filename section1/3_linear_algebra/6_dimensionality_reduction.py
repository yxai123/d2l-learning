import torch

x = torch.arange(4, dtype=torch.float32)
print(x, x.sum())

A = torch.arange(20, dtype=torch.float32).reshape(5, 4)
print(A)
print(A.shape, A.sum())

A_sum_axis0 = A.sum(axis=0)
print(A_sum_axis0, A_sum_axis0.shape)

A_sum_axis1 = A.sum(axis=1)
print(A_sum_axis1, A_sum_axis1.shape)

print(A.sum(axis=[0, 1]))

print(A.mean(), A.sum() / A.numel())
print(A.mean(axis=0), A.sum(axis=0) / A.shape[0])

sum_A = A.sum(axis=1, keepdims=True)
print(sum_A)
print(A / sum_A)
print(A.cumsum(axis=0))
