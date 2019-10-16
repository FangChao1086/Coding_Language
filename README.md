# Coding_language
* [C++](https://github.com/FangChao1086/Coding_language/blob/master/C%2B%2B.md)
* [python](https://github.com/FangChao1086/coding_language/tree/master/python)
* [mysql常用命令](https://mp.weixin.qq.com/s/wUCVeYLxx5JL2Xy-XJNvNQ)  
* Linux常用命令  [详细命令搜索](https://wangchujiang.com/linux-command/)  
  * 文件处理
  * 权限管理
  * 文件搜索
  * 帮助命令
  * 用户管理
  * 解压命令
* [shell](#shell)
```
查看目录的详细信息-d
ls -ld /etc
```
```
链接
软链接：相当于快捷方式
硬链接：相当于复制，但是可以同步更新，
       源文件丢失后，硬链接还是可以访问
```
```
linux的匹配
*    任意字符
？   单个字符
```
```
搜索查找
大于100M的文件;1kb=2个数据块，1M=1024KB
find / -size +204800

补充：
locate命令，新建的需要updatedb命令更新，/tmp下的文件找不到
查找命令的位置：which (例：which cp)
```

```
帮助命令：
man(例：man ls)；
搜索特定的字符所在位置：/+字符（例：/-a）;
翻页：按键n
```

```
用户管理
useradd;passwd;who;w
```

```
解压命令
tar参数详细信息：
    -x 解包  -c 压包
    -v 显示详细信息
    -f 指定解压文件
    -z 解压缩
```

```
用户切换
su - root  -表示连带环境一起切换，最好不要省略
```

<span id="shell"></span>
## shell
* echo
  * `echo -e "a\tb\tc"`

![Linux常用命令](https://i.ibb.co/ggS8BHD/Linux.jpg)
![Linux常用命令2](https://i.ibb.co/26Kk46Q/Linux-2.jpg)
