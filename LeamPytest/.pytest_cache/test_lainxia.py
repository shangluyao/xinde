import pytest
import requests

def register(data):
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    r = requests.post(url,data=data)
    return r

@pytest.fixture(params=[
    {"casedata":{"mobilephone": 1801234, "pwd": 1234561},"expect":{"status":0,"code":"20109","data":None,"msg":"手机号码格式不正确"}},
    {"casedata":{"mobilephone": 18612347985, "pwd": 1234},"expect":{"status":0,"code":"20108","data":None,"msg":"密码长度必须为6~18"}},
    {"casedata":{"mobilephone": 18625567780, "pwd": 1234561},"expect":{"status":1,"code":"10001","data":None,"msg":"注册成功"}}])

def name(request):# request是固定写法

    return request.param #request.param是固定写法，取到每一组数据



def test_register_001(name):
    # 测试数据
    data = name.get("casedata")
    # 预期结果
    expect = name.get("expect")
    # print(json.dumps(expect)) #字典转化为json
    # 检测步骤
    real = register(data)
    # 检查结果
    assert real.json()["msg"] == expect["msg"]
    assert real.json()["code"] == expect["code"]




