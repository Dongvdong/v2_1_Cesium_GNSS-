#激活环境
 
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import time
from flask import *
 
 
app = Flask(__name__)
 
import os
pathnow=os.getcwd()
pathnow=pathnow.replace('\\','/')
#print(pathnow) #获取当前工作目录路径
#print (os.path.abspath('mainPage0.html'))
 
 
 
app = Flask(
    __name__,
    template_folder='.',  # 表示在当前目录 (myproject/) 寻找模板文件
    static_folder='',     # 空 表示为当前目录 (myproject/) 开通虚拟资源入口
    static_url_path='',
)
 
  
@app.route('/')
def index():
    return render_template('index.html')
 
 
 
  
if __name__ == '__main__':
    app.run(host='0.0.0.0',port='8080')