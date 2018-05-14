# 一 创建表的完整语法
# create table 表名(
# 字段名1 类型[(宽度) 约束条件],
# 字段名2 类型[(宽度) 约束条件],
# 字段名3 类型[(宽度) 约束条件]
# );
#
# #解释：
# 类型：使用限制字段必须以什么样的数据类型传值
# 约束条件：约束条件是在类型之外添加一种额外的限制
#
#
# # 注意：
# 1. 在同一张表中，字段名是不能相同
# 2. 宽度和约束条件可选，字段名和类型是必须的
# 3、最后一个字段后不加逗号
# create database db37;

# 二 基本数据类型之整型：
# 1、整型：id号，各种号码，年龄，等级
# 2、分类：
# tinyint，int，bigint

# 3、测试：默认整型都是有符号的
# create table t1(x tinyint);
# insert into t1 values(128),(-129);

# create table t2(x tinyint unsigned);
# insert into t2 values(-1),(256);

# create table t3(x int unsigned);
# #4294967295
# insert into t3 values(4294967296);
#
# create table t4(x int(12) unsigned);
# insert into t4 values(4294967296123);
#
# 4、强调：对于整型来说，数据类型后的宽度并不是存储限制，而是显示限制
#     所以在创建表示，如果字段采用的是整型类型，完全无需指定显示宽度，
#     默认的显示宽度，足够显示完整当初存放的数据
#
# # 显示时，不够8位用0填充，如果超出8位则正常显示
# create table t5(x int(8) unsigned zerofill);
# insert into t5 values(4294967296123);
# insert into t5 values(1);

# 5. 浮点型
# 作用：存储身高、体重、薪资
# float (*****)
# double (**)
# decimal (**)

# 测试：
# # 相同点：
# 1. 对于三者来说，都能存放30位小数；
# # 不同点：
# 1. 精度的排序从低到高：float, double, decimal；
# 2. float与double类型能存放的整数位比decimal多；









