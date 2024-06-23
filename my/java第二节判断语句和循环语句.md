# java第二节判断语句和循环语句

## 一、判断语句

1.if语句

基本if-else语句格式为：

```java
if( ){
  else if( ){
    
  }
}
```

常用比较运算符

```java
大于>； 小于<； 大于等于>=； 小于等于<=； 等于==； 不等于!=；
```



条件表达式

```java
与&&； 或||； 非!；
```

2.swicth

基本switch语句格式为：

```java
swicth( ){//填入变量
  case ://填入变量的一种情况
  		//填入为该变量的输出结果
  		break;//跳出全部循环
  case ://填入变量的一种情况
  		//填入为该变量的输出结果
  		break;
  case ://填入变量的一种情况
  		//填入为该变量的输出结果
  		break;
  case ://填入变量的一种情况
  		//填入为该变量的输出结果
  		break;
  case ://填入变量的一种情况
  		//填入为该变量的输出结果
  		break;
  default:
  	//输出没有
}
```

## 二、循环语句

1.while循环

基本语句格式为：

```java
while( ){//括号中为循环条件只要成立就执行循环体中的语句
  
}
```

2.do-while循环

基本语句格式为：

```java
do{//先执行一遍循环体中的语句再与上方while语句一样
  
}while( )
```

3.for循环

基本语句格式为：

```java
for( ; ; ){//三个空分别填入（声明语句/表达式/初始化循环变量或空 ；条件表达式 ；修改循环变量）
  for( ; ; ){//最有用的是可嵌套for循环
    
  }
}
```

3.break与continue

break跳出全部循环；

continue跳出本次循环；

## 三、做题技巧

### 1.生成随机数字

```java
int n = (int) (Math.random() * 101); // 生成一个0到100之间的随机数
```

为什么乘以个101？

1. Math.random(): 返回一个介于 0（包括）和 1（不包括）之间的伪随机浮点数。其范围是 [0, 1)。

2. **乘以 101**: 当你将 Math.random() 的结果乘以 101 时，得到的范围是 [0, 101)。也就是说，生成的浮点数范围是从 0（包括）到 101（不包括）。例如：

​	•	如果 Math.random() 返回 0.0，结果就是 0.0。

​	•	如果 Math.random() 返回 0.9999（接近 1），结果就是大约 100.99。

3. **强制类型转换** int: (int) 会将浮点数截断为整数（去掉小数部分，而不是四舍五入），这样就得到了一个 0 到 100 之间的整数。举例说明：

​	•	如果浮点数是 0.0，强制转换后就是 0。

​	•	如果浮点数是 100.99，强制转换后就是 100。



所以，乘以 101 的目的是确保通过强制转换后，可以覆盖从 0 到 100 的整数范围。由于 Math.random() 产生的值永远小于 1，所以乘以 101 后，最大值也会略小于 101，最终转换成整数时，最大值为 100。



总之，这个乘法操作的目的是确保生成的整数在 0 到 100 之间，包括这两个边界值。

### 2.曼哈顿距离 (用于解决特定问题贴别好用)

定义:

给定平面上两个点  P1(x1, y1)  和  P2(x2, y2) ，它们之间的曼哈顿距离定义为：


曼哈顿距离|a|= |x1 - x2| + |y1 - y2|


其中  |a|  表示  a  的绝对值。

#### 例题

输入一个奇数 n，输出一个由 `*` 构成的 n 阶实心菱形。

#### 输入格式

一个奇数 n。

#### 输出格式

输出一个由 `*` 构成的 n 阶实心菱形。

具体格式参照输出样例。

#### 数据范围

1≤n≤99

#### 输入样例：

```
5
```

#### 输出样例：

```
  *  
 *** 
*****
 *** 
  *  
```

星号*的位置到中心点的“曼哈顿距离” <= n/2 , 其中中心点的坐标为(n/2, n/2)
曼哈顿距离 ： d = |x1 - x2| + |y1 - y2|

#### 解决代码

![image.png](https://cdn.acwing.com/media/article/image/2022/09/23/184605_44c103fc3b-image.png)

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int cx = n / 2, cy = n / 2;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int d = Math.abs(i - cx) + Math.abs(j - cy);
                if (d <= n / 2) System.out.print("*");
                else System.out.print(" "); 
            }
            System.out.println(); 
        }
    }
}
   *        [0,3]
  ***       [1,2]-->[1,4]
 *****      [2,1]-->[2,5]    
*******     [3,0]-->[3,6]  中间的[3,3],曼哈顿距离d 为3的位置都是*    
 *****      ······
  ***  
   *   
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int num = n/2 + 1;
        // 上半部分
        for (int i = 1; i <= num; i++) { // 1到最中间那一行, n/2 + 1 上半部分总行数 设为num 
            for (int j = 1; j <= num - i; j++) System.out.print(" "); // 空格,只用控制*前面的空格数 num - i 
            for (int k = 1; k <= 2*i - 1; k++) System.out.print("*");   // *
            System.out.println(); // 换行
        }
        // 下半部分
        for (int i = n/2; i >= 1; i--) { // 倒着数
            for (int j = 1; j <= num - i; j++) System.out.print(" "); 
            for (int k = 1; k <= 2*i - 1; k++) System.out.print("*"); 
            System.out.println(); 
        }
    }
}
```

