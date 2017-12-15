# -*- coding: utf-8 -*-
# __author__=luhu
"""
        文件上传也是常见功能之一，上传功能webdriver并没有提供对应的方法，关键在
    于上传文件的思路。
        如果上传需要打开本地的window窗口，从窗口选择本地文件上传，webdriver就无
    能为力了，对于web页面的上传功能一般会有以下几种方式：
        普通上传：普通的附件上传都是将本地文件的路径作为一个值放入input标签中，
    通过form表单提交的时候将这个值提交给服务器，使用send_keys('path')即可。
        插件上传：一般指基于Flash与JavaScript或Ajax等技术所实现的上传功能的插件；
        三方软件上传：AutoIt实现上传，这是一个使用类似BASIC脚本语言的免费软件，他设计用于WindowsGUI
    中进行自动化操作，他利用模拟键盘按键，鼠标移动和窗口/控件的组合来实现自动化任务。安装之后在开始
    菜单中的目录如下：
        AutoIt Windows Info      用于帮助我们识别Windows控件信息
        Compile Script to.exe    用于将AutoIt生成exe执行文件
        Run Script               用于执行AutoIt脚本
        SciTE Script Editor      用于编写AutoIt脚本

        ControlFocus("打开","","Edit1")     ControlFocus()方法用于识别window窗口

        WinWait("[CLASS:#32770]", "", 10)   WinWait()设置10秒等待窗口显示，

        ControlSetText("打开", "", "Edit1", "D:\test.txt")   ControlSetText()用于向输入框中输入文件路径
        Sleep(2000)

        ControlClick("打开", "", "Button1")    点击打开按钮，提交上传的文件

        保存为upload_file.au3，通过Compile Script to.exe工具，生成exe可执行文件

        最后通过python脚本调用该程序，实现文件上传
"""
import os
from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('selenium_files/upload.html')
driver.get(file_path)    # 打开手动创建的上传文件界面
driver.find_element_by_name('file').click()    # 点击选择文件按钮，弹出Window窗口
os.system("upload_file.exe")     # 执行AutoIt脚本编译后的程序实现上传
sleep(3)                         # 默认可以填与该脚本同级目录的文件，也可以使用绝对路径
driver.quit()























