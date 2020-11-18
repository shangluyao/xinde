'''
1.接口性能测试，比较某个接口在500ms返回
2.耗时比较久的操作默认的超时时间执行不玩，比如上传超大的文件可以设置大一点的超时时间

'''
import requests

# url = "https://tcc.taobao.com/cc/json/mobile_tel_segment.htm?tel=18629631820"
#
# for i in range(10):
#     try:
# # 0.1表示100ms
#         r = requests.get(url,timeout=0.1)
#         # HTTPSConnectionPool(host='tcc.taobao.com', port=443): Read timed out. (read timeout=0.1)
#         # 超出设定超时时间
#         print(r.status_code)
#     except Exception as e:
#         print(e)

'''
proxies代理
1.通过代理抓包，用fiddler抓自动化发的报文分析，定位问题。
2.服务器吧ip封掉了，可以通过代理换个ip
'''

proxy = {
    "http":"http://127.0.0.1:8888" , #http代理
    "https":"https://127.0.0.1:8888"#https代理
}
# 设置proxies是，需要打开代理服务器，比如iddler
r = requests.get("http://www.baidu.com",proxies=proxy)
print(r.text)
# 不加verify=False时，会校验证书，发送请求报错，设置verify=False可以不校验证书
r = requests.get("http://www.bagevent.com",proxies=proxy,verify=False)
print(r.text)