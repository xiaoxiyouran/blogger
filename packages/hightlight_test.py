#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re;

if __name__=='__main__':
    s = "i say, hello== world!o== "
    findList = [m.start() for m in re.finditer('==', s)]
    ll = s.split("==")
    newString = ''
    initPos = 0
    while len(findList) >0 and len(findList) != 1:
        first = findList[0];
        second = findList[1];
        newString += s[initPos:first] + '<mark>' + s[first+2:second] + '</mark>' ; #+ s[second + 2: ]
        initPos = second +2;
        findList.pop(0)  # 前面已经弹出去了一个，下一个就在最前面
        findList.pop(0)
    print newString + s[initPos:];  # 即使没有==，也能把原值s赋给它。
    # ll = s.split("==")
    # print ll
    # print s.find("==")
    # newString = ''
    # for i in range(len(ll)):
    #     if s.find("==") == 0:
    #         print

