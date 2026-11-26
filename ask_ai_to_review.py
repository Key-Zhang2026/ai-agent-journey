from ai_helper import ask_ai

# 把你刚才写的代码当作字符串传给它
my_code = """
def solve_quadratic_advanced(a, b, c):
    if a == 0:
        raise ValueError("系数 a 不能为 0")
    delta = b ** 2 - 4 * a * c
    x1 = (-b + cmath.sqrt(delta)) / (2 * a)
    x2 = (-b - cmath.sqrt(delta)) / (2 * a)
    return [x1, x2]
"""

prompt = f"你是一个资深 Python 程序员。请审查以下代码，指出它的优点，并给出两条改进建议。代码：\n{my_code}"

print("--- AI 代码审查意见 ---")
print(ask_ai(prompt))