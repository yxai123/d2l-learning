import torch

A = torch.arange(20, dtype=torch.float32).reshape(5, 4)
B = A.clone()  # 通过分配新内存，将A的一个副本分配给B
print(A)
print(A + B)

print(A * B)

a = 2
X = torch.arange(24).reshape(2, 3, 4)
print(a + X, (a * X).shape)
