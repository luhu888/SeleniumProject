show databases;
use test1;
show tables;
select * from website;
insert into website(name,url,alexa,country) values('火狐','https://www.firefox.com',23,'USA'),
('腾讯','https://www.QQ.com',16,'CN');
select distinct country from website;      #选取唯一不同的值
select * from website where country='CN';
select * from website where country='CN' and alexa<=50;
show columns from website;   # SHOW COLUMNS 要求给出一个表名（ 这个例子中的FROMcustomers），它对每个字段返回一行，行中
# 包含字段名、数据类型、是否允许NULL、键信息、默认值以及其他信息（如字段cust_id的auto_increment）
describe website;      # 与上句功能相同，快捷方式
show STATUS;      # 用于显示广泛的服务器状态信息
SHOW CREATE DATABASE test1;
show create TABLE website;
HELP SHOW;    # 显示允许的show语句,在命令行中可以使用，内置命令在编辑器中无法使用
show errors;   # 用来显示服务器的错误
show WARNINGS;  # 用来显示服务器的警告
show GRANTS;     # 用来显示授予用户（所有用户或特定用户）的安全权限


















