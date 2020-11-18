'''
任务集合,分层管理，按模块，子系统来管理
'''
from locust import TaskSet, task, HttpUser, between


class SystemManage(TaskSet):
    @task
    def task1(self):
        self.client.get("/carRental/sys/toUserManager.action")
    @task
    def task2(self):
        self.client.get("/carRental/sys/toRoleManager.action")
    @task(8)
    def task3(self):
        self.client.get("/carRental/sys/toLogInfoManager.action")

class BasicManage(TaskSet):
    @task
    def task1(self):
        self.client.get("/carRental/bus/toCustomerManager.action")

    @task
    def task2(self):
        self.client.get("/carRental/bus/toCarManager.action")

class CarRentalTest(HttpUser):
    wait_time = between(1,3) #任务之间的间隔时间
    # tasks = [BasicManage,SystemManage] #任务集合tasks是user中定义的属性不能写错
    tasks = {BasicManage:4,SystemManage:1}#任务集合后面数字表示权重，四个用户
    # 访问BasicManage一个用户访问SystemManage
    def on_start(self):#测试前置 ,登录
        user = {"loginname":"admin","pwd":"123456"}
        self.client.post("/carRental/login/login.action")
    def on_stop(self):
        self.client.post("/carRental/logout/logout.action")

# -f 要执行的文件

#Web-port locust Web 页面访问的端口
# locust -f locust_test2.py --host=http://127.0.0.1:8080 --Web-host=127.0.0.1  --web-port=8088
# 输入locust -f locust_test2.py（文件名）后，点击网址，在跳转的Web端，将0.0.0.0改为localhost回环地址，
#
