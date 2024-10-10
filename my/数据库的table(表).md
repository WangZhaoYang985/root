# 数据库的table(表)

**1.创建与关联**

```sql
create table student(学号 char(10) primary key,姓名 char(10),性别 char(2),户籍 char(20),出生日期 date);//创建了一个以学号为主键的student表
```

```sql
create table cjb(学号 char(10) primary key,数学 decimal(5,1)asse foreign key(学号) references student(学号));-- 创建了一个cjb表，并通过外键约束将这两个表连接了起
```

```sql
create view 计科201 as select * from student where 班级='计科20-1';-- 创建一个视图，名为计科201，这个视图包含了student表中所有班级为计科20-1的学生记录
```

**解释说明**

**外键**: 通过 FOREIGN KEY 约束，确保 学号 字段与 student 表中的 学号 字段关联。

**外键约束**: 在 cjb 表中，学号 字段作为外键，确保每个记录的 学号 都必须在 student 表中存在。这就建立了两表之间的关联。

**数据完整性**: 外键约束可以确保在 cjb 表中插入或更新数据时，只有存在于 student 表中的 学号 才能被引用。这保证了数据的一致性和完整性。

**2.修改表**

```sql
alter table student modify 出生日期 date-- 修改出生日期为date类型；
alter table student add 出生日期 date(2024-10-10)；-- 增加2024年10月10日这个出生日期；
alter table student drop 出生日期 date(2024-10-10)；-- 删除2024年10月10日这个出生日期；
alter table cjb rename column 数学 to 数学成绩;-- 将数学列重命名为数学成绩;
alter table student add 学号 char(20);-- 增加一个名为学号的列
alter table student drop column 学号;-- 删除学号列
```

**3.表的查找**

```sql
select * from student where 性别='男'；-- 从表的所有列(*代表选择表中所有列)中选择性别为男的所有记录；
select * from student where month(出生日期)>=3 and month(出生日期)<=5；-- 筛选 出生日期 的月份在 3 月（包括 3 月）到 5 月（包括 5 月）之间的记录。
select * from student where month(出生日期)= between 3 and 5；-- 筛选 出生日期 的月份在 3 月（包括 3 月）到 5 月（包括 5 月）之间的记录。
select 姓名,籍贯,班级,2024-year(出生日期) 年龄 from student;-- 从student表中找到年龄为2024年的人的姓名,籍贯,班级,出生日期;(后面的"年龄"为修改那列的名称为年龄否则结果给的不符合数据客观事实)
select 姓名,籍贯,班级,(today()-出生日期)/365 年龄 from student;-- 算出到今天为止这个人多少岁；
select * from student where 籍贯 in('北京','上海')；-- 找到籍贯为北京和上海的所有人；
select * from student where 籍贯 not in('北京','上海');-- 找到籍贯除了北京和上海的所有人；
select * from student where 籍贯='北京' union select * from student where 籍贯='上海';-- 将上海和北京的人都查询出来并去掉重复的人
select * from student where 籍贯 is null;-- 查找没有籍贯信息的人
select * from student where 籍贯 =(selcet 籍贯 from student where 姓名 = '莉莉');-- 查找跟莉莉同一个老家的人的所有信息(嵌套查找)
select cout(学号) from student where 籍贯='天津';-- 计算天津人的数量总和
select sum(数学) , avg(数学) , sum(语文) , avg(语文) , sum(数据库) from cjb;-- 计算数学语文成绩的求和和平均数还有数据库的和
select * from cjb where 数学>=(select avg(数学) from cjb);-- 查找超过数学平均值的同学
select * from cjb where 数学>=60 order by 数学;-- 查找到数学大于60分的同学并按照升序排列
select * from cjb where 数学>=60 order by 数学 desc;-- 查找到数学大于60分的同学并按照降序排列从高到低
select * from student where 学号 like '20_0%';-- like的模糊查找%(百分号)代表任意数量的字符_(下划线)代表任意单个字符
```

**4.表的插入**

```sql
insert into student(学号,姓名,性别,籍贯,班级) values('2022100220','张国荣','男','上海','计科20-2');-- 插入叫张国荣的全部信息到这个表中(前面填了什么信息插入什么)
insert into student values('2022100220','张国荣','男','上海','计科20-2');-- 插入叫张国荣的全部信息到这个表中(表中有的信息都要插入)
insert into 计科201 (select 学号,姓名,性别,籍贯 from student where 姓名='王珊');-- 将student表中王珊的学号,姓名,性别,籍贯信息插入计科201中
```

**5.表的更新**

```sql
update student set 籍贯='阿勒泰' where 姓名 ='郭丽娟';-- 将郭丽娟的籍贯更新为阿勒泰
update cjb set 数学=数学+10 where 学号='2022100112';-- 学号为2022100112的学生的数学成绩增加10分
update student set 籍贯='阿勒泰',班级='计科'where 学号='2022100114';-- 将学号为2022100114的学生的籍贯更新为“阿勒泰”，班级更新为“计科”
```

**6.表的删除**

```sql
delete from student where 学号 =(select student.学号 from student,cjb where 数学<60 and student.学号=cjb.学号);-- 从student表中删除数学成绩低于60分的学生记录
delete from 计科201 where 学号='9999';-- 删除学号为9999的学生记录
drop table student;-- 删除student这个表
drop view student;-- 删除student这个视图
```

**7.用户与权限设置**

**管理员账号：dba**

​	    **密码：sql**

```sql
grant select,insert,delete,update on student to 李四;-- 赋予给李四这个用户给student表的查找插入删除更改权限
grant select on student to aaa,bbb,ccc;-- 赋予用户aaa,bbb,ccc以查找的权限
grant all privileges on student to 李四;-- 给予李四student表的全部权限
grant insert on student to aaa with grant option;-- 再赋予aaa权限的基础上,他可以给其他用户赋给他拥有的插入这个权限
remove select on student from 李四;-- 从李四手上收回查找的权限
```

**不出意外的话sql代码到此应该完结了**
