import json

question = {
    "id": 1,
    "type": "quadratic",
    "coefficients": {"a": 1, "b": -3, "c": 2},
    "answer": [2, 1]
}

# 字典 -> JSON 字符串
json_text = json.dumps(question, ensure_ascii=False, indent=2)
print("JSON 字符串：")
print(json_text)

# JSON 字符串 -> 字典
back = json.loads(json_text)
print("转回字典后取 a：", back["coefficients"]["a"])

with open("question.json", "w", encoding="utf-8") as f:
    json.dump(question, f, ensure_ascii=False, indent=2)

with open("question.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

print("从文件读回的 a：", loaded["coefficients"]["a"])