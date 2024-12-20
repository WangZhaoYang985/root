# Java的方法

1.**定义：**

指出方法所包含的程序片段，以及方法的名称和各种属性。

2.**结构：**

```java
//修饰符 返回值类型 方法名(参数列表)
{
      //方法体
}
//方法头指定方法的修饰符、返回值类型、方法名和参数。
```

方法头由<font color=red>方法的类型、名称和名称之后的一对小括号以及其中的参数列表所构成</font>；

```java
//例
int speak(){                 //无参数的方法头
  return 23;
}
int add(int x,int y,int z)   //有参数的方法头
{ return x+y+z;
}
//注意：方法返回的数据类型可以是java中的任何数据类型之一，当一个方法不需要返回数据时，返回类型必须是void；
```

3.**实例，求三个数的平均数：**

```java
public class Main{
    public static void main(String[] args){
       System.out.println(ave(1.2,2.2,3.2));
}
    public static double ave(double a,double b,double c){
        return (a+b+c)/3;
    }
}
```

4.**static**

**什么是 static？**



​	•	**属于班级**: 想象一下，你在学校里。班级里的老师是属于整个班级的，而不是只属于一个学生。static 就像这个老师，意味着这个方法或变量是属于整个类（就像班级），而不是某一个特定的对象（就像班级里的某个学生）。



**为什么要用 static？**



​	1.	**不需要创建学生**: 当你想找老师的时候，不需要每次都去创建一个新学生才能去找老师。在 Java 中，main 方法是程序的开始点，电脑（JVM）只知道如何直接找到这个方法，因此它必须是 static 的，这样它就能直接找到，不需要先创建一个类的对象。

​	2.	**共享的方法**: 如果你有一个班级里的方法（比如计算分数的办法），所有的学生都可以用这个方法，而不需要每个学生都有自己的方法。static 方法就像这样的共享方法，所有对象（学生）都可以使用，而不需要每个对象自己有一个副本。



**举个例子**



假设你有一个工具箱：



​	•	**工具箱**: 这是你的 Java 类。

​	•	**工具**: 每个工具（像是锤子、螺丝刀）就像是你类里的方法。

​	•	**工具是共享的**: 所有需要用工具的人（对象）都可以直接从工具箱里拿工具，不需要每个人都自己买一个工具箱（实例化对象）。如果工具是 static，就意味着大家可以一起使用它。



**总结**



​	•	static 意味着某个方法或变量是属于整个类的，不需要创建新的对象来使用它。

​	•	main 方法必须是 static，因为它是程序的入口，电脑需要直接找到它。

​	•	使用 static 可以让方法和变量在不同的地方被共享，大家都可以一起使用。

5.**ave方法**

**ave 方法是什么？**



​	•	**功能**: ave 方法用来计算三个数字的平均值。就像老师帮你算成绩的平均分一样。

​	•	例如，如果你有三门课的分数：80 分、90 分和100 分，ave 方法会把这三门课的分数加起来，然后除以 3，得到平均分。



**为什么要用 static？**



​	1.	**无须创建对象**: 你可以直接使用 ave 方法来计算平均值，而不需要先创建一个 Main 类的对象。这就像在学校里，大家可以直接找老师（方法），而不需要先让每个学生都注册一个新的学生身份（对象）。

​	2.	**工具方法**: ave 方法是一个“工具方法”，它只根据传入的数字来计算结果，而不依赖于任何对象的状态。它不需要记住自己的状态，所以将其定义为 static 是合适的。就像一个计算器，任何人都可以用它来计算，而不需要有自己的独特版本。



**举个例子**



假设你在学校有一个“计算分数”的工具：



​	•	**工具**: 这是 ave 方法。

​	•	**计算功能**: 这个工具可以接收三个分数（比如 80、90 和 100），然后计算它们的平均值。

​	•	**使用方式**: 任何学生（对象）都可以直接使用这个工具（ave 方法），不需要每个学生都自己买一个（创建对象）。



**总结**



​	•	ave 方法用来计算三个数字的平均值。

​	•	它被声明为 static，因为你可以直接使用它来计算，而不需要创建新的对象。

​	•	ave 方法是一个“工具方法”，它可以在不同地方被调用，帮助大家计算平均值。

6.练习

编写以下两个方法，并在main方法中测试这两个方法。
（1）方法1：在屏幕上输出：“方法练习”
（2）方法2：计算长方形的面积，长和宽为整形，面积为双精度浮点型

```java
public class Main {
    public static void method1() {
        System.out.println("方法练习");
    }
    public static double method2(int length, int width) {
        double area = (double) length * width; 
        return area;
    }
    public static void main(String[] args) {
        method1();
        int length = 5;
        int width = 10;
        double area = method2(length, width);
        System.out.println("长方形的面积为: " + area);
    }
}
```

