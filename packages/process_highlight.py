#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
useage: python -W all generate_index.py doc
'''

import  re
import  copy


def delInCode(findList,findListPreCode,findListPostCode):
    '''
    需要把代码域内的 == 排除掉
    :param findList:
    :param findListPreCode:
    :param findListPostCode:
    :return:
    '''
    # print findList
    # print findListPreCode
    # print findListPostCode

    # process_list = findList
    while len(findListPreCode) > 0 and len(findListPostCode) >0 :
        first = findListPreCode.pop(0)
        second = findListPostCode.pop(0)
        pop_index = []
        for i in range(len(findList)):
            if findList[i] >= first and second >= findList[i]:
                pop_index.append(i)
        newFindList = []
        for i in range(len(findList)):
            if i not in pop_index:
                newFindList.append(findList[i])

        findList = copy.deepcopy(newFindList)


    return findList





def process_highlight(markdown):
    s = markdown['html']
    findList = [m.start() for m in re.finditer('==', s)]
    findListPreCode = [m.start() for m in re.finditer('<pre><code', s)]
    findListPostCode = [m.start() for m in re.finditer('</code></pre>', s)]

    findList = delInCode(findList,findListPreCode, findListPostCode)
    # print findList
    # ll = s.split("==")
    newString = ''
    initPos = 0
    while len(findList) > 0 and len(findList) != 1:
        first = findList[0];
        second = findList[1];
        newString += s[initPos:first] + '<mark>' + s[first + 2:second] + '</mark>';  # + s[second + 2: ]
        initPos = second + 2;
        findList.pop(0)  # 前面已经弹出去了一个，下一个就在最前面
        findList.pop(0)
    markdown['html'] = newString + s[initPos:];
    # print markdown['html']

if __name__=='__main__':
    markdown = {'html':''}
    markdown['html'] = '''
    <h1 id="-">链接 -------</h1>
    <blockquote>
    <p>牛客OJ：<a href="http://www.nowcoder.com/practice/1a834e5e3e1a4b7ba251417554e07c00?tpId=13&amp;tqId=11165&amp;rp=1&amp;ru=/ta/coding-interviews&amp;qru=/ta/coding-interviews/question-ranking">数值的整数次方</a></p>
    <p>九度OJ：http://ac.jobdu.com/problem.php?pid=1514</p>
    <p>GitHub代码： <a href="https://github.com/gatieme/CodingInterviews/tree/master/011-数值的整数次方">011-数值的整数次方</a></p>
    <p>CSDN题解：<a href="http://blog.csdn.net/gatieme/article/details/51123043">剑指Offer--011-数值的整数次方</a></p>
    </blockquote>
    <table style='border: 1px solid black; border-collapse:collapse;  border-spacing:0;'>
    <thead>
    <tr>
    <th style='border: 1px solid black; border-collapse:collapse;  border-spacing:0;'>牛客OJ</th>
    <th align="center">九度OJ</th>
    <th align="right">CSDN题解</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td style='border: 1px solid black; border-collapse:collapse;  border-spacing:0;'><a href="http://www.nowcoder.com/practice/1a834e5e3e1a4b7ba251417554e07c00?tpId=13&amp;tqId=11165&amp;rp=1&amp;ru=/ta/coding-interviews&amp;qru=/ta/coding-interviews/question-ranking">数值的整数次方</a></td>
    <td align="center"><a href="http://ac.jobdu.com/problem.php?pid=1514">1514-数值的整数次方</a></td>
    <td align="right"><a href="http://blog.csdn.net/gatieme/article/details/51123043">剑指Offer--011-数值的整数次方</a></td>
    </tr>
    </tbody>
    </table>
    <p><br>
    <strong>您也可以选择<a href="http://blog.csdn.net/gatieme/article/details/51916802">回到目录-剑指Offer--题集目录索引</a></strong></p>
    <h1 id="_1">题意</h1>
    <hr />
    <p><strong>题目描述</strong></p>
    <blockquote>
    <p>给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。</p>
    <p> ==可==以==的==</p>
    </blockquote>
    <h1 id="_2">自以为很简单的解法</h1>
    <hr />
    <pre><code class="cpp">class Solution
    {
    public:
    	double Power(double base, int exponent)
    	{
    		double res = 1;
    		for(int i = 0; i &lt; exponent; i++)
    		{
    			res *= base;
    		}

    		return res;
    	}
    };
    </code></pre>

    <p>貌似我们已经完美的解决了问题，但是真的这样么？
    我们输入一个指数为负数的情况</p>
    <pre><code class="cpp">    Solution solu;
    	cout &lt;&lt;solu.Power(2, -3) &lt;&lt;endl;
    </code></pre>

    <p>可见我们的算法是多么的自以为是啊？</p>
    <h1 id="_3">简单的处理边界的情况（全面但是不够高效）</h1>
    <hr />
    <p>前面所说的指数为负数只是边界的一种情况，学习算法，必须全面了解所有的边界</p>
    <p>指数幂的所有边界包括</p>
    <ul>
    <li>
    <p>指数为0的情况，不管底数是多少都应该是1</p>
    </li>
    <li>
    <p>指数为负数的情况，求出的应该是其倒数幂的倒数</p>
    </li>
    <li>
    <p>指数为负数的情况下，底数不能为0</p>
    </li>
    </ul>
    <pre><code class="cpp">#include &lt;iostream&gt;
    #include &lt;cmath&gt;
    using namespace std;

    //  调试开关
    #define __tmain main

    #ifdef __tmain

    #define debug cout

    #else

    #define debug 0 &amp;&amp; cout

    #endif // __tmain



    class Solution
    {
    public:
    	double Power(double base, int exponent)
    	{
    		//  指数为0的情况，不管底数是多少都应该是0
    		if(exponent == 0)
    		{
    			return 1.0;
    		}
    		//  指数为负数的情况下，底数不能为0
    		if(Equal(base, 0.0) == true &amp;&amp; exponent &lt; 0)
    		{
    			debug &lt;&lt;&quot;异常, 指数为负数的情况下，底数不能为0&quot; &lt;&lt;endl;
    			return 0.0;
    		}

    		double res = 1.0;
    		if(exponent &gt; 0.0)
    		{
    			res = PowerNormal(base, exponent);
    		}
    		else
    		{
    			res = PowerNormal(base, -exponent);
    			res = 1 / res;
    		}

    		return res;
    	}

    private :
    	double PowerNormal(double base, int exponent)
    	{

    		double res = 1;
    		for(int i = 0; i &lt; exponent; i++)
    		{
    			res *= base;
    		}

    		return res;

    	}
    	double Equal(double left, double right)
    	{
    		if(fabs(left - right) &lt;  0.0000001)
    		{
    			return true;
    		}
    		else
    		{
    			return false;
    		}
    	}
    };



    int __tmain( )
    {
    	Solution solu;

    	cout &lt;&lt;solu.Power(2, 0) &lt;&lt;endl;
    	cout &lt;&lt;solu.Power(2, -3) &lt;&lt;endl;
    	return 0;
    }

    </code></pre>

    <h1 id="_4">位运算（全面而且高效的算法）</h1>
    <hr />
    <p>那么还有没有更加快速的办法呢？</p>
    <p>别急，我们慢慢来分析</p>
    <ol>
    <li>
    <p>写出指数的二进制表达，例如13表达为二进制1101。</p>
    </li>
    <li>
    <p>举例:$10^{1101} = 10^{0001}  \times 10^{0100}  \times 10^{1000}$。 【直接乘上 基数的多少次方】</p>
    </li>
    <li>
    <p>通过&amp;1和&gt;&gt;1来逐位读取1101，为1时将该位代表的乘数累乘到最终结果。</p>
    </li>
    </ol>
    <p>简单明了，看来结果根指数中1的个数和位置有关系，那么就简单了，还记得<a href="http://blog.csdn.net/gatieme/article/details/51122144">剑指Offer--010-二进制中1的个数</a></p>
    <pre><code class="cpp">double PowerNormal(double base, int exponent)
    	{
    		if(exponent == 0)
    		{
    			return 1;
    		}
    		else if(exponent == 1)
    		{
    			return base;
    		}

    		int res = 1, temp = base;
    		while(exponent != 0)
    		{
    			if((exponent &amp; 1) == 1) //  当前指数为不为0
    			{
    				res *= temp;        //  就计算一个乘积
    			}
    			//  移位后, curr需要翻倍, 这样到下个
    			temp *= temp;           // 翻倍
    			exponent &gt;&gt;= 1;         // 右移一位
    		}
    		return res;
    	}
    </code></pre>

    <p>当然也可以用递归的写法</p>
    <p>$a^n =a^{n/2} * a^{n/2} , n 为偶数时$ </p>
    <p>$a^n =a^{n/2} * a^{n/2} \times a , n 为奇数时$ </p>
    <pre><code class="cpp">    double PowerNormal(double base, int exponent)
    	{
    		if(exponent == 0)
    		{
    			return 1;
    		}
    		else if(exponent == 1)
    		{
    			return base;
    		}
    		double res = PowerNormal(base, exponent &gt;&gt; 1);
    		res *= res;
    		/// 判断是奇数还是偶数
    		if((exponent &amp; 1) == 1)
    		{
    			res *= base;
    		}

    		return res;
    	}
    </code></pre>


    <hr/>
    <div class="footer">
    	Copyright &copy; xiaoxiyouran. All rights reserved.

    </div>
'''
    process_highlight(markdown)