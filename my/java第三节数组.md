# java第三节 数组

### 1.基本结构

```java
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
      	int[] a = new int[10], b;//b也定义为了一个数组但是为0；
        int[] c = {0, 1, 2};        // 含有3个元素的数组，元素分别是0, 1, 2；  
        int[] d = new int[3];       // 含有3个元素的数组，元素的值均为0
        for (int i = 0; i < 3; i ++ )//用for循环来批量输入(量多的时候的输入输出方式)；
            d[i] = sc.nextInt();
        float[] e = new float[33];
        double[] f = new double[123];
        char[] g = new char[21];
      	char[] h = {'a', 'b', 'c'}; // 字符数组的初始化
      	System.out.printf("%d %d %d\n", c[0], c[1], c[2]);//输出(一般的时候的输入输出方式)；
    }
}
```

### 2.多维数组

```java
        int[][] a = new int[3][4]; // 大小为3的数组，每个元素是含有4个整数的数组。
        int[][][] b = new int[10][20][30]; // 将所有元素的初值为0
        // 大小为10的数组，它的每个元素是含有20个数组的数组
        // 这些数组的元素是含有30个整数的数组
			  for (int i = 0; i < 3; i ++ ) {  // 输出二维数组
             for (int j = 0; j < 4; j ++ ) {//使用嵌套循环来输出 
                System.out.printf("%d ", a[i][j]);
            }
            System.out.println();
        }
```

#### 为二维数组准备的增强for循环

```java
        // 使用增强型for循环遍历二维数组的每一行
        for (int[] row: a) {  // 范围遍历
            // 使用增强型for循环遍历当前行的每一个元素
            for (int x: row)  // 范围遍历
                // 格式化输出每个元素，元素间用空格隔开
                System.out.printf("%d ", x);
            // 每行结束后换行
            System.out.println();
        }
```

**代码解析**



​	1.	for (int[] row: a):

​	•	这个增强型 for 循环用于遍历二维数组 a 的每一行。

​	•	a 是一个二维数组，其每个元素 row 都是一个一维数组。

​	•	在每次循环迭代中，row 被赋值为 a 数组中的下一行。

​	2.	for (int x: row):

​	•	在上一行代码的基础上，这个循环用于遍历当前行 row 中的每个元素。

​	•	row 是一个一维数组，其每个元素是 int 类型的整数。

​	•	在每次循环迭代中，x 被赋值为 row 数组中的下一个整数。



**作用**



​	•	外层 for 循环逐行读取二维数组 a 的内容。

​	•	内层 for 循环逐个访问当前行 row 中的每个整数，并执行相应的操作（在此代码中是打印输出）。



这种方式比传统的基于索引的 for 循环更简洁，更直观，特别是在不需要访问元素的索引时。

### 3.常用API

#### 1.属性length：返回数组长度，注意不加小括号

```java
import java.util.Scanner;
public class Main{
  public static void main(System[] args){
		int [][] a={
      {1,2,3},
      {4,5,6},
      {7,8,9}
    };
    System.out.println(a.length);//输出外侧二维数组的长度即3；
    for(int i=0;i<3;i++){
       System.out.println(a[i].length);//输出内侧一维数组的长度即3，3，3；
    }
  }
}
```

#### 2.Arrays.sort()：数组排序与Arrays.toString()：将数组转化为字符串和Arrays.deepToString()：将多维数组转化为字符串    <font color=red>注：使用Arrays需要加import java.util.Arrays</font>

```java
import java.util.Scanner;
import java.util.Arrays;
public class Main{
  public static void main(System[] args){
    int [] q={5,3,2,1,4}
    Arrays.sort(q);//将q排好序;
    System.out.println(Arrays.toString(q));//将排好序的q转化为字符输出出来;
  }
}
```

##### 如果想要倒序排列：

·需要调用比较函数 就不能使用基本类型，数组得为对象不能使用基本类型；

```java
import java.util.Scanner;
import java.util.Arrays;
public class Main{
  public static void main(System[] args){
    Integer [] q={5,3,2,1,4}//Integer为int的对象;
    Arrays.sort(q,(x,y) ->{//加入比较函数，比较函数中传入两个值x,y;
      return y-x;//return x-y若返回值为负数x要排到y的前面即x小于y反则易知
    });//,所以将x-y反转即可为逆序排列；
    System.out.println(Arrays.toString(q));//将排好序的q转化为字符输出出来;
  }
}
```

·如此二维数组也可排序

```java
import java.util.Scanner;
import java.util.Arrays;
public class Main{
  public static void main(System[] args){
		int [][] a={
      {4,5,6,7},
      {0,1,2,3},
      {8,9,10,11}
    };
    Arrays.sort(a,(x,y) ->{
      return x[0]-y[0];
    });
      System.out.println(Arrays.deepToString(a));//二维及以上数组用这个将多维数组转化为字符串
  }
}
```



#### 3.Arrays.fill(int[] a, int val)：填充数组

```java
import java.util.Scanner;
import java.util.Arrays;
public class Main{
  public static void main(System[] args){
    int [] a=new int[10];
    Arrays.fill(a,-1);//注意只能初始化一维数组不能初始化多维数组；
    System.out.println(Arrays.toString(a));//将a数组全部初始化为-1；
  }
}
```



### 4.技巧

##### 1.再敲例如[ ] { }等时

```java
a[] or a{}
```

等是敲出[ ]后再按一次]即光标可到]的后面









