## Linux常用命令  [搜索](https://wangchujiang.com/linux-command/)  
* [文件处理](#文件处理)
* 权限管理
* [文件搜索](#文件搜索)
* 帮助命令
* 用户管理
* 解压命令

* [shell](#shell)

### 文件处理

```
ls -ld /etc 显示目录的详细信息-d
ls -l 显示当前目录中可见文件详细信息
ls -a 显示当前目录中的所有文件（包括隐藏文件）
ls -h 显示易读的文件大小
ls -i 显示节点号
```
```
链接
软链接：相当于快捷方式
硬链接：相当于复制，但是可以同步更新，
       源文件丢失后，硬链接还是可以访问
```
### 文件搜索
```
linux的匹配
*    任意字符
？   单个字符
```
```
搜索查找
大于100M的文件;1kb=2个数据块，1M=1024KB
find / -size +204800

搜索名为a的文件
find / -name a

补充：
locate命令，新建的需要updatedb命令更新，/tmp下的文件找不到
查找命令的位置：which (例：which cp)
```
#### 文件内的搜索
```shell
有加号代表从某行开始，没有加号则是多少行
tail -n 1000：显示最后1000行
tail -n +1000：从1000行开始显示，显示1000行以后的

显示filename文件的3000-3999行
cat filename | tail -n +3000 | head -n 1000

显示filename文件的1000-3000行
cat filename | head -n 3000 | tail -n +1000
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
![Linux常用命令](https://i.ibb.co/ggS8BHD/Linux.jpg)
![Linux常用命令2](https://i.ibb.co/26Kk46Q/Linux-2.jpg)  


<span id="shell"></span>
## shell
* echo
  * `echo -e "a\tb\tc"`
* 快捷键
  * `ctrl+c    强制终止`
  * `ctrl+L    清屏`
  * `ctrl+u    删除当前输入行`
* 输入输出重定向
  * `命令 >> 文件1 2>>文件2    正确输出保存在文件1，错误输出保存在文件2`
  * `命令 &> 文件    保存错误和正确的输出（&>:覆盖；&>>:追加）`
