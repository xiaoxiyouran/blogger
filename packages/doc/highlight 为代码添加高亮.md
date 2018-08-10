# 用 highlight.js 为文章中的代码添加语法高亮

如果我们的文章中包含了代码，Ghost 默认是不做处理的，也就是说：没有为代码增加语法高亮。

其实，这个问题可以从 Ghost 系统入手解决，可惜现在 Ghost 还不支持插件，如果直接修改 Ghost 系统的话，每次系统升级都会很麻烦；那么，我们只好在页面上解决这个问题了，也就是为主题（theme）增加语法高亮的支持，在这里，我们以 Ghost 的默认主题（theme）-- Casper -- 为例，语法高亮插件采用 [highlight.js ](https://highlightjs.org/)。

先来看看 highlight.js 有什么能力吧：

支持 71 种编程语言的语法解析；拥有 44 种样式
自动检测编程语言
同时为多种编程语言代码高亮
可以在 node.js 平台上运行
支持各种标签
与任何 js 框架兼容
OK，接下来就看看怎么用 hightlight.js 吧！

使用方法: [highlight.pdf](highlight.pdf) 


另一种方式是使用[Prism.pdf](Prism.pdf)