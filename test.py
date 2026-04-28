import matplotlib.pyplot as plt
import numpy as np
data = [
[150, 50],
[150, 60],
[150, 70],
[155, 70],
[160, 70],
[170, 70],
[175, 70],
[180, 70],
[175, 80],
[180, 90],
[180, 66],
[172, 55],
[175, 60]
]
data_np = np.array(data)
x = data_np[:, 0]
y = data_np[:, 1]
plt.scatter(x, y)
plt.xlabel("Height[cm]")
plt.ylabel("Weight[kg]")
plt.grid(linestyle="--")
n = data_np.shape[0]
s_xx = np.sum(x * x) / n
s_xy = np.sum(x * y) / n
s_x = np.sum(x) / n
s_y = np.sum(y) / n
a = (s_xy - s_x * s_y) / (s_xx - s_x * s_x)
b = s_y - a * s_x
y_hat = a * x + b
plt.plot(x, y_hat)
plt.scatter(180,66 ,c='r')
plt.scatter(172,55, c='r')
plt.scatter(175,60 ,c='r')
