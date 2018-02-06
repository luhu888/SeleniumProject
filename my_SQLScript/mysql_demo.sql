use test_tb1;
show tables;
create table log (aid int auto_increment,site_id int,count int,date date,primary key(aid));

select * from log;

select* from websites;

select id from websites; --  从数据表中选定指定的列

select distinct country from websites; --  返回该列唯一不同的值

select * from websites where country='CN'; -- 返回country值为CN的记录

select * from websites where id>1 and id <5; -- 返回id大于1，小于5的记录

select * from websites where country like '%A'; -- 模糊查询country中以A结尾的记录,%表示多个字符,_下划线表示一个字符

select * from websites where country like '%U__'; -- 模糊查询country倒数第三位字母是U的记录

select * from websites where alexa in (1,3,5); -- 查找alexa值为1,3,5的记录,

select * from websites order by alexa desc; -- 将表的所有记录按照alexa降序排列

select * from websites order by alexa asc;   -- 将表的所有记录按照alexa升序排列,默认升序排列

select * from websites where alexa between 5 and 19; -- 返回排名在5到19之间的记录

select * from websites limit 5; -- -- 规定要返回的记录的数目

select * from websites where name regexp '^[GbF]'; -- 正则匹配

select name as n,alexa as a from websites;-- 给表的字段创建别名

select name, concat(url,'','',alexa,'','',country) as site_info from websites; -- 将多个字段放在一起创建别名

select websites.id,websites.name, log.count,log.date from websites inner join log on websites.id=log.site_id order by log.count;

-- inner join 如果表中有至少一个匹配，websites表中的id和log表中的site_id相等的话就显示websites表中的id，name，log表中的count，date

select id from websites union all select site_id from log; -- union操作符用于合并两个或多个select语句的结果集,

select avg(id) from websites; -- 返回列的平均值

select count(site_id) from log; -- 返回匹配指定条件的行数(null不计入)

select count(distinct site_id) from log; -- 返回指定列的不同值的数目alter

select count(*) from log; -- 返回表中总记录数

select name as FirstName from websites limit 1; -- 显示websites 表中name列的第一个值并命名为FirstName

select name as LastName from websites order by name desc limit 1; -- 显示websites表name列中倒数第一的记录

select max(alexa) as max_alexa from websites; -- 选取websites表alexa列的最大值显示并命名为max_alexa

select min(alexa) as min_alexa from websites; -- 选取websites表alexa列的最小值显示并命名为min_alexa

select sum(alexa) as sum_alexa from websites; -- 显示websites表alexa列的数值的总和

select site_id,sum(log.count) as numbers from log group by site_id; -- group by 语句用于结合聚合函数，根据一个或多个列对结果集进行分组

select websites.name,websites.url,sum(log.count)as nums from
  (log inner join websites on log.site_id = websites.id)
group by websites.name, websites.url having nums>0; -- having子句可以让我们筛选分组后的各组数据,

select ucase(name)as site_name,url,lcase(country) from websites; -- 将name列的值变为大写,将country列的值变为小写

select mid(name,1,4) as shortTitle from websites; -- 提取某列的前4个字符;1为起始位置(必填),4为返回的字符数(选填)

select name,length(url) as LengthOfURL from websites; -- 从websites表中选取name列，url列中值的长度

select round(alexa,5) from websites; -- 把数值字段舍入为5位小数，round返回值被变为一个一个bigint型

select name,alexa,url,now()as date from websites; -- now()返回当前的时间

select name,alexa,url,date_format(now(),'%Y-%m-%d') as date from websites; -- format()将当前时间格式化位YYYY-mm-dd

select name,url,curdate()as '当前日期' from websites; -- 返回当前日期

select name,url,curtime()as'当前时间' from websites; -- 返回当前时间

insert into websites(name,url,alexa,country) values('QQ','https://www.QQ.com',6,'CN'); -- 指定插入的列名

insert into websites values(14,'dreamgotech','http://www.dreamgotech.com',19,'CN'); -- 不指定插入的类型,但要输入全部字段的值

insert into websites values(10,'菜鸟教程','https://www.tunoob.com',4001,'CN');

insert into websites values(4,'facebook','https://www.facebook.com',3,'USA'),
(5,'WEIBO','https://weibo.com',20,'CN'); -- 向Websites中插入数据

insert into log(site_id,count,date) values(3,100,'2017-03-04'),(1,230,'2016-05-14'),(2,10,'2017-01-01'),(5,205,'2016-03-16');

update websites set name='Google_update' where name='Google'; --  更新表中已存在的记录,将记录name为Google改为Google_update，如果省略where，全部记录的那么字段都会被更新

delete from websites where alexa=6; -- 删除排名为6的记录

delete from websites; -- 不删除表结构，删除表中所有的数据

alter table websites change id id int auto_increment; -- 只有主键能被定义为自增类型

alter table websites add unique key(alexa); -- 修改alexa字段的记录为唯一值

alter table websites add constraint weiyi_id primary key (id,alexa);

alter table websites drop primary key;

CREATE TABLE copy_website like website;     # 复制表结构，不复制数据
CREATE TABLE copy_website SELECT  * FROM website;  # 完整复制表结构及数据