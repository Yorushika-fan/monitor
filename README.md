# 商品监控系统

## 项目简介

联通商城天猫精灵，摄像头，路由器 库存监控通知

## 配置说明

### config.json 配置项

```json
{
"goodConfig":[
        {
            "goodsId": "994210179230",
            "cityCode": "110",
            "mode": "1"
        },    
        {
            "goodsId": "994211139173",
            "cityCode": "110",
            "mode": "1"
        },
        {
            "goodsId": "994210179247",
            "cityCode": "110",//不用改
            "mode": "1"
        },
]
"time": 10, // 监控间隔时间（秒）
"wxPush": true, // 是否启用微信推送
"sendKey": "xxx" // Server酱推送密钥
}
```

- **time**: 监控时间间隔，单位为秒
- **wxPush**: 是否开启微信推送通知
- **sendKey**: Server 酱推送服务的密钥

## 使用方法

1. 下载exe文件和config放在同一目录下
2. 根据需求修改配置文件
3. 运行程序开始监控

## 微信推送配置

1. 访问 [Server 酱](https://sct.ftqq.com/) 获取推送密钥
2. 将获取到的密钥填入 config.json 的 sendKey 字段
3. 将 wxPush 设置为 true 开启推送

## 注意事项

- 请合理设置监控间隔时间，避免请求过于频繁
- 请妥善保管 Server 酱 的推送密钥
