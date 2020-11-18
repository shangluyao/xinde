'''
上传文件，一般都是用post接口用fles参数上传

'''
import requests

url = "http://www.httpbin.org/post"
'''
files 参数：字典的格式，："name": file-tuple
file-tuple可以是 2-tuple 或 3-tuple或 4-tuple
'''
with open ("d:/test.txt",encoding="utf-8") as f:
    # "text/plain"如果上传的是一个文本文件，可以去掉content_type默认文件类型是文本文件,既不需要指定文本类型
    file = {"file1":("test.txt",f,"text/plain")}#text/plain:plain表示文件类型
    r = requests.post(url,files=file)
    print(r.text)
    # \u4e2b\u6587   unicode的编码
    print("+++++++++++++++++++++++++++")
    print(r.json())
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")

with open ("C:/Users/尚璐瑶/Desktop/123.png","rb") as f:
    file1 = {"filel":("123.png",f,"image/png")}
    r = requests.post(url,files=file1)
    print(r.text)
print("双文件+++++++++++++++++++++++++++++++++++++++++++++")

with open ("d:/test.txt",encoding="utf-8")as f:
    with open("C:/Users/尚璐瑶/Desktop/123.png", "rb") as f2:
        a = {"file1":("test.txt",f),"file2":("123.png",f2,"image/png")}
        r = requests.post(url,files=a)
        print(r.text)


