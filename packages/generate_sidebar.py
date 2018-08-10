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
import re
import generate_top
from generate_top import generate_top

create_root_dirnode = "_$Root_level$ = tree.createNode('$nodeName$',false,'$base_url$/packages/doc_tree/jquery-tree/images/folder.png',null,null,'context1');"
create_root_unlink_filnode = "_$Root_level$ = tree.createNode('$nodeName$',false,'$base_url$/packages/doc_tree/jquery-tree/images/file.png',null,null,'context1');"
create_root_link_filnode = '''_$Root_level$ = tree.createNode("<a href = '$LinkPath$' target = 'right'>$nodeName$</a>",false,'$base_url$/packages/doc_tree/jquery-tree/images/file.png',null,null,'context1');'''

create_child_dirnode = "_$Root_level$ = $fatherNode$.createChildNode('$nodeName$',false,'$base_url$/packages/doc_tree/jquery-tree/images/folder.png',null,'context1');"
create_child_unlink_filnode = "_$Root_level$ = $fatherNode$.createChildNode('$nodeName$',false,'$base_url$/packages/doc_tree/jquery-tree/images/file.png',null,'context1');"
create_child_link_filnode = '''_$Root_level$ = $fatherNode$.createChildNode("<a href = '$LinkPath$' target = 'right'>$nodeName$</a>",false,'$base_url$/packages/doc_tree/jquery-tree/images/file.png',null,'context1');'''


def write_to_file(content,output_dir):
    # 处理输出地址的相对地址
    base_url = '..'                            # 默认有一级
    sep_count = output_dir.count(os.path.sep)  # 如 ../docs/aa 就有两级目录
    for i in range(sep_count-1):
        base_url = base_url + '/..'


    html_head = '''
<!doctype html>
<html lang="zh">
<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"> 
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>xi's sidebar</title>
	<link rel="stylesheet" type="text/css" href="$base_url$/packages/doc_tree/jquery-tree/css/default.css">
	<link rel="stylesheet" type="text/css" href="$base_url$/packages/doc_tree/jquery-tree/css/Aimara.css">
	<link rel="stylesheet" type="text/css" href="$base_url$/packages/doc_tree/jquery-tree/css/Example.css">
	<script id="testscript" src="$base_url$/packages/doc_tree/jquery-tree/lib/Aimara.js" type="text/javascript" callBack="$base_url$"></script>
	<script type="text/javascript">
			window.onload = function() {

				//Initializing Tree

				//Tree Context Menu Structure
				var contex_menu = {
					'context1' : {
						elements : [
							{
								text : 'Expand Subtree',
								icon: 'images/tree.png',
								action : function(node) {
									node.expandSubtree();
								},
							},
							{
								text : 'Collapse Subtree',
								icon: 'images/tree.png',
								action : function(node) {
									node.collapseSubtree();
								}
							}						
						]
					}
				};

				//Creating the tree
				tree = createTree('div_tree','white',contex_menu);

				// div_log = document.getElementById('div_log');

				//Setting custom events
				tree.nodeBeforeOpenEvent = function(node) {
					// div_log.innerHTML += node.text + ': Before expand event<br/>';
				}

				tree.nodeAfterOpenEvent = function(node) {
					// div_log.innerHTML += node.text + ': After expand event<br/>';
				}

				tree.nodeBeforeCloseEvent = function(node) {
					// div_log.innerHTML += node.text + ': Before collapse event<br/>';
				}

				//Loop to create test nodes    
    
    '''

    html_tail = '''
				//Rendering the tree
				tree.drawTree();
			};

			function expand_all() {
				tree.expandTree();
			}

			function clear_log() {
				// document.getElementById('div_log').innerHTML = '';
			}

			function collapse_all() {
				tree.collapseTree();
			}
		</script>
	<!--[if IE]>
		<script src="$base_url$/packages/doc_tree/jquery-tree/lib/html5shiv.min.js"></script>
	<![endif]-->
</head>
<body>
<div class="htmleaf-container">
		<div class="htmleaf-content">			
			<button onclick="expand_all()">Expand</button>
			<button onclick="collapse_all()">Collapse</button>
			<br>
			<div id="div_tree"></div>
		</div>
		
</div>

</body>
</html>    
    '''

    html_head = html_head.replace('$base_url$', base_url)
    html_tail = html_tail.replace('$base_url$', base_url)
    content = content.replace('$base_url$', base_url)

    with open(output_dir+ os.path.sep + 'global_sidebar.html','w') as f:
        f.writelines(html_head+content+html_tail);





def process_special_symbol(name):
    '''
    process the special symbol, like blank, - , ~, . These will create error for javascript to generate a tree using a valid name.
    :return:
    '''

    name = re.sub('\s', '', name)  # delete all blank
    name = name.replace('-', '_')
    name = name.replace('~', '_')
    name = name.replace('.','_')
    name = name.replace('@','_')
    name = name.replace('+', '_')
    name = name.replace(',', '_')
    name = name.replace('，', '_')
    name = name.replace('[', '_')
    name = name.replace(']', '_')
    name = name.replace('【', '_')
    name = name.replace('】', '_')
    name = name.replace('(', '_')
    name = name.replace(')', '_')
    name = name.replace('【', '_')
    name = name.replace('】', '_')
    name = name.replace('，', '_')
    name = name.replace('#', '_')
    name = name.replace("'", '_')
    name = name.replace("（", '_')
    name = name.replace("）", '_')
    name = name.replace("：", '_')
    name = name.replace("、", '_')
    name = name.replace("？", '_')
    name = name.replace("&", '_')

    # 去除空格
    strinfo = re.compile(' ')
    name = strinfo.sub('', name)

    name = name.replace(' ', '')
    name = ''.join(name.split())



    return name

def generate_sidebar(global_tree, output_dir, info):
    # print info

    # 先为树结构创建一个根节点

    content = ''

    global_tree_name = global_tree.split(os.path.sep)[-1]
    tt = create_root_link_filnode.replace('$nodeName$', global_tree_name)
    tt = tt.replace('$LinkPath$', global_tree)
    tt = tt.replace('$Root_level$', global_tree_name.replace('.','_') + str(1))

    content = content + tt + '\n'
    for path in info:
        pat = path[0]
        char = path[1]
        pat_div = pat.split(os.path.sep)
        # print pat_div
        level = len(pat_div) - 1

        # if pat == './global_sidebar.html' or pat == global_tree or pat == './top.html':
        if 'global_sidebar.html' in pat or 'global_tree.html' in pat or 'top.html' in pat:
            continue;

        if level == 1: # 处在第一级的开始创建根节点
            if char == 'dir':
                dir_name = pat_div[-1]
                ss = create_root_dirnode.replace('$nodeName$',dir_name)
                ss = ss.replace('$Root_level$',process_special_symbol(dir_name) + str(level) )
            else:
                file_name = pat_div[-1]
                file_name = process_special_symbol(file_name)

                ps = os.path.splitext(pat_div[-1])
                ext = ps[1]

                if 'html' in ext or 'pdf' in ext:
                    ss = create_root_link_filnode.replace('$nodeName$',pat_div[-1])
                    ss = ss.replace('$LinkPath$',pat)
                    ss = ss.replace( '$Root_level$',file_name + str(level) )
                else:
                    continue;
                    ss = create_root_unlink_filnode.replace('$nodeName$',pat_div[-1])
                    ss= ss.replace('$Root_level$',file_name + str(level))
        else:
            if char == 'dir':
                dir_name = pat_div[-1]
                ss = create_child_dirnode.replace('$nodeName$', dir_name)
                # ss = ss.replace('$Root_level$', dir_name + str(level))
                ss = ss.replace('$fatherNode$', '_'+ process_special_symbol(pat_div[-2]) + str(level-1) )
                ss = ss.replace('$Root_level$', process_special_symbol( dir_name) + str(level) )
            else:
                file_name = pat_div[-1]

                ps = os.path.splitext(pat_div[-1])
                ext = ps[1]

                if 'html' in ext or 'pdf' in ext:
                    ss = create_child_link_filnode.replace('$nodeName$',pat_div[-1])
                    ss = ss.replace('$LinkPath$',pat)
                    ss = ss.replace('$fatherNode$','_' + process_special_symbol( pat_div[-2]) + str(level-1) )
                    ss = ss.replace('$Root_level$', process_special_symbol(file_name) + str(level))
                else:
                    continue
                    ss = create_child_unlink_filnode.replace('$nodeName$',pat_div[-1])
                    ss = ss.replace('$fatherNode$','_' + process_special_symbol( pat_div[-2]) + str(level-1) )
                    ss = ss.replace('$Root_level$', process_special_symbol( file_name ) + str(level))



        content = content + ss + '\n';

    write_to_file(content,output_dir)
    print '[-------------------------END TO GENERATE SIDEBAR---------------------------]'
    #-------------------------------------------------------------------开始写顶层
    print '[-------------------------BEGIN TO GENERATE TOOP----------------------------]'
    global_sidebar = '.' + os.path.sep + 'global_sidebar.html'
    generate_top(global_sidebar,global_tree, output_dir)

