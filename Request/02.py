import requests
import json

def get_weather(city_id, api_key,host):
    """
    :param city_id: 城市代码(例如上海是 101020100)
    :param api_key: 在天气服务商官网申请的密钥
    """
    base_url = f"https://{host}/v7/weather/now"

    query_params = {
        "location": city_id,
        "key": api_key,
        "lang": "en",  #中文是zh
        "unit": "m"    #单位制,如华氏度和摄氏度
    }

    try:
        response = requests.get(base_url, params=query_params, timeout=10)
        
        # 检查网络状态（如果是200才继续）
        response.raise_for_status() 
        
        data = response.json()
        if data['code'] == '200':
            now = data['now']
            temp = now['temp']         # 温度
            text = now['text']         # 天气现象（如 Sunny, Cloudy）
            wind = now['windDir']      # 风向
            humidity = now['humidity'] # 湿度

            print(f"--- Weather Report ---")
            print(f"Condition: {text}")
            print(f"Temperature: {temp}°C")
            print(f"Humidity: {humidity}%")
            print(f"Wind Direction: {wind}")
            print(f"----------------------")
        else:
            print(f"Error from API: {data['code']} (Please check your API Key or City ID)")

    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")

MY_KEY = "fdf8d94c1da04094a720a8300a01fb8f" 
MY_HOST = "m73aaqrn72.re.qweatherapi.com"
get_weather("101020100", MY_KEY, MY_HOST)#101020100是上海城市代码