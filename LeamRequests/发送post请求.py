'''
发送post请求
    使用data传表单格式参数
    使用json传json格式参数
    带请求头使用headers
'''
import  requests
# 发送post请求，带参数可以使用data或json来传参，具体使用哪个要看系统是怎么实现的
# 上一步注册成功的手机后，验证登录，登录使用post
# url = "http://jy001:8081/futureloan/mvc/api/member/login?mobilephone=17626602345&pwd=147298990"
#
# r = requests.post(url)
# print(r.text)
url = "http://jy001:8081/futureloan/mvc/api/member/login"
mm = {"mobilephone":"17626602345","pwd":"147298990"}
r = requests.post(url,params=mm)
print(r.text)

r = requests.post(url,data=mm)
print(r.text)


r = requests.post(url,json=mm)
print(r.text)

# 发送请求到httpbin,观察区别
r = requests.post("http://www.httpbin.org/post",data=mm)
print(r.text)
print("+++++++++++++++++++++++++++++++++++++++++++++")
r = requests.post("http://www.httpbin.org/posh",json=mm)
print(r.text)
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

tou = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}
r = requests.get("http://www.httpbin.org/posh",headers=tou,data = mm)
print(r.text)
