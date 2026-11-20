import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("ZHIPU_API_KEY"),
    base_url="https://open.bigmodel.cn/api/paas/v4/"
)

response = client.chat.completions.create(
    model="glm-4",
    messages=[
        {"role": "user", "content": "用一句话解释什么是一元二次方程"}
    ]
)

print(response.choices[0].message.content)
