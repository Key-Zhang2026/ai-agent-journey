import os
from openai import OpenAI, AuthenticationError, APIConnectionError, RateLimitError

def _create_client():
    api_key = os.getenv("ZHIPU_API_KEY")
    if not api_key:
        return None
    return OpenAI(
        api_key=api_key,
        base_url="https://open.bigmodel.cn/api/paas/v4/"
    )

client = _create_client()

def ask_ai(prompt):
    if client is None:
        return "错误：没有读到环境变量 ZHIPU_API_KEY。请检查环境变量设置，并重启 VS Code 和终端。"
    try:
        response = client.chat.completions.create(
            model="glm-4-flash",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except AuthenticationError:
        return "错误：API Key 无效。请检查 Key 是否正确、是否已过期。"
    except APIConnectionError:
        return "错误：网络连接失败。请检查网络后重试。"
    except RateLimitError:
        return "错误：请求太频繁或免费额度用完了。等一会儿再试。"
    except Exception as e:
        return f"未知错误：{e}"