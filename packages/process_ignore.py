#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
useage: python -W all generate_index.py doc
'''

import sys
reload(sys)

import warnings
import locale
import os
import platform

def ignore(filename):
    res = []
    file = open(filename)

    while 1:
        lines = file.readlines(100000)
        if not lines:
            break
        for line in lines:
            line = line.strip()                     # 去除首位的空格空行等
            line = line.strip('\n')                 # 去除末尾的换行符
            if line:                                # 跳过空行，读进为 空的串
                # index = 0;
                # while line[index].isspace():        # 判断单个字符或者整个字符串是否为空格
                #     index = index + 1
                #     if index >= len(line):          # 类似于 '\n' 非空，但直到数组溢出都是空的
                #         continue
                #
                # tmpLine = line[index:]              # 出去开头的空白 后的字符串
                if line[0] == '#':
                    continue;                       # 跳过注释
                line = line.rstrip(os.path.sep)                   # 如果是目录，需要跳过 末尾的反斜杠
                res.append(line)

    return res

if __name__=='__main__':
    print ignore(".mdignore")

