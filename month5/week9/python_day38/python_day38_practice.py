# 1 创建用户表 id，username,password
#     id为自增且唯一约束
#     username和password为主键
create table user(
    id int unique not null auto_increment,
    username char(20) not null,
    password char(20) not null,
    group_id int,
    constraint pk_user primary key(username, password)
);

create table user(
    id int unique not null auto_increment,
    username char(20) not null,
    password char(20) not null,
    primary key(username, password)
);

# 2 插入三条数据，root ，123
#                 egon，456
#                 lqz，678

insert into user(username, password)
values
    ('root', '123'),
    ('egon', '456'),
    ('lqz', '678');

# 3 创建用户组表： id，groupname
#     id为主键自增
#     groupname为唯一约束不为空
create table group(
    id int primary key auto_increment,
    group_name char(20) unique not null
);

# 4 插入数据：IT部门
#             销售部门
#             财务部门
#             总经理
insert into groups(group_name) values
    ('IT部门'),
    ('销售部门'),
    ('财务部门'),
    ('总经理');

# 5 创建主机表：id，ip
#             id自增，主键
#             ip唯一约束不为空，默认为127.0.0.1
create table host(
    id int primary key auto_increment,
    ip char(20) unique not null default '127.0.0.1'
);

# 6 插入数据：('172.16.45.2'),
#             ('172.16.31.10'),
#             ('172.16.45.3'),
#             ('172.16.31.11'),
#             ('172.10.45.3'),
#             ('172.10.45.4'),
#             ('172.10.45.5'),
#             ('192.168.1.20'),
#             ('192.168.1.21'),
#             ('192.168.1.22'),
#             ('192.168.2.23'),
#             ('192.168.2.223'),
#             ('192.168.2.24'),
#             ('192.168.3.22'),
#             ('192.168.3.23'),
#             ('192.168.3.24')
insert into host(ip)
values
    ('172.16.45.2'),
    ('172.16.31.10'),
    ('172.16.45.3'),
    ('172.16.31.11'),
    ('172.10.45.3'),
    ('172.10.45.4'),
    ('172.10.45.5'),
    ('192.168.1.20'),
    ('192.168.1.21'),
    ('192.168.1.22'),
    ('192.168.2.23'),
    ('192.168.2.223'),
    ('192.168.2.24'),
    ('192.168.3.22'),
    ('192.168.3.23'),
    ('192.168.3.24');

# 7 创建业务线表： id，businesss
#                 id主键自增
#                 business不为空，唯一约束
create table business(
    id int primary key auto_increment,
    business char(120) unique not null
);

# 8 插入数据：('轻松贷'),
#             ('随便花'),
#             ('大富翁'),
#             ('穷一生')
insert into business(business)
values
    ('轻松贷'),
    ('随便花'),
    ('大富翁'),
    ('穷一生');

# 9 建关系：user与usergroup
# （自行关联，外键约束）
create table user_groups(
    id int not null unique  auto_increment,
    user_id int not null,
    group_id int not null,
    constraint pk_user primary key(user_id, group_id),
    constraint fk_user_id foreign key(user_id) references user(id),
    constraint fk_group_id foreign key(group_id) references groups(id)
);

# 10 插入数据：   (1,1),
#                 (1,2),
#                 (1,3),
#                 (1,4),
#                 (2,3),
#                 (2,4),
#                 (3,4)
insert into user_groups(user_id, group_id)
values
    (1,1),
    (1,2),
    (1,3),
    (1,4),
    (2,3),
    (2,4),
    (3,4);

# 11 建关系：host与business
# （自行关联，外键约束）
create table host_business(
    id int unique not null auto_increment,
    host_id int,
    business_id int,
    constraint pk_host primary key(host_id, business_id),
    constraint fk_host_id foreign key(host_id) references host(id),
    constraint fk_business_id foreign key(business_id) references business(id)
);

# 12 插入数据：   (1,1),
#                 (1,2),
#                 (1,3),
#                 (2,2),
#                 (2,3),
#                 (3,4)
insert into host_business(host_id, business_id)
values
    (1,1),
    (1,2),
    (1,3),
    (2,2),
    (2,3),
    (3,4);

# 13 建关系：user与host
# （自行关联，外键约束）
create table user_host(
    id int primary key auto_increment,
    user_id int,
    host_id int,
    foreign key(user_id) references user(id) on delete cascade on update cascade,
    foreign key(host_id) references host(id) on delete cascade on update cascade
);

# 14 插入数据：   (1,1),
#                 (1,4),
#                 (1,15),
#                 (1,16),
#                 (2,2),
#                 (2,3),
#                 (2,4),
#                 (2,5),
#                 (3,10),
#                 (3,11),
#                 (3,12)
insert into user_host(user_id, host_id)
values
    (1,1),
    (1,4),
    (1,15),
    (1,16),
    (2,2),
    (2,3),
    (2,4),
    (2,5),
    (3,10),
    (3,11),
    (3,12);

# 15 创建班级表：cid,caption
#     学生表：sid，sname，gender，class_id
#     老师表：tid,tname
#     课程表：cid，cname，teacher_id
#     成绩表：sid，student_id，course_id，number
#     (相关关联关系要创建好，插入几条测试数据)
create table class(
    cid int primary key auto_increment,
    caption char(20) not null
);

create table student(
    sid int primary key auto_increment,
    sname char(20) not null,
	gender char(10) not null,
	class_id int,
	foreign key(class_id) references class(cid) on delete cascade on update cascade
);

create table teacher(
    tid int primary key auto_increment,
    tname char(20) not null
);

create table course(
    cid int primary key auto_increment,
    cname char(20) not null,
	teacher_id int,
	foreign key(teacher_id) references teacher(tid) on delete cascade on update cascade
);

create table score(
    sid int primary key auto_increment,
    student_id int,
	course_id int,
	number float(5,2),
	foreign key(student_id) references student(sid) on delete cascade on update cascade,
	foreign key(course_id) references course(cid) on delete cascade on update cascade
);
