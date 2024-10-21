# 使用Github配置个人图床

## 1.为何要使用Github

某天打开博客，所有通过免费图床上传的图片全部无法正常显示，跳转链接去看发现图床倒了，而大部分都是freestyle的截图并没有本地备份，这才后知后觉以前心血成为飞灰。这才萌生了索性迁移博客并且把图片上传到Github的想法。同时，也学习一下通过Github仓库部署博客，毕竟免费的资源谁说不香呢。

## 2.关于配置图床的记录

这里学习并参考的许多前辈的文章，以下是配置的流程：

管理工具使用了[PicList](https://piclist.cn/)，此工具可以方便的管理仓库内图片的增删。

参考：

[通过 Github + jsDelivr + PicGo 配置免费图床](https://ilaozhu.com/archives/2063/)

[Github图床搭建，结合Picgo与jsdelivr的免费cdn加速，以及部分问题解决方案](https://www.cnblogs.com/MorningMaple/p/17978113)

[教你如何使用github+jsDelivr搭建免费图床](https://www.cnblogs.com/starry-skys/p/13905766.html)

[CDN jsdelivr加速github图床](https://finisky.github.io/speedupgithubbycdn/)

### 2.1 Github仓库配置

网址：[Github](https://github.com/)

新建一个**公开**(Public)仓库：

<img src="https://cdn.jsdelivr.net/gh/Pennicc/imag-repostioty@main/blog/1728204316298-34af36d47bf5df48.png" style="zoom:30%;" />

创建一个新的供管理工具访问的`token`：

<img src="https://cdn.jsdelivr.net/gh/Pennicc/imag-repostioty@main/blog/1728204386846-3513d10d17ed3965.png" style="zoom:33%;" />

<img src="https://cdn.jsdelivr.net/gh/Pennicc/imag-repostioty@main/blog/1728204429357-90fb5b82f5d19838.png" style="zoom:40%;" />

<img src="https://cdn.jsdelivr.net/gh/Pennicc/imag-repostioty@main/blog/1728204593174-a8d9400c31dfb669.png" style="zoom:50%;" />

范围勾选`repo`：

<img src="https://cdn.jsdelivr.net/gh/Pennicc/imag-repostioty@main/blog/1728204641880-a4e7dcc0458dafab.png" style="zoom:40%;" />

生成`token`并保存：

<img src="https://cdn.jsdelivr.net/gh/Pennicc/imag-repostioty@main/blog/1728204731054-51074fc894c1f9b2.png" style="zoom:50%;" />

~~（因为之前生成了一个，这个仅供测试，一会儿删除，就不打码了）~~

值得注意的是，token生成之后只显示这一次，要尽快复制保存。

### 2.2 配置PicList工具

网址：[PicList](https://piclist.cn/)

个人认为PicList相较于其他工具的优点是可以通过简单的配置自动实现cdn加速。

下载并安装PicList，完成后打开：

<img src="https://cdn.jsdelivr.net/gh/Pennicc/imag-repostioty@main/blog/1728204910587-d27780f8f9ba7178.png" style="zoom:50%;" />

设置Github图床，按要求填写相关配置：

<img src="https://cdn.jsdelivr.net/gh/Pennicc/imag-repostioty@main/blog/1728204962823-5acf4bd1e32a16da.png" style="zoom:50%;" />

## 3.使用jsdelivr加速

地址：[jsdelivr](https://www.jsdelivr.com/?docs=gh)

```
https://cdn.jsdelivr.net/gh/Github用户名/仓库名@main
https://fastly.jsdelivr.net/gh/Github用户名/仓库名@main
```

------

至此，基于Github的图床便设置完成。
