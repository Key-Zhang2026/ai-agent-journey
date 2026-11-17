import math

equations = [
    (1, -3, 2),
    (1, 2, 1),
    (1, 0, 1),
    (2, -4, -6),
]

for a, b, c in equations:
    print("--- 方程：", a, "x² +", b, "x +", c, "= 0")
    delta = b ** 2 - 4 * a * c

    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("两个实根：x1 =", x1, "x2 =", x2)
    elif delta == 0:
        x = -b / (2 * a)
        print("一个实根：x =", x)
    else:
        print("无实数根")
    print()