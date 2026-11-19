import json
import math

def solve_quadratic(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta > 0:
        return [(-b + math.sqrt(delta)) / (2 * a), (-b - math.sqrt(delta)) / (2 * a)]
    elif delta == 0:
        return [-b / (2 * a)]
    else:
        return []

with open("questions.json", "r", encoding="utf-8") as f:
    questions = json.load(f)

results = []
for q in questions:
    roots = solve_quadratic(q["a"], q["b"], q["c"])
    results.append({
        "equation": f"{q['a']}x²+{q['b']}x+{q['c']}=0",
        "roots": roots
    })

with open("results.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("处理完成，共", len(results), "道题，结果已写入 results.json")