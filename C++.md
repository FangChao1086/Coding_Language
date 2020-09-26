<span id="back"></span>
# C++
[参考链接：C++面试知识点详细](https://github.com/huihut/interview)

[参考链接：C++面试常见问题](https://blog.csdn.net/u012864854/article/details/79777991)  

[参考链接：STL标准库常见面试题](https://blog.csdn.net/xiongluo0628/article/details/81546197)  

[参考链接：牛客C++面试宝典](https://www.nowcoder.com/tutorial/93/509ef14094564a758193396b8e110228)

* [C++11新特性](#C++11新特性)
* [STL标准库](#STL标准库)
* [C++内存管理](#C++内存管理)
* [const](#const)
* [static关键字](#static关键字)
* [this指针](#this指针)  
* [inline内联函数](#inline内联函数)  
* [volatile](#volatile)  
* [虚函数和纯虚函数](#虚函数和纯虚函数)
* [C++多态](#C++多态)
* [指针与引用](#指针与引用)
* [new/delete和malloc/free](#new和malloc)
* [异步与实现方式](#异步与实现方式)
* [重载与重写](#重载与重写)
* [类成员的访问权限](#类成员的访问权限)
* [友元函数](#友元函数)
* [struct和class](#struct和class)
* [sizeof](#sizeof)
* [大端小端](#大端小端)

<span id="C++11新特性"></span>
## [C++11新特性](#back)
* `auto`关键字 
  * 分析表达式所属的类型
* `nullptr`
  * 初始化空指针（空指针：不指向任何对象的指针）
  * 可以转换为其他任意类型指针
  * NULL一般被宏定义为0，在遇到重载时可能会出现问题
* 智能指针：std::shared_ptr、std::weak_ptr
  * 作用：自动释放所指向的对象 
  * 解决的问题：在内存管理中，1、忘记释放内存 2、尚有指针引用的情况下释放了内存
  * `Shared_ptr`可以让多个智能指针指向同一个对象
  * `unique_ptr`只容许一个指针独自指向一个对象。
* 初始化列表：使用初始化列表来对类进行初始化
* 右值引用
  * 基于右值引用可以实现移动语义和完美转发
  * 消除两个对象交互时不必要的对象拷贝，节省运算存储资源，提高效率
* 范围`for`语句
  * `for(auto c : vec)`
* `lambda`表达式

<span id="STL标准库"></span>
## [STL标准库](#back)
**STL的构成：分配器 容器 算法 迭代器 仿函数 配接器**
* 分配器给容器分配存储空间
* 算法通过迭代器获取容器中的内容
* 仿函数可以协助算法完成各种操作
* 配接器用来套接适配仿函数
### 常用容器
* **vector  序列容器**  **连续内存**
  * 底层结构：数组
  * **适用场景：经常随机访问，且不经常对非尾节点进行插入删除**
  * **两倍容量增长**：当分配的空间不够装下数据时，分配双倍于当前容量的存储区，把当前的值拷贝到新分配的内存中，并释放原来的内存。
  * 在插入位置和删除位置之后的所有迭代器和指针引用都会失效，同理，扩容之后的所有迭代器指针和引用也都会失效。
  * 在中间节点进行插入删除会导致内存拷贝
* deque  序列容器
* **List**   **不连续内存**
  * 底层结构：双向链表
  * **适用场景：经常插入删除大量数据**
  * 每插入一个元素都会分配空间，每删除一个元素都会释放空间。
* priority_queue
  * 有权值的单向队列，根据堆来调整
* map  关联容器
  * 底层结构：红黑树
  * 适用场景：**有序**键值对**不重复**映射
* multimap  
  * 底层结构：红黑树 
  * 适用场景：**有序**键值对**可重复**映射
* unordered_map
  * 底层结构：哈希表
* set  关联容器
  * 底层：红黑树  有序存储，  不重复
* multiset  
  * 底层：红黑树  有序存储，  可重复
### 哈希冲突的解决办法
* **拉链法**  关键字相同的节点连接在同一链表中
* **开放定址法**  发生冲突时，寻找下一个地址
  * 线性探测 1, 2, 3, ...
  * 二次探测 12, -12, 22, -22, 32, -32
  * 随机探测 伪随机数发生器
* **再散列法**  多个哈希函数，当哈希函数1发生冲突时，计算函数2，...直到不发生冲突

<span id="C++内存管理"></span>
## [C++内存管理](#back)
* **栈**：*存放函数参数与局部变量*  
* **堆**：new所申请的内存区域在堆上
* **自由存储区**：new所申请的内存区域在C++中称为自由存储区
* **全局/静态存储区**：*保存自动全局变量和static变量*  
* **常量存储区**：*此存储区不可修改，常量（const）存在此处*  

### 虚拟内存
在C++中，虚拟内存分为代码段、数据段、BSS段、堆区、文件映射区以及栈区六部分
* 代码段：包括只读存储区和文本区，其中只读存储区存储字符串常量，文本区存储程序的机器代码。
* 数据段：存储程序中已初始化的全局变量和静态变量
* bss 段：存储未初始化的全局变量和静态变量（局部+全局），以及所有被初始化为0的全局变量和静态变量。
* 堆区：调用new/malloc函数时在堆区动态分配内存，同时需要调用delete/free来手动释放申请的内存。
* 映射区：存储动态链接库以及调用mmap函数进行的文件映射
* 栈：使用栈空间存储函数的返回地址、参数、局部变量、返回值

### 堆栈的区别：栈的效率高，堆灵活  
* **管理方式不同**：堆需手动释放  
  * 栈是编译器自动管理的,堆需手动释放  
* **空间大小不同**：堆大  
  * 在32位OS下,堆内存可达到4GB的的空间,而栈就小得可怜.(VC6中,栈默认大小是1M,当然,你可以修改它)  
* **能否产生碎片不同**：堆会产生碎片  
  * 对于栈来说,进栈/出栈都有着严格的顺序(先进后出),不会产生碎片;而堆频繁的new/delete,会造成内存空间的不连续,容易产生碎片.  
* **生长方向不同**  
  * **栈向下生长**,以降序分配内存地址;**堆向上生长**,以升序分配内在地址.  
* **分配方式不同**  
  * **堆动态分配**,无静态分配;栈分为静态分配和动态分配,比如局部变量的分配,就是动态分配(alloca函数),函数参数的分配就是动态分配(我想的…).  
* **分配效率不同**：栈的效率高  
  * 栈是系统提供的数据结构,计算机会在底层对栈提供支持,进栈/出栈都有专门的指令,这就决定了栈的效率比较高.堆则不然,它由C/C++函数库提供,机制复杂,堆的效率要比栈低得多.  

### 定义一个只能在堆上（栈上）生成对象的类
* 只能在堆上
  * 将析构函数设置为私有
* 只能在栈上
  * 将 new 和 delete 重载为私有

## [const](#back)
* 修饰变量
  * 该变量不可变
* 修饰指针
  * 指向常量的指针  const int* function()
  * 自身是常量的指针  int* const function();  
* 修饰引用
  * 指向常量的引用
  * 用于形参类型，避免了拷贝，又避免了函数对值的修改
* 修饰成员函数
  * 该成员函数内不能修改成员变量

```cpp
// const的使用

// 类
class A
{
private:
    const int a;                // 常对象成员，只能在初始化列表赋值

public:
    // 构造函数
    A() : a(0) { };
    A(int x) : a(x) { };        // 初始化列表

    // const可用于对重载函数的区分
    int getValue();             // 普通成员函数
    int getValue() const;       // 常成员函数，不得修改类中的任何数据成员的值
};

void function()
{
    // 对象
    A b;                        // 普通对象，可以调用全部成员函数、更新常成员变量
    const A a;                  // 常对象，只能调用常成员函数
    const A *p = &a;            // 指针变量，指向常对象
    const A &q = a;             // 指向常对象的引用

    // 指针
    char greeting[] = "Hello";
    char* p1 = greeting;                // 指针变量，指向字符数组变量
    const char* p2 = greeting;          // 指针变量，指向字符数组常量
    char* const p3 = greeting;          // 自身是常量的指针，指向字符数组变量
    const char* const p4 = greeting;    // 自身是常量的指针，指向字符数组常量
}

// 函数
void function1(const int Var);           // 传递过来的参数在函数内不可变
void function2(const char* Var);         // 参数指针所指内容为常量
void function3(char* const Var);         // 参数指针为常量
void function4(const int& Var);          // 引用参数在函数内为常量

// 函数返回值
const int function5();      // 返回一个常数
const int* function6();     // 返回一个指向常量的指针变量，使用：const int *p = function6();
int* const function7();     // 返回一个指向变量的常指针（自身是常量的指针），使用：int* const p = function7();
```

## [static关键字](#back)
* 同时编译多个文件时，
  * 所有未加static前缀的全局变量和函数对其他文件可见
  * 加了static关键字的变量和函数可对其它源文件隐藏
* static定义的静态局部变量分配在数据段上，不会跟普通的局部变量随着栈的释放而释放
* 类的静态数据成员
  * 不依赖于对象，依赖于类
  * **在对象诞生之前，静态数据成员在内存中就已经存在**
  * 普通的数据成员需要实例化后才存在
* 类静态成员函数
  * 无法调用普通数据成员和普通成员函数，可以调用静态数据成员和静态成员函数
补充：加了static前缀的变量默认初始值为0

## [this指针](#back)
* this 指针是一个隐含于每一个非静态成员函数中的特殊指针，它指向调用该成员函数的那个对象
* 当对一个对象调用成员函数时，编译程序先将对象的地址赋给 this 指针，然后调用成员函数，每次成员函数存取数据成员时，都隐式使用 this 指针。
* this 并不是一个常规变量，而是个右值，所以不能取得 this 的地址（不能 &this）
* 显示引用 this 指针的场景：
  * 为实现对象的链式引用；
  * 为避免对同一对象进行赋值操作；
  * 在实现一些数据结构时，如 list。

## [inline内联函数](#back)
* 相当于把内联函数直接写在调用内联函数处
* 相当于不用执行进入函数的步骤，直接执行函数体
* **相当于宏，但比宏多了类型检查**，真正具有函数特性
* 编译器一般**不内联包含循环、递归、switch 等**复杂操作的内联函数
* 在类声明中定义的函数，除了虚函数的其他函数都会自动隐式地当成内联函数。

## [volatile](#back)
* volatile 关键字声明的变量，每次访问时都必须从内存中取出值（没有被修饰的可能由于编译器的优化，从cpu取值）
* const、指针都可以是volatile

## [虚函数和纯虚函数](#back)
* 虚函数可以直接使用，也可以被子类重写后以多态形式调用
* 纯虚函数必须在子类中实现该函数才可使用，因为**纯虚函数在基类中只有声明没有定义**
* 虚函数必须实现，对虚函数来说父类和子类都有各自的版本
* **虚函数可以是内联函数，虚函数表现多态性时不能内联**
* **构造函数不能是虚函数**（必须要构造函数调用完成后才会形成虚表指针）
> 抽象类：含有纯虚函数的类  
> 非抽象类：只含有虚函数的类
### 虚函数原理
**虚函数是依赖于虚函数指针实现，每个拥有虚函数的类都有一个虚表，类的对象存在一个虚函数表指针，指向实际类型的虚表。虚函数运行的时候，会根据虚函数表指针找到正确的虚表（虚表中存放一个个函数指针），从而执行正确的虚函数。**

**<details><summary>抽象类与接口</summary>**
 
* 抽象类
  * **含有纯虚函数的类**
  * 无法实例化对象，子类也有可能是抽象类
  * 抽象类可以实现接口
* 接口
  * 接口类更多的表达是一种能力或者协议
  * **接口中只能有抽象方法，即没有具体实现的方法**
  * 接口可以继承多个接口，不能继承或实现抽象类
</details>

<span id="C++多态"></span>
## [C++多态](#back)
* **静态多态**
  * 通过重载与模板实现，在编译的时候确定
* **动态多态**
  * 通过虚函数与继承关系实现， 在运行的时候确定
  * 动态多态实现的条件
    * 虚函数
    * 一个基类的指针或引用指向派生类的对象

<span id="指针与引用"></span>
## [指针与引用](#back)
### 指针
& ：每一个变量都有一个内存位置，内存位置定义了可使用&访问的地址
```cpp
int  var1;
char var2[10];
cout << "var1 变量的地址： ";
cout << &var1 << endl;
cout << "var2 变量的地址： ";
cout << &var2 << endl;

// var1 变量的地址： 0xbfebd5c0
// var2 变量的地址： 0xbfebd5b6
```
指针：一个变量，其值是另一个变量的地址；`a`: 表示地址，`*a`: 表示地址中的值
```cpp
int  var = 20;   // 实际变量的声明
int  *ip;        // 指针变量的声明
ip = &var;       // 在指针变量中存储 var 的地址
cout << "Value of var variable: ";
cout << var << endl;
// 输出在指针变量中存储的地址
cout << "Address stored in ip variable: ";
cout << ip << endl;
// 访问指针中地址的值
cout << "Value of *ip variable: ";
cout << *ip << endl;

// Value of var variable: 20
// Address stored in ip variable: 0xbfc601ac
// Value of *ip variable: 20
```
#### 空指针
NULL指针表示值为0的常量，**不指向任何对象**
```cpp
int  *ptr = NULL;
cout << "ptr 的值是 " << ptr ;

// ptr 的值是 0
```
#### 指针的加减
```cpp
const int MAX = 3;
int  var[MAX] = {10, 100, 200};
int  *ptr;
// 指针中的数组地址
ptr = var;
for (int i = 0; i < MAX; i++)
{
   cout << "Address of var[" << i << "] = ";
   cout << ptr << endl;
   cout << "Value of var[" << i << "] = ";
   cout << *ptr << endl;
   // 移动到下一个位置
   ptr++;
}

// Address of var[0] = 0xbfa088b0
// Value of var[0] = 10
// Address of var[1] = 0xbfa088b4
// Value of var[1] = 100
// Address of var[2] = 0xbfa088b8
// Value of var[2] = 200
```

### 引用：创建时就需要初始化
& 读作引用
```cpp
// 声明简单的变量
int    i;
double d;
// 声明引用变量
int&    r = i;
double& s = d;
i = 5;
cout << "Value of i : " << i << endl;
cout << "Value of i reference : " << r  << endl;
d = 11.7;
cout << "Value of d : " << d << endl;
cout << "Value of d reference : " << s  << endl;

// Value of i : 5
// Value of i reference : 5
// Value of d : 11.7
// Value of d reference : 11.7
```

<span id="new和malloc"></span>
## [new/delete和malloc/free](#back)
* **new/delete是C++的关键字，malloc/free是c语言的库函数**
* **new/delete会调用构造、析构函数，malloc/free不会**，所以他们无法满足动态对象的要求
* malloc/free 必须指明申请内存空间大小
* new返回有类型的指针，malloc返回无类型的指针
* new失败抛异常，malloc失败返回空
### new/delete的底层实现
* new
  * 调用底层全局函数operator new来申请空间
  * 在申请的空间上执行构造函数，完成对象的构造
* delete
  * 在空间上执行析构函数，清理对象中资源
  * 调用全局函数operator delete来释放对象的空间

## [异步与实现方式](#back)
* **异步**
  * **当一个异步过程调用发出后，调用者不能立刻得到结果**。实际上处理这个调用的部件在完成后，通过**状态 、通知和回调**来通知调用者
* 实现方式
  * 可以使用哪种方式依赖于执行部件的实现，除非执行部件提供多种选择，否则不受调用者控制。
  * 若执行部件用状态的方式，效率低（调用者需要每隔一段时间检查状态一次）
  * 通知的方式，效率高（几乎不需要做额外的操作）
  * 回调函数，与通知类似

## [重载与重写](#back)
* 重写：**有继承关系**，对虚函数的重写
* 重载：**没有继承关系**，同名函数参数表不同
* 多态：**包括重载与重写**，同名函数同参数表，类型不同
* 重定义与隐藏：子类对父类的非虚函数再写一遍

## [类成员的访问权限](#back)
* 成员访问限定符
  * public
  * protected
  * private
* 类内访问：都可访问
* 类外：通过对象访问成员
  * 父类对象实例可访问 public 成员，禁止访问 protected 和 private 成员
  * 子类可访问父类中的 protected 成员

## [友元函数](#back)
* 定义在类外部，但有权访问类的所有私有成员和保护成员
```cpp
#include <iostream>
 
using namespace std;
 
class Box
{
   double width;
public:
   friend void printWidth(Box box);
   void setWidth(double wid);
};
 
// 成员函数定义
void Box::setWidth(double wid)
{
    width = wid;
} 
// 请注意：printWidth() 不是任何类的成员函数
void printWidth(Box box)
{
   /* 因为 printWidth() 是 Box 的友元，它可以直接访问该类的任何成员 */
   cout << "Width of box : " << box.width <<endl;
}
 
// 程序的主函数
int main( )
{
   Box box;
   box.setWidth(10.0);  // 使用成员函数设置宽度
   printWidth(box);  // 使用友元函数输出宽度
   return 0;
}
```

<span id="struct和class"></span>
## [struct和class](#back)
struct 默认继承权限和默认访问权限是 public  
class 默认继承权限和默认访问权限是 private  
* **默认的继承访问权** 取决于子类，struct：public；class：private；
  ```cpp
  struct A
  {
   int a;
  };

  struct B: A   //共有继承
  {
   int b;
  };
  class C: A    //私有继承
  {
   int c
  };
  ```
* **默认的访问权限**
  ```cpp
  struct A
  {
   int a;
  };
  
  class B
  {
   int b;
  };
  
  int main()
  {
   A n;
   n.a = 10;  //可在结构外访问成员变量，所以struct默认是共有的
   B n1;
   n1.b = 10;  //在类外无法访问私有变量
   return 0;
  }
  ```

<span id="sizeof"></span>
## [sizeof](#back)  [用法介绍](https://www.cnblogs.com/huolong-blog/p/7587711.html)
* 字节数
  * char 1
  * int 4
  * float 4
  * double 8
* 结构的sizeof
  ```cpp
  struct S2  
  {  
    int b;  
    char a;  
  };  
  sizeof(S2);  // 值为8，字节对齐，在char之后会填充3个字节。  

  struct S3  
  {  
  };  
  sizeof(S3);  // 值为1，空结构体也占内存
  ```
* 联合体的sizeof
  ```cpp
  union u  
  {  
      int a;  
      float b;  
      double c;  
      char d;  
  };  

  sizeof(u);  // 值为8;每个成员sizeof的最大值  
  ```
* 数组的sizeof
  ```cpp
  char a[10];  
  char n[] = "abc";   
  cout<<"char a[10]"<<sizeof(a)<<endl;//数组，值为10  
  cout<<"char n[] = /"abc/""<<sizeof(n)<<endl;//字符串数组，将'/0'计算进去，值为4
  
  // 作为形参
  void func(char a[3])  
  {  
    int c = sizeof(a); //c = 4，因为这里a不在是数组类型，而是指针，相当于char *a。  
  }  
  ```

## [大端小端](#back)
比如 0x12345678 这个数：
* 大端法在内存中按字节依次存放为：12 34 56 78
* 小端法在内存中按字节依次存放为：78 56 34 12

大端：较高的有效字节存放在较低的存储器地址，较低的有效字节存放在较高的存储器地址。  
比如整型变量 0x12345678 占 4 个字节，那么根据内存地址从小到大它们的存放方式如下：  

|数据|0x12|0x34|0x56|0x78|
|-|-|-|-|-|
|地址|0x10000000|0x10000001|0x10000002|0x10000003|


小端：较高的有效字节存放在较高的的存储器地址，较低的有效字节存放在较低的存储器地址。  
整型变量 0x12345678 根据内存地址从小到大它们的存放方式如下：

|数据|0x78|0x56|0x34|0x12|
|-|-|-|-|-|
|地址|0x10000000|0x10000001|0x10000002|0x10000003|
