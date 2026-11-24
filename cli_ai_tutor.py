from ai_helper import ask_ai

print("=== 高中数学 AI 助教 v1.0 ===")
print("输入数学问题，我会尝试解答。输入 exit 退出。\n")

while True:
    user_input = input("你的问题：")
    user_input = user_input.strip()

    if user_input.lower() == "exit":
        print("助教已退出，再见！")
        break

    if not user_input:
        print("（你什么都没输入，请重新输入）\n")
        continue

    print("\n--- AI 正在思考 ---")
    prompt = f"你是一个亲切的高中数学助教。请用高一学生能听懂的语言解答：{user_input}"
    answer = ask_ai(prompt)
    print(answer)
    print("\n" + "=" * 30 + "\n")