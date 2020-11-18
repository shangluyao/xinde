import pytest
import requests
def register(data):
    url = "http://jy001:8081/futureloan/mvc/api/member/login"
    r = requests.post(url,data)
    return r

@pytest.fixture(params=[
{"casedata":{"mobilephone": None, "pwd": 1234561},"expect":{"status":0,"code":"20103","data":None,"msg":"手机号不能为空"}},
    {"casedata":{"mobilephone": 18612347985, "pwd":None},"expect":{"status":0,"code":"20103","data":None,"msg":"密码不能为空"}},
    {"casedata":{"mobilephone": 18625567780, "pwd":123},"expect":{"status":0,"code":"20111","data":None,"msg":"用户名或密码错误"}},
    {"casedata":{"mobilephone": 18625567569, "pwd":1234561},"expect":{"status":0,"code":"20111","data":None,"msg":"用户名或密码错误"}},
    {"casedata":{"mobilephone": 18625567780, "pwd": 1234561},"expect":{"status":1,"code":"10001","data":None,"msg":"登录成功"}}])

def name(request):
    return request.param





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