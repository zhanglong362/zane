# 1 创建学生表：有学生 id，姓名，密码，年龄
create table student(
    id int primary key auto_increment,
    name varchar(50) not null,
    password varchar(25) default '123',
    age varchar(10)
    );
# 2 创建学校表：有学校id，学校名称，地址
create table school(
    id int primary key auto_increment,
    name varchar(50) not null,
    address varchar(100) not null
    );
# 3 创建课程表：有课程id，课程名称，课程价格，课程周期，所属校区（其实就是学校id）
create table course(
    id int primary key auto_increment,
    name varchar(50) not null,
    price int not null,
    cycle varchar(50) not null,
    school_id varchar(50) not null
    );
# 4 创建选课表：有id，学生id，课程id
create table curricula_variable(
    id int primary key auto_increment,
    student_id int not null,
    course_id int not null
    );

# 添加学生：张三，20岁，密码123
#           李四，18岁，密码111
insert into student(name, password, age) values('张三', '123', '20'), ('李四', '111','18');

# 创建学校：oldboyBeijing 地址：北京昌平
#           oldboyShanghai 地址：上海浦东
insert into school(name, address) values('oldboyBeijing', '北京昌平'), ('oldboyShanghai', '上海浦东');

# 创建课程：Python全栈开发一期，价格2w，  周期5个月，属于上海校区
#           Linux运维一期       价格200，周期2个月，属于上海校区
#           Python全栈开发20期 ，价格2w，周期5个月，属于北京校区
insert into course(name, price, cycle, school_id) values('Python全栈开发一期', 20000, 5, 2), ('Linux运维一期', 200, 2, 2), ('Python全栈开发20期', 20000, 5, 1);

# 张三同学选了Python全栈开发一期的课程
# 李四同学选了Linux运维一期的课程
# （其实就是在选课表里添加数据）
insert into curricula_variable(student_id, course_id) values(1, 1), (2, 2);
# 查询：查询北京校区开了什么课程
select * from course where school_id=1;
#       查询上海校区开了什么课程
select * from course where school_id=2;
#       查询年龄大于19岁的人
select * from student where age>19;
#       查询课程周期大于4个月的课程
select * from course where cycle>4;

