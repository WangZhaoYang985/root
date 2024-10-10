# Find girlfriend之类与接口

### 1.findgirfriend接口

```java
package org.wzy;

public interface Findgirlfriend {
    public void figure();
    public void Fivesenses();

}

```

### 2.add接口之接口的继承

```java
package org.wzy;

public interface Add extends Findgirlfriend {
    public void appearance();
}

```

### 3.接口的实现

```java
package org.wzy;

public class yujie implements Add {
    private final String name="yujie";

    @Override
    public void appearance() {
        System.out.println(name+": 成熟");
    }
    public void figure(){
        System.out.println(name+": 高挑");
    }
    public void Fivesenses(){
        System.out.println(name+"立体");
    }

}
```

```java
package org.wzy;

public class luoli implements Add {
    private final String name="luoli";
    @Override
    public void appearance() {
        System.out.println(name+"年轻");
    }

    @Override
    public void figure() {
        System.out.println(name+"娇小");
    }

    @Override
    public void Fivesenses() {
        System.out.println(name+"柔和、稚嫩");
    }
}
```

```java
package org.wzy;

public class contrastyujie implements Add {
    private final String name="contrastyujie";

    @Override
    public void appearance() {
        System.out.println(name+": 成熟");
    }

    @Override
    public void figure() {
        System.out.println(name+"娇小");
    }

    @Override
    public void Fivesenses() {
        System.out.println(name+"立体");
    }
}
```

```java
package org.wzy;

public class contrastluoli implements Add {
    private final String name="contrastluoli";

    @Override
    public void appearance() {
        System.out.println(name+"年轻");
    }

    @Override
    public void figure() {
        System.out.println(name+": 高挑");
    }

    @Override
    public void Fivesenses() {
        System.out.println(name+"柔和、稚嫩");
    }
}
```

**每个类可以实现多个接口**

### 4.接口的多态

```java
package org.wzy;
import  org.wzy.Add;
import  org.wzy.contrastluoli;
import  org.wzy.contrastyujie;
import  org.wzy.yujie;
import  org.wzy.luoli;
public class Main {
    public static void main(String[] args) {
        Add[] adds = {
                new contrastluoli(),
                new contrastyujie(),
                new yujie(),
                new luoli()
        };
        for (Add add : adds) {
            add.appearance();
            add.figure();
            add.Fivesenses();
        }
    }
}
```

