import requests
import json
import time

def load_config():
    with open('config.json', 'r') as f:
        return json.load(f)

def send_wx_push(title, content, send_key):
    """
    发送微信推送通知
    使用Server酱推送服务 https://sct.ftqq.com/
    """
    url = f"https://sctapi.ftqq.com/{send_key}.send"
    data = {
        "title": title,
        "desp": content
    }
    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print("微信推送发送成功")
        else:
            print(f"微信推送发送失败: {response.text}")
    except Exception as e:
        print(f"微信推送发送异常: {str(e)}")

def check_stock():
    with open('config.json', 'r', encoding='utf-8') as f:
        config = json.load(f)
    
    # 首次运行发送绑定成功通知
    if config['wxPush']:
        title = "库存监控服务已启动"
        content = f"""
        监控服务已成功启动
        时间: {time.strftime('%Y-%m-%d %H:%M:%S')}
        监控商品数: {len(config['goodConfig'])}
        检查间隔: {config['time']}秒
        """
        send_wx_push(title, content, config['sendKey'])
    
    while True:
        print(f"\n开始检查库存 - {time.strftime('%Y-%m-%d %H:%M:%S')}")
        print("-" * 30)
        
        for item in config['goodConfig']:
            url = f"https://card.10010.com/mall-order/qryStock/v2"
            params = {
                "goodsId": item["goodsId"],
                "cityCode": item["cityCode"], 
                "mode": item["mode"]
            }
            
            try:
                response = requests.get(url, params=params)
                data = response.json()
                
                models = data.get('data', {}).get('bareMetal', {}).get('modelsList', [])
                for model in models:
                    color = model.get('COLOR_DESC', '未知')
                    version = model.get('MACHINE_VERSION_DESC', '未知')
                    stock = model.get('articleAmount', 0)
                    
                    print(f"商品颜色: {color}")
                    print(f"商品型号: {version}")
                    print(f"库存数量: {stock}")
                    
                    # 当启用微信推送且库存大于0时发送通知
                    if config['wxPush'] and stock > 0:
                        title = f"库存提醒 - 发现有货"
                        content = f"""
                        商品ID: {item['goodsId']}
                        颜色: {color}
                        型号: {version}
                        库存: {stock}
                        时间: {time.strftime('%Y-%m-%d %H:%M:%S')}
                        """
                        send_wx_push(title, content, config['sendKey'])
                
                print("-" * 30)
            except Exception as e:
                print(f"查询失败: {str(e)}")
        
        # 使用配置文件中的时间间隔
        time.sleep(config['time'])

if __name__ == "__main__":
    check_stock()
