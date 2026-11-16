import math

a = float(input("请输入二次项系数 a："))
b = float(input("请输入一次项系数 b："))
c = float(input("请输入常数项 c："))

if a == 0:
    print("a 不能为 0，这不是一元二次方程。")
else:
    delta = b ** 2 - 4 * a * c
    print("判别式 Δ =", delta)

    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("方程有两个不相等的实根：")
        print("x1 =", x1)
        print("x2 =", x2)
    elif delta == 0:
        x = -b / (2 * a)
        print("方程有两个相等的实根：x =", x)
    else:
        print("方程没有实数根。")