import torch

u = torch.tensor([3.0, -4.0])
print(torch.norm(u))

print(torch.abs(u).sum())

print(torch.ones((4, 9)))
print(torch.norm(torch.ones((4, 9))))
