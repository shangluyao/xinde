'''
比较灵活的测试前置和后置fixture
1.不受setup,teardown命名限制
2.使用灵活
'''
import pytest


# 测试前置
# 首次作用域module级别，首次调用这个fixtrue的释放执行前置，全部用例执行完，执行后置
@pytest.fixture(scope='module')#fixtrue,后无参数，默认函数级别，module是模块级
def a():# 需要前置操作时，将方法名当做参数传如用例函数
    print("系统登录")  #yield之前是前置
    yield
    print("退出登录")  #yield之后是后置

@pytest.fixture(autouse=True)
def db_op():
    print("链接数据库")
    yield
    print("断开数据库链接")

def test_001():
    print("用例1：查询操作不需要登录")

# 使用方法1：将测试前置login作为参数传入
def test_002(a):
    print("用例2：添加操作需要登录")

# 使用方法二，usefixtures使用login
@pytest.mark.usefixtures("a")
def test_003():
    print("用例3：删除操作需要登录")

