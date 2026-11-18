with open("test.txt", "w", encoding="utf-8") as f:
    f.write("第一行\n")
    f.write("第二行\n")

with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()

print("文件内容：")
print(content)

with open("test.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

for line in lines:
    print("读到：", line.strip())