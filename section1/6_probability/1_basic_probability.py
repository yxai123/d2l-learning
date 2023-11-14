import matplotlib
import torch
from d2l import torch as d2l
from torch.distributions import multinomial

fair_probs = torch.ones([6]) / 6
print(fair_probs)

print(multinomial.Multinomial(1, fair_probs).sample())
print(multinomial.Multinomial(10, fair_probs).sample())

# 将结果存储为32位浮点数以进行除法
counts = multinomial.Multinomial(1000, fair_probs).sample()
print(counts)
print(counts / 1000)  # 相对频率作为估计值

counts = multinomial.Multinomial(10, fair_probs).sample((500,))
print(counts)
cum_counts = counts.cumsum(dim=0)
print(cum_counts)
estimates = cum_counts / cum_counts.sum(dim=1, keepdims=True)
d2l.set_figsize((6, 4.5))
for i in range(6):
    matplotlib.pyplot.plot(estimates[:, i].numpy(),
                           label=("P(die=" + str(i + 1) + ")"))
matplotlib.pyplot.axhline(y=0.167, color='black', linestyle='dashed')
matplotlib.pyplot.gca().set_xlabel('Groups of experiments')
matplotlib.pyplot.gca().set_ylabel('Estimated probability')
matplotlib.pyplot.show()
