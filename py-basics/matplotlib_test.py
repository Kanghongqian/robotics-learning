import math

print("=== Mechanical Engineering Calculator ===")

# 圆面积计算
radius = float(input("Input radius (mm): "))

area = math.pi * radius ** 2

print(f"Circle Area = {area:.2f} mm²")

# 圆周长计算
circumference = 2 * math.pi * radius

print(f"Circumference = {circumference:.2f} mm")