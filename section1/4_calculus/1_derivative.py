# 定义u = f(x) = 3x2 − 4x如下：
def f(x):
    return 3 * x ** 2 - 4 * x


# 通过令x = 1并让h接近0,（f(x+h)−f(x)）/h 的数值结果接近2
# 当x = 1时，导数u′是2
def numerical_lim(f, x, h):
    return (f(x + h) - f(x)) / h


h = 0.1
for i in range(5):
    print(f'h={h:.5f}, numerical limit={numerical_lim(f, 1, h):.5f}')
    h *= 0.1
