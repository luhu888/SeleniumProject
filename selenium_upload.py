# -*- coding: utf-8 -*-
# __author__=luhu
"""
        文件上传也是常见功能之一，上传功能webdriver并没有提供对应的方法，关键在
    于上传文件的思路。
        如果上传需要打开本地的window窗口，从窗口选择本地文件上传，webdriver就无
    能为力了，对于web页面的上传功能一般会有以下几种方式：
        普通上传：普通的附件上传都是将本地文件的路径作为一个值放入input标签中，
    通过form表单提交的时候将这个值提交给服务器，使用send_keys('path')即可。
        插件上传：一般指基于Flash与JavaScript或Ajax等技术所实现的上传功能的插件。
"""

























