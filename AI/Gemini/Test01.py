#显式提供 API 密钥
from google import genai

client = genai.Client(api_key="AIzaSyAATtlkMCe7B9qMDwwijx3BWJp-CtEaDY8")

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="hi"
)

print(response.text)