import  requests

'''
发送get请求
'''
# 接口地址（"http://www.baidu.com"）
# 发送一个get请求,是收到的响应
r = requests.get("http://www.baidu.com")
#texe文本格式响应内容
print(r.text)
# 打印响应码
print(r.status_code)

# 响应描述
print(r.reason)
# 断言响应成功
assert r.reason == "OK"

# 金融项目获取用户列表
url = "http://jy001:8081/futureloan/mvc/api/member/list"
r = requests.get(url)
print(r.text)
assert r.status_code == 200
assert r.reason == 'OK'
print(r.json()['status'])
assert r.json()['status'] == 1
print(r.json()['code'])
assert r.json()['code'] == '10001'

# get请求带参数
# 1，拼接到url后面
# 2.使用params
url1 = "http://jy001:8081/futureloan/mvc/api/member/register?mobilephone=17626602345&pwd=147298990&regname='火星’"
r = requests.get(url1)

print(r.text)
print("---------------------------------")
# 2.使用params
url2 = "http://jy001:8081/futureloan/mvc/api/member/register"
canshu = {"mobilephone":"17626363497","pwd":"123456","regname":""}
r = requests.get(url2,params=canshu)
print(r.text)

# get请求带请求头 设置User-Agent,伪装成是浏览器发送的，避免服务器屏蔽自动化发的请求
url = "http://www.httpbin.org/get"#一个测试网站get是接口名字，发送的请求原封不动返回回来
r = requests.get(url)
print(r.text)
print("++++++++++++++++++++++++++")
# User-Agent 包含浏览器的版本号，操作系统的版本号等信息
tou = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}
r = requests.get(url,headers=tou)
print(r.text)
print("++++++++++++++++++++++++++++++++")

url = "https://wenku.baidu.com/view/027d607deff9aef8941e06c0.html"
r = requests.get(url,headers=tou)
print(r.text)
print("蜂群算法源代码" in r.text)







