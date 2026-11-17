scores = [85, 92, 78, 60, 45]
print("全班分数：", scores)
print("第一个分数：", scores[0])
print("最后一个分数：", scores[-1])
print("一共有几个人：", len(scores))
scores.append(99)
print("追加后：", scores)
scores[0] = 88
print("修改后：", scores)