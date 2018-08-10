#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
useage: python -W all generate_index.py doc
'''

import sys
import warnings
import os
import generate_sidebar
from generate_sidebar import generate_sidebar

sys.setdefaultencoding('utf-8')
divider_direc = '|----'
divider_file  = '|____'
divider_blank = '|    '

import locale
import platform
def encode_decode(full_path):
    '''
    process the encode problem in windows
    :param full_path:
    :return:
    '''
    if locale.getdefaultlocale()[1] == 'cp936' and 'Windows' in platform.system():
        full_path = full_path.decode('gbk')
        full_path = full_path.encode('utf-8')

    return full_path

def write_to_file(content,output_dir):
    # 处理输出地址的相对地址
    base_url = '..'  # 默认有一级
    sep_count = output_dir.count(os.path.sep)  # 如 ../docs/aa 就有两级目录
    for i in range(sep_count - 1):
        base_url = base_url + '/..'


    html_head = '''
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
	<title>xi's tree</title>
		
	<!-- 右上角的侧边导航栏 -->
	<link rel="stylesheet" href="$base_url$/packages/hock_side_bar/css/sidebar.css"> <!--初始化文件-->
	<script src="$base_url$/packages/hock_side_bar/js/sidebar.js"></script> <!--rem适配js-->
	
	<style type="text/css">
	body{
		margin: 4px;
		padding: 0;
		font-size: 14px;
		Font-family: Helvetica, Tahoma, Arial, STXihei, “华文细黑”, “Microsoft YaHei”, “微软雅黑”, SimSun, “宋体”, Heiti, “黑体”, sans-serif;
		background: #fff;
	}
	ul{
		margin: 4px;
		padding: 0 0 0 14px;
	}
	
	a:link { 
	color:#FF0000; 
	text-decoration:underline; 
	} 
	a:visited { 
	color:#00FF00; 
	text-decoration:none; 
	} 
	a:hover { 
	color:#000000; 
	text-decoration:none; 
	} 
	a:active { 
	color:#0000FF; 
	text-decoration:none; 
	} 
	</style>
</head>
<body>
<div id="mySidenav" class="sidenav" >
  <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>
   <a href="#"> 目录 </a>
   <iframe id="ha" src="./global_sidebar.html" name='left' frameborder="0" scrolling="auto" width="400"  height="100%">
    您的浏览器不支持iframe，请升级
   </iframe>
 <!-- <frame src='./global_sidebar.html' name='left' frameborder="1" bordercolor="#999999"> -->
  
</div>
<span style="font-size:20px;cursor:pointer;z-index: 9999; position: fixed; right: 0px; top: 0px;" onclick="openNav()">&#9776; 目录</span>
<pre><code>

'''
    html_tail = '''
    
    </code>
</pre>

</body>
</html>
'''
    html_head = html_head.replace('$base_url$', base_url)
    with open(output_dir+ os.path.sep + 'global_tree.html','w') as f:
        f.writelines(html_head+content+html_tail);


def generate_tree(info,output_dir):
    # print info

    content = ''
    for path in info:
        pat = path[0]
        pat = encode_decode(pat);
        char = path[1]
        pat_div = pat.split(os.path.sep)

        level = len(pat_div) - 1
        ss = ''

        # if pat == './global_tree.html' or pat == './global_sidebar.html' or pat == './top.html':
        if 'global_tree.html' in pat or 'global_sidebar.html' in pat or 'top.html' in pat:
            continue;

        if char == 'dir':
            ss = divider_blank * (level -1) + divider_direc + pat_div[-1]
        else:
            ps = os.path.splitext(pat_div[-1])
            ext = ps[1]
            if 'html' in ext or 'pdf' in ext or 'xlsx' in ext:
                ss = divider_blank * (level - 1) + \
                     divider_file + \
                     "<a href='" + pat + "'>"+\
                     pat_div[-1] +\
                    "</a>"
            else:
                continue;
                ss = divider_blank * (level -1) + divider_file + pat_div[-1]

        content = content + ss + '\n';

    write_to_file(content,output_dir)
    print '[-------------------------END TO GENERATE TREE------------------------------]'

    #-------------------------------------------------------------------开始产生左侧的sidebar
    print '[-------------------------BEGIN TO GENERATE SIDEBAR-------------------------]'
    global_tree = '.' + os.path.sep + 'global_tree.html'
    generate_sidebar(global_tree, output_dir, info)
