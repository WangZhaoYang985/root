# java第一节变量、运算符、表达式、输入和输出

## <font color=orange>变量、运算符、表达式</font>

1. 1byte=8 bit=01010111;对应着2^8=256种情况(<font color=red>正负个一半</font>);

2. | 变量             | 字节 |                   范围                   |
	| :--------------- | :--: | :--------------------------------------: |
	| Byte             |  1   |                 2^8=256                  |
	| short            |  2   |               2^16=65,536                |
	| Int              |  4   |                 2.1*10^9                 |
	| Long             |  8   |                  10^18                   |
	| Float            |  4   |     有效数字6-7位，显示地表示加1.0f      |
	| double           |  8   |    有效数字15-16位，显示地表示加1.0d     |
	| boolean          |  1   |                True/false                |
	| Char             |  2   | 'A'可转化为整数(ascii),A 65; a 97; 0 48; |
	| 精度由低到高排列 | 顺序 |  Byte<short<char<int<long<float<double   |
	
3. 强制类型转化(可大转小),且范围小的优先转化为范围大的；

	Char c = '1';  <font color=orang>显示</font>

	Int  c = (int) c;

	Double x = 12; <font color=orang>隐式</font>

	Double y=4*3.3;
	
	<font style=background:yellow>final</font> int x=1;(<font color=red>常量不能修改</font>)

  4.运算符与表达式

 	 1." / "向零取整C++/java,向下取整python。
 	
 	2." "双引号表示字符串 ，‘ ’表示字符

​	  3.a + " "整数+字符串默认将整数转化为字符串

​          4.println只能输出一个数据

​	  5.字符串的比较，计算两个数差值的绝对值。

```java           
double x=1,y=2;

 if(Math.abs(x-y)<1e^-6);//就认为相等
```

## <font color=gree>输入输出</font>

1.模版

```java
import java.util.Scanner;
public class Main{
  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    System.out.println();//System.out.printf("%d",x);
  }
}
```

2.输入

<font style=background:yellow>如何获取输入？</font>

<font color=red>先获取一个包:</font>

```java
import java.util.Scanner;
/*在Java中，为了避免资源泄漏，通常会使用try-with-resources语句来自动管理资源，确保在代码执行完毕后资源能够被自动关闭。*/
try(Scanner sc = new Scanner(System.in))//// 使用sc进行输入操作
{
String str = sc.next();//遇到空白字符(空格、回车、制表符等)结束；
String str = sc.nextLine();//读入一行
int x = sc.nextInt(),y = sc.nextInt();
} // sc在这里会自动关闭
```

<font style=background:yellow>如果输出数据超过10^5,用</font>

```java
import java.io.BufferedReader;
import java.io.InputStreamReader;
public class Main{
	public static void main(String[] args)throws Exception{//抛除异常操作
 		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
 		String str = br.readLine();
    int x = Integer.parseInt(br.readLine());//为3 4分行；
    String[] strs =readLine(),split("");//若3 4在一行得切割,进行如下处理；
    int x=Interger.parseInt(strs[0]);
    int y=Interger.parseInt(strs[1]);
  }
}
```

3.输出

```java
System.out.println();//ln回车；
System.out.printf("%4d%.2f/n,4,123.456");//格式化输出；
```

​	%4d(<font style=background:yellow>补空格在前面补</font>);             %-4d(<font style=background:yellow>补空格在后面补</font>);           %.3f(<font style=background:yellow>保留3位小数</font>);

<font style=background:yellow>若输出特别多</font>

```java
import java.io.BufferedWriter;
import java.io.InputStreamWriter;
public class Main{
	public static void main(String[] args)throws Exception{//抛除异常操作
 		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    bw.write("Hello world");
    bw.flush();//刷新一下缓冲区；
```

## 做题技巧

当要在一行内输入两种不同类型的数时：

```java
sc.next();//读取并丢弃一个输入项，通常是一行文本中的下一个单词。如果输入项之间由空格分隔，那么这个单词就是下一个单词。
int a=sc.nextInt();
double b=sc.nextDouble();
sc.next();//再次读取并丢弃一个输入项。
int c=sc.nextInt();
double d=sc.nextDouble();
```



当double数据要求到很小值会数据不精确：

```java
 n += 1e-8;//加上一个1e-8,改变精度问题
```





