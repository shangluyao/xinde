import requests
import openpyxl
class Jiekou:
    def zhang_hao(self,shou,mima):
        '''手机号密码'''
        zhanghao = {"mobilephone": shou, "pwd": mima}
        return  zhanghao


    def  requests_post(self,url,zhanghao):
        hui = self.requests.post(url, params=zhanghao)
        return hui
    def requests_get(self,url):
        hui = self.requests.post(url)
        return hui



class GetExcel:
    def load(self,workbook,worksheet):
        '''加载Excel文件。workbook:是工作簿路径
        worksheet:是工作表名'''
        # 打开工作簿
        book = openpyxl.load_workbook(workbook)
        # 获取指定的工作表
        sheet = book[worksheet]
        data = [tuple(cell.value for cell in row) for row in sheet]
        return data[1:]



