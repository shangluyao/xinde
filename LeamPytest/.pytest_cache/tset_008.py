
import mock
import requests
'''
取现接口
'''
# 登录
def shi(data):
    url = "http://jy001:8081/futureloan/mvc/api/member/login"

    k =requests.post(url,data)
    return k


# 登录
def test_denglu():
    ta = {"mobilephone": 18625567780, "pwd": 1234561}
    bb = shi(ta)
    expect = {"status":1,"code":"10001","data":None,"msg":"登录成功"}
    assert bb.json()["msg"] == expect["msg"]
    assert bb.json()["code"] == expect["code"]
    print("登录成功")
# 充值
def test_chongzhi():
    ta1 = {"mobilephone": 18625567780, "amount": 10000}
    mm = requests.post("http://jy001:8081/futureloan/mvc/api/member/recharge",ta1)
    expect1 = {"status": 1, "code": "10001", "data": None, "msg": "充值成功"}
    assert mm.json()["msg"] == expect1["msg"]
    assert mm.json()["code"] == expect1["code"]
    print('充值成功')





class Encashment:

    def encashment(self,data):
        r = requests.post("http://jy001:8081/futureloan/mvc/api/member/withdraw",data=data).json()
        return r



class Testjinrong:

    def test_encashment(self):
        Ecn = Encashment()

        Ecn.encashment = mock.Mock(return_value={"status": "1", "code": "10001", "msg": "会员存在，提现成功"})
        data = {"mobilephone": "15811110001", "amount": "500"}
        r = Ecn.encashment(data)

        assert r["msg"] == "会员存在，提现成功"
        assert r["status"] == "1"
        assert r["code"] == "10001"

        print(r)
    def test_encashment2(self):

        Ecn = Encashment()

        Ecn.encashment = mock.Mock(return_value={"status":"0","code":"20117","msg":"请输入范围再0~50万之间的正数金额"})
        data = {"mobilephone":"18625567780","amount":"5000"}
        r2 = Ecn.encashment(data)
        assert r2["msg"] == "请输入范围再0~50万之间的正数金额"
        assert r2["status"] == "0"
        assert r2["code"] == "20117"
        print(r2)