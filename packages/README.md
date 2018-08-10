# 一条指令转换所有markdown 文档 

为了将markdown 批量转换成`html` 文档，并生成结构树方便查询和管理，自写脚本`main.py`来实现

使用 PyCharm IDE 调试的输入参数是：`../src ../doc`

## 使用  
将`packages`文件夹复制到`markdown`文档所在的目录。文档结构应该如下：  

```
.
├── docs
├── packages
└── src
```

其中， `packages` 是本软件所在的一些包， `src`里面是`.md`所在的文档。 如果上层目录不是`src`，可以自行在`Makefile`里设置。  
`docs`目录是`Makefile`里指定生成的目标目录。默认是`output` 目录。最好指定，要不然，可能结构会乱。但经过测试，本软件还是能很好的支持。

使用: 

	make
 
如果要重新生成： 	

	make clean;
    make
    
## 注意   

1- 首先需要`python2x`的支持  
2- 安装了 `make` ，没有的话，自己手动敲`Makefile` 里的指令 
3- `srcum`文档结构组织如下：  
`.md` 是说明文档，`.pdf`是网上下的参考， `unmd`文件加里存放的软件或者其它杂料会被跳过，不会复制，也不会处理，将使生成的文档更加简洁。
```
.
├── function.md
├── reference_From_Internet.pdf
└── unmd
    ├── soft
    └── softwares


```

## 开发  
`resources`文件夹下，有三个文件：  
其中，大部分参考的是`ssdb-doc.tar.gz`这个项目，解压开就能用。其中`markdown`文档的转换基本都是这里面的。  
`jquery-tree.zip`是花里10块钱在网上买的，主要是生成侧边栏文档目录树(`sidebar`)   
`黑色平铺布局.tar.gz`也是那个网站上趴的一个能平铺显示所有的文件，算是一个还不错的例子，我没怎么用。后期有需要再追加。

```
.
├── jquery-tree.zip
├── ssdb-doc.tar.gz
└── 黑色平铺布局.tar.gz

```