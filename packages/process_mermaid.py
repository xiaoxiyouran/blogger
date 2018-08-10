#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
useage: python -W all generate_index.py doc
'''
import  re
def process_mermaid(markdown):
    # print markdown['html']
    oldReplace = '<pre><code class="mermaid">'
    oldReplace2 = '</code></pre>'
    len_oldReplace = len(oldReplace)
    len_oldReplace2 = len(oldReplace2)
    findList = [m.start() for m in re.finditer(oldReplace, markdown['html'])]
    # findList2 = []
    #
    # for i in range(len(findList)):
    #     index = markdown['html'].find(oldReplace2,findList[i] )
    #     if index is not -1:
    #         findList2.append(index)
    #
    # print findList2

    newReplace = '<div class="mermaid">'
    newReplace2 = '</div>'

    # len_newReplace = len(newReplace)

    # print findList
    startPos = 0
    newString = ''
    while len(findList) > 0 :
        first = findList.pop(0)
        second = markdown['html'].find(oldReplace2,first )
        if second is not -1:
            midContent = markdown['html'][first+len_oldReplace:second]
            midContent = midContent.replace('&gt;', '>')
            newString += markdown['html'][startPos:first] + newReplace + midContent + newReplace2;
            startPos = second + len_oldReplace2

    markdown['html'] = newString + markdown['html'][startPos:];
    # print markdown['html']

if __name__=='__main__':
    markdown = {'html':''}
    markdown['html'] = '''
   <h1 id="mermaid">mermaid 画图</h1>
<p>画图的原文链接： http://www.sysctl.me/2017/11/11/Draw%20Diagrams%20With%20Markdown/</p>
<p>下载包： https://mermaidjs.github.io/ 下面的<code>remark.js</code></p>
<p>使用方法： https://github.com/gnab/remark/wiki/Adding-graphs-via-Mermaid</p>
<h2 id="_1">序列图</h2>
<h3 id="1">例子1</h3>
<pre><code>​```mermaid
%% Example of sequence diagram
  sequenceDiagram
	Alice-&gt;&gt;Bob: Hello Bob, how are you?
	alt is sick
	Bob-&gt;&gt;Alice: Not so good :(
	else is well
	Bob-&gt;&gt;Alice: Feeling fresh like a daisy
	end
	opt Extra response
	Bob-&gt;&gt;Alice: Thanks for asking
	end

</code></pre>

 <div class="mermaid">%% Example of sequence diagram
  sequenceDiagram
	Alice->>Bob: Hello Bob, how are you?
	alt is sick
	Bob-&gt;&gt;Alice: Not so good :(
	else is well
	Bob-&gt;&gt;Alice: Feeling fresh like a daisy
	end
	opt Extra response
	Bob-&gt;&gt;Alice: Thanks for asking
	end

</div>

<h2 id="_2">流程图</h2>
<pre><code>​```mermaid
graph LR
A[Hard edge] --&gt;B(Round edge)
	B --&gt; C{Decision}
	C --&gt;|One| D[Result one]
	C --&gt;|Two| E[Result two]

</code></pre>

<pre><code class="mermaid">graph LR
A[Hard edge] --&gt;B(Round edge)
	B --&gt; C{Decision}
	C --&gt;|One| D[Result one]
	C --&gt;|Two| E[Result two]
</code></pre>

<h2 id="_3">甘特图</h2>
<pre><code class="mermaid">```mermaid
%% Example with slection of syntaxes
		gantt
		dateFormat  YYYY-MM-DD
		title Adding GANTT diagram functionality to mermaid

		section A section
		Completed task            :done,    des1, 2014-01-06,2014-01-08
		Active task               :active,  des2, 2014-01-09, 3d
		Future task               :         des3, after des2, 5d
		Future task2               :         des4, after des3, 5d

		section Critical tasks
		Completed task in the critical line :crit, done, 2014-01-06,24h
		Implement parser and jison          :crit, done, after des1, 2d
		Create tests for parser             :crit, active, 3d
		Future task in critical line        :crit, 5d
		Create tests for renderer           :2d
		Add to mermaid                      :1d

		section Documentation
		Describe gantt syntax               :active, a1, after des1, 3d
		Add gantt diagram to demo page      :after a1  , 20h
		Add another diagram to demo page    :doc1, after a1  , 48h

		section Last section
		Describe gantt syntax               :after doc1, 3d
		Add gantt diagram to demo page      : 20h
		Add another diagram to demo page    : 48h

</code></pre>

<pre><code class="mermaid">%% Example with slection of syntaxes
		gantt
		dateFormat  YYYY-MM-DD
		title Adding GANTT diagram functionality to mermaid

		section A section
		Completed task            :done,    des1, 2014-01-06,2014-01-08
		Active task               :active,  des2, 2014-01-09, 3d
		Future task               :         des3, after des2, 5d
		Future task2               :         des4, after des3, 5d

		section Critical tasks
		Completed task in the critical line :crit, done, 2014-01-06,24h
		Implement parser and jison          :crit, done, after des1, 2d
		Create tests for parser             :crit, active, 3d
		Future task in critical line        :crit, 5d
		Create tests for renderer           :2d
		Add to mermaid                      :1d

		section Documentation
		Describe gantt syntax               :active, a1, after des1, 3d
		Add gantt diagram to demo page      :after a1  , 20h
		Add another diagram to demo page    :doc1, after a1  , 48h

		section Last section
		Describe gantt syntax               :after doc1, 3d
		Add gantt diagram to demo page      : 20h
		Add another diagram to demo page    : 48h
</code></pre>


<hr/>
<div class="footer">
	Copyright &copy; xiaoxiyouran. All rights reserved.

</div>

</div> <!-- /container -->
    '''
    process_mermaid(markdown)
