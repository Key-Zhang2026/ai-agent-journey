student = {
    "name": "小明",
    "score": 85,
    "class": "高二3班"
}

print("姓名：", student["name"])
print("分数：", student["score"])
print("班级：", student["class"])

student["score"] = 92
student["email"] = "xiaoming@example.com"
print(student)