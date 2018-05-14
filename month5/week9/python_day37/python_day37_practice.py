# 1 创建购物信息表：
# 购物人 	商品名称 	数量
# A 	     甲 	     2
# B 	     乙 	     4
# C 	     丙 	     1
create table shopping_cart(
    id int primary key auto_increment,
    name char(20) not null,
    good char(20) not null,
    count int not null
    );
# 1.1：查询购买两件及以上人的姓名
select * from shopping_cart where count>2;
# 1.2：查询购买数量为2的人的商品名
select * from shopping_cart where count=2;
# 1.3：查询购买数量为4的购物人姓名
select * from shopping_cart where count=4;
# 1.4: 修改A的数量为10
update shopping_cart set count=10 where name='A';
# 1.5：删除数量等于1的这条记录
delete from shopping_cart where count=1;



# 2 创建学生表：
# 姓名 	课程 	分数
# 张三 	语文 	81
# 李四 	语文 	90
# 王五 	语文 	49

create table student(
    id int primary key auto_increment,
    name char(20) not null,
    course char(20) not null,
    score float(5,2) not null
);

insert into student(name,course,score) values
    ('张三', '语文', 81),
    ('李四', '语文', 90),
    ('王五', '语文', 49);
# 2.1：查询及格人的名字
select name from student where score>=60;
# 2.2：查询成绩在90分或以上的人名
select name from student where score>=90;
# 2.3：查询分数等于49的人名和课程名
select name,course from student where score=49;
# 2.4：修改王五的分数为60
update student set score=60 where name='王五';
# 2.5：删除名字为李四的记录
delete from student where name='李四';
# 3 创建学生表：有学生 id，姓名，密码，年龄，注册时间，体重
#   随便插入几条数据
create table student(
    id int primary key auto_increment,
    name char(20) not null,
    password char(20) not null,
    age int not null,
    weight float(5,2) not null,
    register_time datetime not null
);

