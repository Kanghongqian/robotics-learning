import numpy as np
import matplotlib.pyplot as plt

# 连杆长度
L1 = 10
L2 = 7

# 角度（单位：度）
theta1 = 45
theta2 = 30

# 转弧度
t1 = np.radians(theta1)
t2 = np.radians(theta2)

# 第一关节位置
x1 = L1 * np.cos(t1)
y1 = L1 * np.sin(t1)

# 末端位置
x2 = x1 + L2 * np.cos(t1 + t2)
y2 = y1 + L2 * np.sin(t1 + t2)

print("Joint 1 Position:", (x1, y1))
print("End Effector Position:", (x2, y2))

# 可视化
plt.plot([0, x1], [0, y1], marker='o')
plt.plot([x1, x2], [y1, y2], marker='o')

plt.xlim(-20, 20)
plt.ylim(-20, 20)

plt.grid()
plt.axis('equal')

plt.title("2-Link Robot Arm Forward Kinematics")

plt.show()