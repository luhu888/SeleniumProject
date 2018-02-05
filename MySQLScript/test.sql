show databases;
use test1;
show tables;
select * from website;
insert into website(name,url,alexa,country) values('火狐','https://www.firefox.com',23,'USA'),
('腾讯','https://www.QQ.com',16,'CN');
select distinct country from website;      #选取唯一不同的值
select * from website where country='CN';
select * from website where country='CN' and alexa<=50; 