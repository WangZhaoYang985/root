# arduino基本架构与常用函数

### 一、Arduino基本架构

```c++
void setup() {//一些基础设定在开发板通电的那一刻运行

  // put your setup code here, to run once:

}

void loop() {//在通电时无限循环运行

  // put your main code here, to run repeatedly:

}
```

#### 二、Arduino的基本函数

**1.pinMode函数：设置数字引脚输入、输出模式；**

​    1.两个参数：引脚号即数字引脚的编号+模式

​    2.模式分为三种

     ```c++
     input//接受电信号
     output//输出电信号
     intput_pullup//接受外部信号且在没有外部输出时自动拉到5V
     ```

```c++
pinMode(pin, mode)
/* 参数 pin 为指定配置的引脚编号参数，不过要注意这里是要接在数字引脚的；mode为指定的配置模式通常可用模式
有三种:INPUT 输入模式；OUTPUT 输出模式；INPUT_PULLUP 输入上拉模式 */
```



**2.digitalWrite函数：向数字引脚写入数字值即输出数字信号**

​	1.两个参数：引脚号即数字引脚的编号+值

​        2.值分为两种

  ```c++
  High/Low
  ```

详细解释：如果已经设置为输出模式，

​		  调用digitalWrite( )会给该引脚上输出一个数字信号，

​		  如果为high则是高信号反之如果为low则为低信号；

```c++
digitalWrite(pin, value)
// 参数 pin 为指定输出的引脚编号；参数 value 为你要指定输出的电平使用 HIGH 指定输出高电平，或是使用 LOW 指定输出低电平。
```



**3.digitalRead函数：读取数字引脚上的数字值，即输入信号；**

​         一个参数引脚号即数字引脚的编号

详细解释：如果设置为输入模式，

​		   调用digitalread读取该引脚上的数字信号，

​		   如果为高电信号则为high反之如果为低信号则为low；

```c++
digitalRead(pin);
// 参数pin为指定读取状态的引脚编号。返回值为获取到的信号状态，1为高电平，0为低电平。
```



**4.analoWrite函数：模拟信号的输出函数**

​	1.两个参数：引脚号即数字引脚的编号+值

​	2.值可以为0-255之间的整数

```c++
analogWrite(pin,value)
// 参数pin是指定要输出 PWM 波的引脚，不过要注意使用可以输出 PWM 的引脚带PWM功能的引脚标有波浪线'~'；参数value指定是PWM的脉冲宽度，范围为0～255，对应占空比为 value/255。
```



**5.analogrRead函数：模拟信号的输入函数**

​	  一个值

关于值的详细解释：Arduino Uno 模拟输入功能有10位精度，

​				  即可以将0～5V的电压信号转换为0～1023的整数形式表示

​			 	 其中的0～1023即为值。

```c++
analogRead(pin)
// 参数pin是指定要读取模拟值的引脚，被指定的引脚必须是模拟输入引脚。
```

**6.delay与delayMicroseconds暂停函数**

delay  单位：ms	delayMicroseconds 单位：us

详细解释：会停止一切，

​	          若需要在暂停期间保持程序的响应性，

​		  使用非阻塞延时技术如millis( )函数；

```c++
delay(ms)
// 此函数为毫秒级延时。参数为时长，类型unsigned long

delayMicroseconds(us)
// 此函数为微秒级延时。参数为时长,类型unsigned int
```

