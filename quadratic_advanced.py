import cmath
from ai_helper import ask_ai

def solve_quadratic_advanced(a, b, c):
    if a == 0:
        # 主动抛出错误
        raise ValueError("系数 a 不能为 0，这不是一元二次方程！")
    
    delta = b ** 2 - 4 * a * c
    # 用 cmath.sqrt，无论 delta 正负都能算
    x1 = (-b + cmath.sqrt(delta)) / (2 * a)
    x2 = (-b - cmath.sqrt(delta)) / (2 * a)
    return [x1, x2]

# --- 测试区 ---
print("=== 测试 1：正常的实数根 ===")
try:
    roots1 = solve_quadratic_advanced(1, -3, 2)
    print("方程的根：", roots1)
except ValueError as e:
    print("发生错误：", e)

print("\n=== 测试 2：无实数根（复数根） ===")
try:
    roots2 = solve_quadratic_advanced(1, 0, 1)
    print("方程的根：", roots2)
    print("--- AI 解析 ---")
    print(ask_ai(f"方程 x²+1=0 的根是 {roots2}，请给高中生简单解释一下什么是复数根。"))
except ValueError as e:
    print("发生错误：", e)

print("\n=== 测试 3：故意输入 a=0 ===")
try:
    roots3 = solve_quadratic_advanced(0, 2, 1)
    print("方程的根：", roots3)
except ValueError as e:
    print("发生错误：", e)