import math

def solve_quadratic(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return [x1, x2]
    elif delta == 0:
        return [-b / (2 * a)]
    else:
        return []

with open("equations.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

with open("result.txt", "w", encoding="utf-8") as out:
    for line in lines:
        parts = line.strip().split()
        if len(parts) != 3:
            continue
        a = float(parts[0])
        b = float(parts[1])
        c = float(parts[2])
        roots = solve_quadratic(a, b, c)
        out.write(f"方程 {a}x²+{b}x+{c}=0 的根：{roots}\n")

print("处理完成，结果已写入 result.txt")