'''
fixture作用域
默认是function级别的，有function（方法),module（模块）,class（类),session(跨文件)级别
'''
import pytest
@pytest.fixture(scope='class') #每个类调用一次，在类中首次调用fixture的时候执行前置，类里方法执行完后执行置
def login():
    print('登录系统')#前置
    yield
    print('退出登录')#后置

class TestQuery():
    def test_case1(self):
        print("测试查询1")
    def test_case2(self,login): #执行前置
        print("测试查询2")
    def test_case3(self): #3执行完后执行后置
        print("测试查询3")

class TestDeletr():
    def test_case1(self,login): #执行前置
        print('测试删除1')
    def test_case2(self):
        print('测试删除2')
    def test_case3(self):#执行完后执行后置
        print('测试删除3')