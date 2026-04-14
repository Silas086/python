import requests

def search_word(word):
    # 这是一个查词的接口地址（模拟演示）
    url = f"https://dict-mobile.iciba.com/interface/index.php?c=word&m=getsuggest&nums=1&client=6&is_new_add=1&word={word}"
    
    try:
        res = requests.get(url)
        data = res.json()
        
        # 提取释义
        meaning = data['message'][0]['paraphrase']
        print(f"【{word}】的释义是：{meaning}")
        print("-----")
        print(res.text)
    except Exception as e:
        print("查询失败，请检查网络或单词拼写")

# 运行测试
search_word('ball')
