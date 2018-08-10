# project organization build

对于以下几种工程组织结构如下：
- 仅有 source 源码
- 仅有 doc 文档
- 两种都有 （更普遍）

一般如下：

```
.
├── packages (生成文档必备的包 + 工程模板)
├── project_doc_src
│   ├── project_independent1 (参照源 project_source 目录 )
│   │   └── main.md
│   └── project_independent2 (参照源 project_source 目录 )
│       └── main.md
├── project_docs (生成的文档所在地，预留)
├── project_organization.md (项目组织的complement report)
└── project_source
    ├── project_independent1 (放第三方开发工具如CLion 等单独的工程)
    │   └── main.cpp
    └── project_independent2 (第二个工程)
        └── main.cpp
```
当需要建立工程的时候，可以复制该目录。在 [./packages/xxxNET_project_template](../xxxNET_project_template) 目录下。  
