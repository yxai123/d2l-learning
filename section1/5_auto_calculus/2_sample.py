import torch

x = torch.arange(4.0)
print(x)

x.requires_grad_(True)  # 等价于x=torch.arange(4.0,requires_grad=True)
x.grad  # 默认值是None
print(x.grad)

y = x * x
u = y.detach()
z = u * x

z.sum().backward()
print(x.grad)
print(x.grad == u)

x.grad.zero_()
y.sum().backward()
print(x.grad)
print(x.grad == 2 * x)
