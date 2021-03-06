'''
mark标记
1.skip:这个版本有缺陷，导致某个用例执行不通过，可以跳过这个用例等缺陷修复后，在放开执行
2.自定义标记：
    随着代码规模增大，功包含能测试，接口测试，性能测试，冒烟测试，只想执行接口测试的用例怎么挑选用例
'''
import pytest
def test_case1():
    print("测试用例1")

@pytest.mark.skip(reason="有缺陷。缺陷号为158634665，待缺陷解决后在执行")
@pytest.mark.maoyan
def test_case2():
    print("测试用例2")

@pytest.mark.maoyan
def test_case3():
    print("测试用例3")

def test_case4():
    print("测试用例4")

 #  放在类上面，对类里面的每个方法生效
@pytest.mark.api
class TestUserMark:
    @pytest.mark.maoyan
    def test_case5(self):
        print("测试用例5")

    def test_case6(self):
        print("测试用例6")

    def test_case7(self):
        print("测试用例7")
