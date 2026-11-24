print("=== 高中数学 AI 助教 v0.1 ===")
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

    # 这里先占位，看看框架能不能跑通
    print(f"【模拟回复】我收到了你的问题：{user_input}\n")