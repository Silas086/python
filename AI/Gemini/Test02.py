import os
from google import genai

# 必须加上这两行配置代理，否则连不上 Google
# 如果你的梯子端口不是 7890，请改成你自己的端口（比如 1080, 1087 等）
os.environ['http_proxy'] = 'http://127.0.0.1:7897'
os.environ['https_proxy'] = 'http://127.0.0.1:7897'

# 初始化客户端
client = genai.Client(api_key="AIzaSyAATtlkMCe7B9qMDwwijx3BWJp-CtEaDY8")

print("正在获取模型列表...")

try:
    # 获取列表
    for m in client.models.list():
        # 打印所有包含 "gemini" 的模型名字
        if "gemini" in m.name:
            print(m.name)
            
except Exception as e:
    print(f"连接依然失败，请检查代理端口是否正确。错误详情: {e}")