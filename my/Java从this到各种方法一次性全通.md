# Java从this到各种方法一次性全通

### 一、this

1.this最基本翻译为“本对象”或“对象本身”，指向对象自己

通俗来说是“我”；

举例：别人称呼你的时候叫“朝曦”，而“朝曦”称呼自己的时候为“我”；

2.this是一个变量本质上和引用类型变量一样

3.this 本质上就是将内存中的地址复制了一份给指向的人

```java
//例如
public User(String name){
	this.name=name;
}
//该此时this.后面的name的地址是原name的地址复制了一份给它的
```

4.为什么要有this

```java
public class User(){
 	public String name;
  public int age;
  public User(String name,int age){
    this.name=name;
    this.age=age;
  }
}
/*在默认的情况下局部变量在与对象属性同名时，局部变量优先级高于对象属性，此时优先使用局部变量
而当我们使用this指向后这个name时对象属性*/
```

5.this使用时注意事项

this的作用范围时对象内部，可以在对象方法、构造方法中使用，不能在对象外使用否则会报错

this还可以对属性进行赋值如：

```java
String name="admin";
String possword=this.name;
```

this不能用于静态方法中，因为静态方法属于类而不是某个对象

### 二、有参和无参的构造方法

在Java中，构造方法是一种特殊的方法，用于在创建对象时初始化对象。构造方法具有以下特点：

1. 构造方法的名称必须与类名完全相同。
2. 构造方法没有返回类型，连void都没有。
3. 构造方法可以被重载，即一个类可以有多个构造方法，只要它们的参数列表不同。

###### 无参构造方法（No-Argument Constructor）

无参构造方法不接受任何参数。如果一个类没有显式定义任何构造方法，Java编译器会自动提供一个无参构造方法。例如：

```java
public class MyClass {
    // 默认无参构造方法
    public MyClass() {
        System.out.println("无参构造方法被调用");
    }
}
```

如果你显式定义了任何构造方法，那么编译器将不会提供默认的无参构造方法。

###### 有参构造方法（Parameterized Constructor）

有参构造方法接受一个或多个参数，用于在创建对象时初始化对象的状态。例如：

```java
public class MyClass {
    private int number;

    // 有参构造方法
    public MyClass(int number) {
        this.number = number;
        System.out.println("有参构造方法被调用，传入的参数是：" + number);
    }
}
```

在上面的例子中，`MyClass` 类有一个有参构造方法，它接受一个整数参数，并将其赋值给类的成员变量`number`。

###### 构造方法的重载

一个类可以有多个构造方法，只要它们的参数列表不同（参数的数量或类型不同）。这称为构造方法的重载。例如：

```java
public class MyClass {
    private int number;
    private String name;

    // 无参构造方法
    public MyClass() {
        System.out.println("无参构造方法被调用");
    }

    // 有参构造方法1
    public MyClass(int number) {
        this.number = number;
        System.out.println("有参构造方法1被调用，传入的参数是：" + number);
    }

    // 有参构造方法2
    public MyClass(String name) {
        this.name = name;
        System.out.println("有参构造方法2被调用，传入的参数是：" + name);
    }

    // 有参构造方法3
    public MyClass(int number, String name) {
        this.number = number;
        this.name = name;
        System.out.println("有参构造方法3被调用，传入的参数是：" + number + ", " + name);
    }
}
```

在这个例子中，`MyClass` 类有四个构造方法，包括一个无参构造方法和三个有参构造方法，它们通过不同的参数列表实现重载。

### 三、为什么不能重载无参的构造方法

在Java中，你不能重载无参构造方法。重载（Overloading）是指在同一个类中可以定义多个同名方法，只要它们的参数列表不同（即参数的数量或类型不同）。但是，无参构造方法不接受任何参数，所以它没有参数列表。因此，你不能创建多个无参构造方法，因为它们都会被认为是具有相同名称和相同参数列表的方法。

如果你尝试在Java类中定义多个无参构造方法，编译器会报错，因为它无法区分这两个方法。

例如，下面的代码会导致编译错误：

```java
public class MyClass {
    // 尝试重载无参构造方法，这会导致编译错误
    public MyClass() {
        System.out.println("第一个无参构造方法");
    }

    public MyClass() {
        System.out.println("第二个无参构造方法");
    }
}
```

编译器会抛出错误，因为两个构造方法的签名相同。

如果你需要根据不同的条件初始化对象，你可以使用有参构造方法，并在构造方法内部通过逻辑判断来区分不同的初始化情况。例如：

```java
public class MyClass {
    private int value;

    public MyClass() {
        this(0); // 调用有参构造方法，传入默认值
    }

    public MyClass(int value) {
        this.value = value;
    }
}
```

在这个例子中，我们定义了一个有参构造方法`MyClass(int value)`，并在无参构造方法`MyClass()`中调用了有参构造方法，传入了一个默认值。这样，我们就可以根据不同的参数来初始化对象，同时避免了重载无参构造方法的问题。

### 四、在调用构造方法时和其他方法的区别

在Java中，构造方法与其他普通方法在调用时有一些关键的区别：

1. **调用时机**：
   - **构造方法**：构造方法在创建对象时被调用，即在`new`关键字后面紧跟类名时调用。构造方法只能被用来初始化新创建的对象。
   - **普通方法**：普通方法可以在对象创建后，通过对象的引用来调用。它们用于执行对象的行为，可以多次调用。
2. **调用方式**：
   - **构造方法**：构造方法的调用不需要使用任何方法名，只需要使用`new`关键字和类名即可。例如：`new MyClass()`。
   - **普通方法**：普通方法的调用需要通过对象的引用，并使用点号（`.`）后跟方法名和参数。例如：`myObject.someMethod()`。
3. **返回类型**：
   - **构造方法**：构造方法没有返回值，因此没有返回类型，甚至连`void`也没有。
   - **普通方法**：普通方法可以有返回值，因此必须声明返回类型，或者返回`void`表示没有返回值。
4. **构造方法重载**：
   - **构造方法**：一个类可以有多个构造方法，只要它们的参数列表不同（参数的数量或类型不同），这称为构造方法的重载。
   - **普通方法**：一个类也可以有多个同名的普通方法，只要它们的参数列表不同，这也称为方法的重载。
5. **自动调用**：
   - **构造方法**：在构造方法内部，`this()`可以被用来调用同一个类中的另一个构造方法，而`super()`可以被用来调用父类的构造方法。
   - **普通方法**：普通方法之间可以使用`this.methodName`来相互调用。
6. **对象创建**：
   - **构造方法**：构造方法的主要目的是在对象创建时进行初始化。
   - **普通方法**：普通方法用于执行对象的行为，不涉及对象的创建。
7. **构造方法的隐式调用**：
   - 如果子类的构造方法中没有显式地通过`super()`调用父类的构造方法，Java编译器会自动插入`super()`调用父类的无参构造方法。如果没有无参构造方法，编译器会报错。
8. **构造方法不能被继承**：
   - 构造方法不会被继承，每个类都有自己的构造方法。子类的构造方法需要显式地调用父类的构造方法。

#### 例子

###### 1. 调用时机和方式

**构造方法：**

```java
public class Person {
    String name;
    int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
}

public class Main {
    public static void main(String[] args) {
        Person person = new Person("John", 30); // 调用构造方法
    }
}
```
在这个例子中，`Person` 类有一个构造方法，它接受姓名和年龄作为参数。在`main`方法中，我们使用`new`关键字和类名`Person`来创建`Person`对象，并调用构造方法。

**普通方法：**
```java
public class Person {
    String name;

    public Person(String name) {
        this.name = name;
    }

    public void setAge(int age) {
        this.age = age; // 假设有一个名为age的成员变量
    }
}

public class Main {
    public static void main(String[] args) {
        Person person = new Person("John");
        person.setAge(30); // 调用普通方法
    }
}
```
在这个例子中，`Person` 类有一个普通方法`setAge`，它用于设置年龄。在`main`方法中，我们首先创建`Person`对象，然后通过对象引用`person`调用`setAge`方法。

###### 2. 返回类型

**构造方法：**
构造方法没有返回类型，甚至连`void`也没有。

**普通方法：**
```java
public class Calculator {
    public int add(int a, int b) {
        return a + b;
    }
}

public class Main {
    public static void main(String[] args) {
        Calculator calculator = new Calculator();
        int sum = calculator.add(5, 3); // 调用普通方法并接收返回值
    }
}
```
在这个例子中，`Calculator` 类有一个普通方法`add`，它接受两个整数参数并返回它们的和。

###### 3. 构造方法重载

**构造方法重载：**

```java
public class Book {
    String title;

    // 无参构造方法
    public Book() {
        this.title = "Unknown";
    }

    // 有参构造方法
    public Book(String title) {
        this.title = title;
    }
}

public class Main {
    public static void main(String[] args) {
        Book book1 = new Book(); // 调用无参构造方法
        Book book2 = new Book("Java Programming"); // 调用有参构造方法
    }
}
```
在这个例子中，`Book` 类有两个构造方法，一个无参，一个有参，展示了构造方法的重载。

###### 4. 自动调用

**构造方法的隐式调用：**

```java
public class Animal {
    public Animal() {
        System.out.println("Animal created");
    }
}

public class Dog extends Animal {
    public Dog() {
        super(); // 显式调用父类构造方法
        System.out.println("Dog created");
    }
}

public class Main {
    public static void main(String[] args) {
        Dog dog = new Dog(); // 输出: Animal created, Dog created
    }
}
```
在这个例子中，`Dog` 类的构造方法显式调用了父类`Animal`的构造方法。如果没有显式调用，Java编译器会自动插入`super()`调用父类的无参构造方法。

### 五、子类重写父类的方法

在Java中，子类可以重写（Override）父类的方法，这是多态性的一个重要体现。当子类重写父类的方法时，子类的方法会覆盖父类中具有相同名称、参数列表和返回类型的方法。以下是子类重写父类方法的一些规则和示例：

###### 重写规则

1. 方法名、参数列表和返回类型必须完全相同。
2. 访问权限不能比父类中被重写的方法的访问权限更严格。
3. 重写的方法不能抛出新的检查异常或比被重写的方法声明的检查异常更广泛的异常。
4. 构造方法不能被重写。
5. 如果父类方法被声明为`final`，则不能被重写。
6. 如果父类方法不是`public`，则子类中重写的方法只能被子类内部访问。

###### 示例

假设有一个父类`Animal`和一个子类`Dog`，我们可以这样重写父类的方法：

```java
class Animal {
    public void makeSound() {
        System.out.println("Some generic animal sound");
    }
}

class Dog extends Animal {
    @Override
    public void makeSound() {
        System.out.println("Woof woof");
    }
}

public class TestOverride {
    public static void main(String[] args) {
        Animal myDog = new Dog();
        myDog.makeSound(); // 输出 "Woof woof"
    }
}
```

在这个例子中，`Dog`类重写了`Animal`类的`makeSound`方法。当我们创建`Dog`类的实例并调用`makeSound`方法时，会输出`Dog`类中定义的方法体。

###### 使用`@Override`注解

在子类的方法声明前加上`@Override`注解可以明确表示该方法是重写父类的方法。这不仅是一个好习惯，还可以帮助编译器检查是否正确重写了父类的方法。如果父类中没有对应的方法，编译器会报错。

```java
@Override
public void makeSound() {
    System.out.println("Woof woof");
}
```

如果忘记添加`@Override`注解，并且父类中没有对应的方法，编译器不会报错，但运行时会调用父类的方法，这可能会导致逻辑错误。

通过重写方法，子类可以改变父类行为，实现多态性，使得同一个方法调用可以根据对象的实际类型产生不同的行为。

### 六、super

在Java中，`super()` 是用来调用父类的构造方法的。是否在 `super()` 中加入参数取决于父类构造方法的定义。

###### 不加括号（无参数）

当你使用无参数的 `super()` 时，你正在调用父类中定义的无参构造方法。这通常在你想要使用父类构造方法的默认行为时使用。例如：

```java
class Parent {
    public Parent() {
        System.out.println("Parent's no-arg constructor");
    }
}

class Child extends Parent {
    public Child() {
        super(); // 调用父类的无参构造方法
        System.out.println("Child's constructor");
    }
}
```

在这个例子中，`Child` 类的构造方法通过 `super()` 调用了 `Parent` 类的无参构造方法。

###### 加入参数（有参数）

当你使用有参数的 `super(x, y, ...)` 时，你正在调用父类中定义的有参构造方法。这在你想要在子类的构造过程中，使用父类构造方法来初始化父类部分的状态时使用。例如：

```java
class Parent {
    public Parent(int x) {
        System.out.println("Parent's constructor with argument: " + x);
    }
}

class Child extends Parent {
    public Child(int x, int y) {
        super(x); // 调用父类的有参构造方法，并传递参数x
        System.out.println("Child's constructor with argument: " + y);
    }
}
```

在这个例子中，`Child` 类的构造方法通过 `super(x)` 调用了 `Parent` 类的有参构造方法，并传递了参数 `x`。

##### 注意事项

1. **必须在子类构造方法的第一行**：`super()` 必须放在子类构造方法的第一行，因为构造方法的第一条语句是隐式或显式地调用父类的构造方法。

2. **匹配父类构造方法的签名**：`super()` 中的参数必须与父类中定义的某个构造方法的参数列表完全匹配。

3. **不能同时使用无参和有参的 `super()`**：一个子类的构造方法中不能同时调用无参和有参的 `super()`。

4. **如果没有显式的 `super()`**：如果子类的构造方法中没有显式地调用 `super()`，并且父类没有无参构造方法，那么编译器会报错。

5. **`super()` 不能被继承**：`super()` 调用的行为不会被继承，每个子类必须显式地调用 `super()`。

通过这种方式，Java确保了父类部分的状态在创建子类对象时被正确地初始化。

### 七、静态方法

在Java中，静态方法是属于类的，而不是属于某个对象的。这意味着你可以在不创建类的实例的情况下调用静态方法。静态方法通常用于实现不依赖于类实例状态的功能。以下是静态方法的一些关键特性和使用场景：

###### 静态方法的特性

1. **类级别访问**：静态方法可以通过类名直接访问，不需要创建类的实例。
2. **不能访问实例变量和实例方法**：静态方法只能直接访问类的静态成员（包括静态变量和静态方法）。
3. **使用`static`关键字声明**：在方法声明前加上`static`关键字。
4. **静态方法的重载**：静态方法可以被重载，即同一个类中可以有多个同名的静态方法，只要它们的参数列表不同。
5. **静态方法的继承**：静态方法不是由对象继承的，而是被类继承。子类可以访问父类的静态方法，但不会覆盖它们。
6. **不能被声明为`abstract`**：静态方法不能被声明为抽象的。
7. **常用于工具类**：静态方法经常用于工具类，如`java.lang.Math`和`java.util.Collections`。

###### 静态方法的示例

```java
public class Utility {
    public static void printMessage(String message) {
        System.out.println(message);
    }
    
    public static int add(int a, int b) {
        return a + b;
    }
}

public class Main {
    public static void main(String[] args) {
        // 直接通过类名调用静态方法
        Utility.printMessage("Hello, World!");
        int sum = Utility.add(5, 3);
        System.out.println("Sum: " + sum);
    }
}
```

在这个例子中，`Utility`类有两个静态方法：`printMessage`和`add`。它们可以通过类名直接调用，而不需要创建`Utility`类的实例。

###### 静态方法的使用场景

1. **工具方法**：如计算、格式化、比较等不需要访问对象状态的方法。
2. **常量访问**：通过静态方法访问常量，虽然在Java中更常见的是通过静态变量直接访问。
3. **工厂方法**：创建类实例的方法，尤其是在单例模式中。
4. **主方法**：`main`方法就是一个静态方法，它是程序的入口点。

###### 注意事项

- 静态方法不能访问类的实例变量和实例方法，因为它们不依赖于类的任何对象。
- 静态方法在多线程环境中可能需要考虑线程安全问题。
- 过度使用静态方法可能导致代码难以测试和维护，因为静态方法不属于任何对象，这使得模拟（mocking）和依赖注入变得困难。

静态方法是Java语言的一个重要特性，它们提供了一种方便的方式来实现和访问与特定对象状态无关的功能。

