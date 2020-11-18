'''
pytest命名规则
1测试文件以test_开头
2.测试类以Test开头
3.测试方法以test_开头
'''
import requests

def register(data):
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    r = requests.post(url,data=data)
    return r
# 手机号格式不正确

def test_register_001():
    # 测试数据
    data = {"mobilephone":1801234,"pwd":123456}
    # 预期结果
    expect = {"status":0,"code":"20109","data":None,"msg":"手机号码格式不正确"}
    # print(json.dumps(expect)) #字典转化为json
    # 检测步骤
    real = register(data)
    # 检查结果
    assert real.json()["msg"] == expect["msg"]
    assert real.json()["code"] == expect["code"]

def test_register_002():
    data = {"mobilephone": 18012345678, "pwd": 123}
    expect = {"status":0,"code":"20108","data":None,"msg":"密码长度必须为6~18"}

    real = register(data)
    assert real.json()["msg"] == expect["msg"]
    assert real.json()["code"] == expect["code"]

def test_register_003():
    data = {"mobilephone": 18012348975, "pwd": 123456}
    expect = {"status":1,"code":"10001","data":None,"msg":"注册成功"}

    real = register(data)
    assert real.json()["msg"] == expect["msg"]
    assert real.json()["code"] == expect["code"]































