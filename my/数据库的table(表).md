# 数据库的table(表)

**1.创建与关联**

```sql
create table student(学号 char(10) primary key,姓名 char(10),性别 char(2),户籍 char(20),出生日期 date);//创建了一个以学号为主键的student表
```

```sql
create table cjb(学号 char(10) primary key,数学 demial(5,1),语文 demial(5,1),英语 demial(5,1),foreign key(学号) references student(学号));-- 创建了一个cjb表，并通过外键约束将这两个表连接了起来
```

**解释说明**

**外键**: 通过 FOREIGN KEY 约束，确保 学号 字段与 student 表中的 学号 字段关联。

**外键约束**: 在 cjb 表中，学号 字段作为外键，确保每个记录的 学号 都必须在 student 表中存在。这就建立了两表之间的关联。

**数据完整性**: 外键约束可以确保在 cjb 表中插入或更新数据时，只有存在于 student 表中的 学号 才能被引用。这保证了数据的一致性和完整性。

**2.修改表**

```sql
alter table student modify 出生日期 date；-- 修改出生日期为date类型；
alter table student add 出生日期 date(2024-10-10)；-- 增加2024年10月10日这个出生日期；
alter table student drop 出生日期 date(2024-10-10)；-- 删除2024年10月10日这个出生日期；
alter table cjb rename column 数学 to 数学成绩;-- 将数学列重命名为数学成绩;
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
```

