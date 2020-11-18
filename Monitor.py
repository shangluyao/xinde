'''
监控代码：监控服务器内存，cpu,网络，磁盘等，和租车系统部署在一起
'''
from datetime import datetime
from time import sleep

import psutil

print(psutil.cpu_percent())#获取cpu信息
print(psutil.virtual_memory())#虚拟内存
print(psutil.virtual_memory().percent) #虚拟内存百分比
print(psutil.disk_usage("d:/")) #租车系统所在的磁盘
print(psutil.disk_usage("d:/").percent)# 租车系统所在磁盘的百分比
print(psutil.net_io_counters()) # 网络
print(psutil.net_io_counters().bytes_sent) #发送的字节数
print(psutil.net_io_counters().bytes_recv)# 接收的字节数

#达到类似serveragent的效果在性能测试期间获取cpu，内存趋势
# 死循环，每隔三秒，把读取的结果写到文件中测试结束分析文件，使用excel生成图表
# 时间戳， cpu% 内存% 磁盘%发送字节数，接收字节数

with open ("d:资源占用情况.txt",encoding='utf-8',mode='a') as file:
    while True:
        print("监控中.........")
        file.write(datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S") + '%\t')
        file.write(str(psutil.cpu_percent()) + '%\t')
        file.write(str(psutil.virtual_memory().percent) + '%\t')
        file.write(str(psutil.disk_usage("d:/").percent) + '%\t')
        file.write(str(psutil.net_io_counters().bytes_sent) + '%\t')
        file.write(str(psutil.net_io_counters().bytes_recv) + '%\t')
        file.flush() #从缓存刷新到文件，避免文件没关闭之前的内容一直写不进去
        sleep(3)
