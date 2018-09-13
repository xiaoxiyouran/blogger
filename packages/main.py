#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
useage: python -W all main.py src docs
'''

import sys
import warnings
reload(sys)
sys.setdefaultencoding('utf-8')
import os
import  re

import shutil
import time

sys.path.append('markdown');
from markdown import __main__

import generate_index
from generate_index import generate_index
from process_mermaid import process_mermaid
from process_highlight import  process_highlight
from process_ignore import  ignore

def file_put_contents(relative_file_name, html):
    with open(relative_file_name,'w') as f:
        f.writelines(html); # 大概一次写入200M 的文件



def outBytemplate(template,outputFileName,markdown):
    # print template
    fRead = open(template,'r');
    fWrite = open(outputFileName,'w')
    # print markdown
    for s in fRead.readlines():
        s = s.replace('$title$',markdown['title'])
        s = s.replace('$base_url$',markdown['base_url'])
        s = s.replace('$html$',markdown['html'])
        fWrite.writelines(s)
    fRead.close()
    fWrite.close()


def find_lcsubstr(s1, s2):
    '''
    找最长公共子串
    :param s1:
    :param s2:
    :return:
    '''
    m = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]  # 生成0矩阵，为方便后续计算，比字符串长度多了一列
    mmax = 0  # 最长匹配的长度
    p = 0  # 最长匹配对应在s1中的最后一位
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                m[i + 1][j + 1] = m[i][j] + 1
                if m[i + 1][j + 1] > mmax:
                    mmax = m[i + 1][j + 1]
                    p = i + 1
    return s1[p - mmax:p], mmax  # 返回最长子串及其长度


# print find_lcsubstr('abcdfg', 'abdfg')

def default_template(output_base_url_copy, markdown):
    '''

    :param output_base_url_copy: ../mydocs/aa
    :param markdown: {
    output_file: ../mydocs/aa/newDir/testMe.html
    }
    :return:
    '''
    # [common_str,length] = find_lcsubstr(markdown['input_file'],markdown['output_file'])     # 找../src/aa/newDir/testMe.md  和 ../mydocs/aa/newDir/testMe.html 的公共子串
    # nPos = markdown['output_file'].find(common_str)
    #
    # output =  markdown['output_file']
    related_to_sidebar =  markdown['output_file'].count(os.path.sep) -\
            output_base_url_copy.count(os.path.sep) - 1

    related_to_sidebar_str = ' '
    for i in range(related_to_sidebar):
        related_to_sidebar_str = related_to_sidebar_str + '../'     # 相对当前的一级目录返回上一级



    html_header = '''
<!DOCTYPE html>
<html>
<head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">

        <title>$title$</title>
        <meta name="keywords" content="xiaoxiyouran" />
        <meta name="description" content="xiaoxiyouran's Docs" />
        <link href="$base_url$/packages/css/bootstrap.min.css" rel="stylesheet" />
        <link href="$base_url$/packages/css/style.css" rel="stylesheet" />
        <link href="$base_url$/packages/css/monokai_sublime.min.css" rel="stylesheet">

        <!-- 右上角的侧边导航栏 -->
        <link rel="stylesheet" href="$base_url$/packages/hock_side_bar/css/sidebar.css"> <!--初始化文件-->
        <script src="$base_url$/packages/hock_side_bar/js/sidebar.js"></script> <!--rem适配js-->

        <!--
        <link href="<?php echo $base_url?>/css/bootstrap-theme.min.css" rel="stylesheet" />
        -->

        <!-- To generate the side tree of the document itself. -->
  <link rel="stylesheet" href="$base_url$/packages/generate_header_sidebar/css/zTreeStyle/zTreeStyle.css" type="text/css">
  <style>
  body {
  background-color: white;
  margin:0; padding:0;
  // text-align: center;
  overflow: scroll;
  }
  div, p, table, th, td {
    list-style:none;
    margin:8px; padding:0;
    color:#333; font-size:12px;
   Font-family: Helvetica, Tahoma, Arial, STXihei, “华文细黑”, “Microsoft YaHei”, “微软雅黑”, SimSun, “宋体”, Heiti, “黑体”, sans-serif;
  }

 // table{
 //   border-collapse:collapse;
 // }

  //table, td, th{
  //  border:1px solid black;
  //}

  .ztree li a.curSelectedNode {
    padding-top: 0px;
    background-color: #FFE6B0;
    color: black;
    height: 16px;
    border: 1px #FFB951 solid;
    opacity: 0.8;
  }
  .ztree{
    overflow: auto;
    height:100%;
    min-height: 200px;
    top: 0px;
  }
  </style>

<!--
  For Latex formula
-->
<!--
  <script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {inlineMath: [["$","$"],["\\(","\\)"]]}
  });
</script>
-->
 <script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {inlineMath: [["$","$"]]}
  });
</script>
 <script type="text/javascript" src="$base_url$/packages/MathJax/MathJax.js?config=TeX-AMS_HTML-full"></script>

<!-- mermaid 画图 -->
 <link rel="stylesheet" href="$base_url$/packages/mermaid-7.0.0/dist/mermaid.forest.css"/>
 <script src="$base_url$/packages/mermaid-7.0.0/dist/mermaid.js"></script>
<!--  <script src="$base_url$/packages/mermaid-7.0.0/dist/mermaid.full.js"></script> -->
 <!-- <scrpt src="$base_url$/packages/mermaid-7.0.0/node_modules/d3/d3.js"></scrpt> -->
 <!-- <script>mermaid.initialize({startOnLoad:true});</script>  -->
 <script>
        //browserify --entry src/mermaid.js -u d3 -o ./dist/mermaid.brow.slim.js
                        var mermaid_config = {
                                        startOnLoad:true
                        }
                        mermaid.ganttConfig = {
                                        titleTopMargin:25,
                                        barHeight:20,
                                        barGap:4,
                                        topPadding:50,
                                        leftPadding:75,
                                        gridLineStartPadding:35,
                                        fontSize:11,
                                        numberSectionStyles:3,
                                        axisFormatter: [
                                                        // Within a day
                                                        ["%I:%M", function (d) {
                                                                        return d.getHours();
                                                        }],
                                                        // Monday a week
                                                        ["w. %U", function (d) {
                                                                        return d.getDay() == 1;
                                                        }],
                                                        // Day within a week (not monday)
                                                        ["%a %d", function (d) {
                                                                        return d.getDay() && d.getDate() != 1;
                                                        }],
                                                        // within a month
                                                        ["%b %d", function (d) {
                                                                        return d.getDate() != 1;
                                                        }],
                                                        // Month
                                                        ["%m-%y", function (d) {
                                                                        return d.getMonth();
                                                        }]
                                        ]
                        };
        </script>

</head>
<body>
<!-- 右上角的悬浮 sidebar  -->
<div id="mySidenav" class="sidenav">
  <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>
   <a href="#"> 目录 </a>
   <iframe id="ha" src="$related_to_side_bar$global_sidebar.html" name='left' frameborder="0" scrolling="auto" width="400"  height="100%">
    您的浏览器不支持iframe，请升级
   </iframe>
</div>

<TABLE border=0 height=600px align=left>
  <TR>
    <TD width=260px align=left valign=top style="BORDER-RIGHT: #999999 1px dashed">
      <ul id="tree" class="ztree">

      </ul>
    </TD>
    <TD width=770px align=left valign=top>

<!---------------------------------------------------------------------------------------------------------------------------->
<div class="container">
<span style="font-size:20px;cursor:pointer;z-index: 9999; position: fixed; right: 0px; top: 0px;" onclick="openNav()">&#9776; 目录</span>

'''
    html_tail = '''


<hr/>
<div class="footer">
        Copyright &copy; xiaoxiyouran. All rights reserved.

</div>

</div> <!-- /container -->

<!---------------------------------------------------------------------------------------------------------------------------->

        </TD>
  </TR>
</TABLE>

<!-- 请注意，以下两个部分的代码执行是有顺序的，必须严格按照这个顺序来。另外，放在底部是为了优化界面，使加载速度更快 -->
<!-- 为了优化代码风格 -->
<script src="$base_url$/packages/js/jquery-1.9.1.min.js" ></script>
<script src="$base_url$/packages/js/bootstrap.min.js" ></script>
<script src="$base_url$/packages/js/highlight.min.js" ></script>
<script >hljs.initHighlightingOnLoad();</script>

<!-- 以下是为了生成文档的侧边栏 -->
<script type="text/javascript" src="$base_url$/packages/generate_header_sidebar/js/jquery-1.4.4.min.js"></script>
<script type="text/javascript" src="$base_url$/packages/generate_header_sidebar/js/jquery.ztree.core-3.5.js"></script>
<script type="text/javascript" src="$base_url$/packages/generate_header_sidebar/src/ztree_toc.js"></script>

<SCRIPT type="text/javascript" >
<!--
$(document).ready(function(){
  $('#tree').ztree_toc({
    is_auto_number : true,
    use_head_anchor: true
  });
});
//-->
</SCRIPT>

</body>
</html>
    '''
    html_header = html_header.replace('$title$', markdown['title'])
    html_header = html_header.replace('$base_url$', markdown['base_url'])

    # 每个生成的页面都有一个按钮浏览当前一级文件夹下的 side bar
    html_header = html_header.replace('$related_to_side_bar$', related_to_sidebar_str)

    html_tail = html_tail.replace('$base_url$', markdown['base_url'])


    return html_header + markdown['html'] + html_tail


def process_table(markdown):
    '''
    主要是为了处理表格，能画出实现
    :return:
    '''

    markdown['html'] = markdown['html'].replace('<table>',"<table style='border: 1px solid black; border-collapse:collapse;  border-spacing:0;'>");
    markdown['html'] = markdown['html'].replace('<th>',"<th style='border: 1px solid black; border-collapse:collapse;  border-spacing:0;'>");
    markdown['html'] = markdown['html'].replace('<td>',"<td style='border: 1px solid black; border-collapse:collapse;  border-spacing:0;'>");

    # return markdown;



# file src/aa/ab.md
# output_dir docs/aa
def gen_doc(output_base_url_copy, file,output_dir, template=None, base_url=''):
    unModified = True
    base_name = os.path.basename(file)    # src/aa/ab.md => ab.md
    name = os.path.splitext(base_name)[0] # aa.md ==> ab
    markdown={
            'name' : name,
            'input_file' : file,
            'output_file' : output_dir + os.path.sep + name + '.html',
            'title': '',
            'html' : '',
            'base_url': base_url
            };


    if os.path.isfile(markdown['output_file']) and (time.ctime(os.stat(file).st_mtime) < time.ctime(os.stat(markdown['output_file']).st_ctime)):
        print "[skip] " + markdown['input_file'] + "=>" + markdown['output_file'];
        return unModified;

    unModified = unModified and False;
    in_comment = False;
    with open(file, 'r') as f:
        cnt = 0
        for line in f.readlines():
            line = line.strip()  # 把末尾的'\n'删掉
            if line != '':
                if line[0] == '`':
                    if in_comment:
                        in_comment = False;
                    else:
                        in_comment = True;
                else:
                    cnt = cnt + 1   # 非注释

                if cnt < 20:
                    if line[0] == '#' and line[1] != '#' and (not in_comment):
                        line = line.strip()
                        line = line.strip('#')
                        line = line.strip()
                        markdown['title'] = line;
                        break;
                else:
                    break

    fflname = os.path.split(file)
    flname = fflname[-1]
    ext = os.path.splitext(flname)[-1]
    flname = flname.rstrip(ext)  # 删除尾部的扩展名字

    if markdown['title'] == '':
        markdown['title'] = flname

    try:
        markdown['html'] = __main__.called(file,'return')
        process_table(markdown);
        process_highlight(markdown);
        process_mermaid(markdown)  ;
    except UnicodeDecodeError:
        print 'UnicodeDecodeError==============================================================================================================>' \
                + file
    except:
        print 'OtherError======================================================================================================================>' \
                + file

    html = ''
    if template:
        print "[build] "+ markdown['input_file'] + "=>" + markdown['output_file'];
        outBytemplate(template,markdown['output_file'],markdown);
    else:
        html = default_template(output_base_url_copy, markdown);
        print "[buildDefaultTemplate] "+ markdown['input_file'] + "=>" + markdown['output_file'];
        file_put_contents(markdown['output_file'],html)

    return unModified

def parse_dir(output_base_url_copy, input_dir, output_dir,ignoreDirFile = [],isDectionaryDefault = True,base_url='.'):
    unModified = True
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    template = find_template(input_dir)

    extractIgnoreList(ignoreDirFile, input_dir)             # 处理需要忽略的文件和文件


    for file in os.listdir(input_dir):
        full_path = input_dir+os.path.sep+file;
        if full_path in ignoreDirFile:
            continue;

        if os.path.isdir(full_path):
            if 'unmd' in full_path :
                continue

            if isDectionaryDefault and full_path == '../packages':
                continue;


            if isDectionaryDefault and full_path == '../output':
                new_output_dir = output_dir

            else:
                new_output_dir = output_dir + os.path.sep + file

            unModified_tmp = parse_dir(output_base_url_copy, full_path,new_output_dir,ignoreDirFile, isDectionaryDefault, base_url + os.path.sep + "..");
            unModified = unModified and unModified_tmp
        else:
            unModified = parse_file(base_url, file, full_path, output_base_url_copy, output_dir, template, unModified)

    return unModified


def find_template(input_dir):
    template = input_dir + os.path.sep + "template.php"
    if not os.path.isfile(template):
        template = None  # if template == None
    return template


def parse_file(base_url, file, full_path, output_base_url_copy, output_dir, template, unModified):
    # print base_url
    ps = os.path.splitext(file)
    ext = ps[1]
    if 'md' in ext:
        unModified_tmp = gen_doc(output_base_url_copy, full_path, output_dir, template, base_url);
        unModified = unModified and unModified_tmp
    elif not ('php' in ext):
        # 1. 原文件没有修改跳过  2. 自己复制给自己，跳过
        if (os.path.isfile(output_dir + os.path.sep + file) and (time.ctime(os.stat(full_path).st_mtime) < time.ctime(
            os.stat(output_dir + os.path.sep + file).st_ctime))) or \
                    (full_path == (output_dir + os.path.sep + file)):
                        print "[skipcopy] " + full_path + " => " + (output_dir + os.path.sep + file)

        # 1. 如果输出文件存在，原文件不存在，输出文件删除 2. 输出文件存在，原文件也存在，更新
        elif os.path.isfile(output_dir + os.path.sep + file):
            unModified = unModified and False
            delete = False;
            if os.path.isfile(output_dir + os.path.sep + file):
                os.remove(output_dir + os.path.sep + file)
                delete = True;
            if os.path.isfile(full_path):
                shutil.copy(full_path, output_dir + os.path.sep + file);  # copy file or directory
                delete = False

            if delete is True:
                print "[deletecopy] " + full_path + " => " + (output_dir + os.path.sep + file)
            else:
                print "[updatecopy] " + full_path + " => " + (output_dir + os.path.sep + file)

        # 输出文件不存在，从原文件那里创建
        else:  # 从原文件创建也要保证源文件存在
            if os.path.isfile(full_path):
                shutil.copy(full_path, output_dir + os.path.sep + file);  # copy file or directory
                print "[createcopy] " + full_path + " => " + (output_dir + os.path.sep + file)
                unModified = unModified and False
    return unModified


def extractIgnoreList(ignoreDirFile, input_dir):
    # 处理需要忽略的文件和文件夹
    ignoremdFileName = input_dir + os.path.sep + '.mdignore'
    currentIgnore = []
    if os.path.exists(ignoremdFileName):
        currentIgnore = ignore(ignoremdFileName)
    # print currentIgnore
    for dir in currentIgnore:
        file = input_dir + os.path.sep + dir;
        ignoreDirFile.append(file);


def parser(input_dir, output_dir,  isDectionaryDefault, base_url, ignoreDirFile = []):
    '''
    根据输入目录解析一个文件
    :param input_dir:   ../src/aa 这是一个文件夹
    :param output_dir:  ../docs/aa 这也是一个文件夹
    :param ignoreDirFile: 当前文件夹需要忽略的目录
    :param isDectionaryDefault:
    :param base_url:
    :return:
    '''
    # ignoreDirFile = []
    output_base_url_copy = output_dir  # 保存当前输出文件夹的
    output_dir_copy = output_dir

    unModified_tmp = parse_dir(output_base_url_copy, input_dir, output_dir, ignoreDirFile, isDectionaryDefault,
            base_url);

    return unModified_tmp
# return unModified_tmp


def appendix(unModified_tmp, output_dir_copy):
    '''
    产生副作用，添加附加功能，如 top.html, global_sidebar, global_tree 等文件
    :return:
    '''
    unModified = True                   # 遍历当前文件夹，假如没有文件发生改变，索引文件就不需要重新生成

    unModified = unModified and unModified_tmp
    if not unModified:
        if not isDectionaryDefault:
            generate_index(output_dir_copy)
        else:
            generate_index()
    else:
        print '[-------------------------SKIP TO GENERATE INDEX-------------------------]'


def anaylyze_input_dir(input_dir):
    src_str = 'src'                     # 输入目录
    base_url = '..'                     # src 对应的基地址
    nPos = input_dir.find(src_str);
    sep_count = input_dir[nPos:].count(os.path.sep)     # 统计除了 ../src 外反斜杠的个数，如 ../src/aa 现在的字符是 src/aa
    for i in range(sep_count):
        base_url = base_url + os.path.sep + '..'

    return (base_url, sep_count)

if __name__=='__main__':
    # print '参数个数为:', len(sys.argv), '个参数。'
    # print '参数列表:', str(sys.argv)

    args = str(sys.argv)
    isDectionaryDefault = True;
    if len(sys.argv) == 3:  #
        isDectionaryDefault = False
        input_dir = sys.argv[1];
        output_dir = sys.argv[2];
    else:
        warnings.warn('You do not input a src file and output file! default--. and output will be used', DeprecationWarning);
        input_dir = "..";
        output_dir = "../output"


    # 去除首位空格
    input_dir = input_dir.strip()
    output_dir = output_dir.strip()
    # 去除尾部 \ 符号
    input_dir = input_dir.rstrip("\\")
    output_dir = output_dir.rstrip("\\")

    output_dir_copy = output_dir

    [base_url, sep_count] = anaylyze_input_dir(input_dir)

    global_unModified =  True           # 定义一个全局变量
    if sep_count == 0:  # 如果桑主目录 ../src --> ../docs

        ignoreDirFile = []  # 在 ../src 目录下需要读取从当前位置需要忽略的文件或者文件夹
        extractIgnoreList(ignoreDirFile, input_dir)  # 处理需要忽略的文件和文件

        for file in os.listdir(input_dir):            # 输出目录过滤掉了一些没用的
            # file_name = file
            fullname = input_dir + os.path.sep + file; # 注意，这里得用全部路径
            if os.path.isdir(fullname):
                new_output_dir = output_dir_copy + os.path.sep + file       # 产生一级文件夹 ../src/aa
                new_input_dir = input_dir + os.path.sep + file              # 产生一级文件夹 ../docs/aa

                if new_input_dir in ignoreDirFile:                          # 跳过需要忽略的文件夹
                    continue;

                [base_url, sep_count] = anaylyze_input_dir(new_input_dir)   # 用新的 base_url = ../..

                unModified_tmp = parser(new_input_dir, new_output_dir, isDectionaryDefault, base_url, ignoreDirFile)
                appendix(unModified_tmp, new_output_dir)
                global_unModified = global_unModified and unModified_tmp    # 子文件夹有改动，全局肯定也改动了
            else:       # 如果是文件呢，就只解析 markdown, 不产生索引
                new_output_dir = output_dir_copy   # 产生一级文件夹 ../src/aa
                new_input_dir = input_dir + os.path.sep + file  # 产生一级文件夹 ../docs/aa

                if new_input_dir in ignoreDirFile:              # 当前文件是需要忽略的
                    continue;

                [base_url, sep_count] = anaylyze_input_dir(input_dir)

                # unModified_tmp = parser(new_input_dir, new_output_dir, isDectionaryDefault, base_url)   # 已经是上层目录了，../docs 下， base_url = ..
                template = find_template(input_dir)
                unModified_tmp = True
                unModified_tmp = parse_file(base_url, file, new_input_dir, output_dir_copy, new_output_dir, template,
                        unModified_tmp)
                global_unModified = global_unModified and unModified_tmp  # 当前文件夹下有改动，全局肯定也改动了，如 ../src/aa.md

        # 处理完每个子文件夹后，然后生成全局索引
        appendix(global_unModified, output_dir_copy);       # 在 ../docs 下生成相关的索引文件
    else:
        '''
        输入是 ../src/aa ../docs/aa
        '''
        # 先处理子文件夹
        if os.path.isdir(input_dir):                        # 确保 ../src/aa 是一个文件夹
            new_output_dir = output_dir    #output_dir_copy + os.path.sep + file  # 产生一级文件夹 ../src/aa
            new_input_dir = input_dir       # + os.path.sep + file  # 产生一级文件夹 ../docs/aa

            [base_url, sep_count] = anaylyze_input_dir(new_input_dir)  # 用新的 base_url = ../..

            unModified_tmp = parser(new_input_dir, new_output_dir, isDectionaryDefault, base_url)
            appendix(unModified_tmp, new_output_dir)
            global_unModified = global_unModified and unModified_tmp  # 子文件夹有改动，全局肯定也改动了
        else:  # 如果是文件呢，就只解析 markdown, 不产生索引
            '''
            ../src/aa ../docs/aa  如果是文件的话... 那目录就是它的上一级 ../src
            '''
            rPos = output_dir.rfind(os.path.sep)        # 反向找到第一个 / 的位置
            new_output_dir = output_dir[:rPos]  # 产生一级文件夹 ../src/aa

            rPos = input_dir.rfind(os.path.sep)
            new_input_dir = input_dir[:rPos]  # 产生一级文件夹 ../docs/aa

            [base_url, sep_count] = anaylyze_input_dir(new_input_dir)

            unModified_tmp = parser(new_input_dir, new_output_dir, isDectionaryDefault,
                    base_url)  # 已经是上层目录了，../docs 下， base_url = ..
            global_unModified = global_unModified and unModified_tmp  # 当前文件夹下有改动，全局肯定也改动了，如 ../src/aa.md

        # 子文件夹都更新了，全局索引是需要更新的
        ii = 0
        index = 0
        for i in range(len(output_dir)):
            ii = i          # 下标

            if output_dir[i] == os.path.sep:
                index = index + 1
            if index == 2:
                break;

        appendix(global_unModified, output_dir[:ii])       # 输出文件夹是： ../docs



