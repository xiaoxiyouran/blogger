#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
useage: python -W all generate_index.py doc
'''

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import warnings
import os

def write_to_file(global_sidebar, global_tree ,output_dir):
    html = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
	<title>Top</title>
	<style type="text/css">
	body{
		margin: 0;
		padding: 0;
		font-size: 13px;
		Font-family: Helvetica, Tahoma, Arial, STXihei, “华文细黑”, “Microsoft YaHei”, “微软雅黑”, SimSun, “宋体”, Heiti, “黑体”, sans-serif;
		background: #fff;
	}
	</style>
</head>

<frameset cols='200,*'>
	<frame src='$LEFT$' name='left' frameborder="1" bordercolor="#999999">

	<frame src='$RIGHT$' name='right' frameborder="1" bordercolor="#999999">
</frameset>

</html>    
    '''
    html = html.replace('$LEFT$', global_sidebar)
    html = html.replace('$RIGHT$', global_tree)

    with open(output_dir+ os.path.sep + 'top.html','w') as f:
        f.writelines(html);



def generate_top(global_sidebar,global_tree, output_dir):
    write_to_file(global_sidebar, global_tree ,output_dir)

    print '[-------------------------END TO GENERATE TOOP------------------------------]'
