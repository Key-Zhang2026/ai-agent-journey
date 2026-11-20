import os
import math
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("ZHIPU_API_KEY"),
    base_url="https://open.bigmodel.cn/api/paas/v4/"
)

def solve_quadratic(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta > 0:
        return [(-b + math.sqrt(delta)) / (2 * a), (-b - math.sqrt(delta)) / (2 * a)]
    elif delta == 0:
        return [-b / (2 * a)]
    else:
        return []

a, b, c = 1, -3, 2
roots = solve_quadratic(a, b, c)

prompt = f"方程 {a}x²+{b}x+{c}=0 的根是 {roots}。请用高中学生能听懂的语言，解释为什么是这个结果，并说明判别式 Δ 的作用。"

response = client.chat.completions.create(
    model="glm-4-flash",
    messages=[{"role": "user", "content": prompt}]
)

print("计算结果：", roots)
print("--- AI 解析 ---")
print(response.choices[0].message.content)