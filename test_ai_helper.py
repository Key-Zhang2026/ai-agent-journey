from ai_helper import ask_ai

print("测试 1：正常提问")
print(ask_ai("用一句话解释什么是判别式"))
print()

print("测试 2：故意传空字符串")
print(ask_ai(""))