import math

def solve_quadratic(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return [x1, x2]
    elif delta == 0:
        x = -b / (2 * a)
        return [x]
    else:
        return []

result1 = solve_quadratic(1, -3, 2)
print("方程 1 的根：", result1)

result2 = solve_quadratic(1, 2, 1)
print("方程 2 的根：", result2)

result3 = solve_quadratic(1, 0, 1)
print("方程 3 的根：", result3)