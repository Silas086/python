import ollama

client = ollama.Client(host = "http://localhost:11434")

#response:dict类型
while True:
    a = input("Enter:")
    response = client.chat(
        model = 'deepseek-r1:32b',
        messages = [{"role":"user","content":a}]  
    )
    print(response['message']['content'])