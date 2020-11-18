'''
fixture  可以带参数和返回值
'''

# 测试前置：用来准备测试数据，在测试用例中使用测试数据。测试数据使用fixture的返回值
import pytest


@pytest.fixture()
def username_pwd():# 这个函数名可以作为变量使用
    return {"username":"root","pwd":123456}#可以返回任意类型

def test_login(username_pwd):
    print("测试数据为:{username_pwd['pwd']}") #f是将其格式化，可以将里面的内容当做变量使用
    print("测试数据为:",{username_pwd['pwd']}) #不写f就用这种方式写

# 相同的测试用例，只是每次输入的数据不同，就是分别用几组数据测同一组测试用例
@pytest.fixture(params=['root','admin','administrator','12323'])#多组用户名
def data(request):# request是固定写法
    return request.param #request.param是固定写法，取到每一组数据

def test_login2(data):
    print("使用用户名{data}测试登录功能")

@pytest.fixture(params=[{"casedata":'root',"expect":"成功"},{"casedata":'admin',"expect":"成功"}])#多组用户名
def data1(request):# request是固定写法
    return request.param #request.param是固定写法，取到每一组数据

def test_login3(data1):
    print("使用用户名{data1}测试登录功能")

def test_login4(data1):
    print("使用用户名{data1['casedata']}测试登录功能，预期结果为{data1['expect']}")
