#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
useage: python -W all generate_index.py doc
一些常用的工具插件
'''
import locale
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
print sys.getdefaultencoding()      # ascii
print locale.getdefaultlocale()[1]  # cp936

import  platform
print  platform.system()

