import requests

def get_word():
    url = "http://open.iciba.com/dsapi/"
    try:
        r = requests.get(url)
        data = r.json()
        # 提取英文、中文、图片
        content = data['content'] #英文
        note = data['note'] #中文
        img_url = data['picture2'] # 每日一句自带的图片
        return content, note, img_url
    except:
        return "Keep on going."

def send_pushplus(token, content, note, img_url):
    url = "http://www.pushplus.plus/send"
    
    # 构造推送内容
    body = f"""
    <h3>每日英语单词</h3>
    <p style='color:#1e88e5; font-size:18px;'><b>{content}</b></p>
    <p style='color:#555;'>{note}</p>
    <img src='{img_url}' style='width:100%; border-radius:8px;' />
    <br><br>
    <p style='font-size:12px; color:#999;'>推送时间：来自我的单词机器人</p>
    """
    
    data = {
        "token": token,
        "title": "Morning!",
        "content": body,
        "template": "html"  
    }
    
    response = requests.post(url, json=data)
    print(f"发送状态: {response.text}")

if __name__ == "__main__":
    MY_TOKEN = "07cbd2c2f104401181411bdcc956c85c"
    
    word_en, word_cn, img = get_word()
    send_pushplus(MY_TOKEN, word_en, word_cn, img)