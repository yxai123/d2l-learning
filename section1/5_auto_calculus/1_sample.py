import torch

# 求导必须是浮点型，必须加.
x = torch.arange(4.0)
print(x)

x.requires_grad_(True)  # 等价于x=torch.arange(4.0,requires_grad=True)
x.grad  # 默认值是None
print(x.grad)

# x是一个长度为4的向量，计算x和x的点积，得到了我们赋值给y的标量输出
y = 2 * torch.dot(x, x)
print(y)

# 调用反向传播函数来自动计算y关于x每个分量的梯度，并打印这些梯度。
y.backward()
print(x.grad)

print(x.grad == 4 * x)

x.grad.zero_()
y = x.sum()
y.backward()
print(x.grad)
