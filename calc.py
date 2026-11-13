import math

x1 = float(input("请输入 A 点 x 坐标："))
y1 = float(input("请输入 A 点 y 坐标："))
x2 = float(input("请输入 B 点 x 坐标："))
y2 = float(input("请输入 B 点 y 坐标："))

d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print("A、B 两点间的距离是：", d)