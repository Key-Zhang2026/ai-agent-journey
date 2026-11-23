import math
from ai_helper import ask_ai

def solve_quadratic(a, b, c):
    if a == 0:
        return None
    delta = b ** 2 - 4 * a * c
    if delta > 0:
        return [(-b + math.sqrt(delta)) / (2 * a), (-b - math.sqrt(delta)) / (2 * a)]
    elif delta == 0:
        return [-b / (2 * a)]
    else:
        return []

a = float(input("请输入 a："))
b = float(input("请输入 b："))
c = float(input("请输入 c："))

roots = solve_quadratic(a, b, c)

if roots is None:
    print("a 不能为 0，这不是一元二次方程。")
elif len(roots) == 0:
    print("方程无实数根。")
    print("--- AI 解析 ---")
    print(ask_ai(f"方程 {a}x²+{b}x+{c}=0 无实数根，请用高中生能懂的话解释原因。"))
else:
    print("方程的根：", roots)
    print("--- AI 解析 ---")
    print(ask_ai(f"方程 {a}x²+{b}x+{c}=0 的根是 {roots}，请用高中生能懂的话解释求解过程。"))