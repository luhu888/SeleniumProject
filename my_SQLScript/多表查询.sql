create table article(       -- 创建文章表
aid int primary key auto_increment,
title varchar(255),
content varchar(255),
uid int,
tid int
);
show databases;
# use test1;
# show tables;
-- drop table article;
# select * from article;
insert into article values(1,'文章1','文章1的正文内容fdsgfa',1,1);
# alter table article add constraint aid primary key (aid);
# alter table article change aid aid int auto_increment;
insert into article(title,content,uid,tid) values('文章2','文章2的正文内容fdsgfa',1,2);
insert into article(title,content,uid,tid) values('文章3','文章3的正文内容fdsgfa',2,1),('文章4','文章4的正文内容fdsgfa',4,1);
create table user(      -- 创建用户表
uid int primary key not null auto_increment,
username varchar(255),
email varchar(255)
);
insert into user(username,email) values('admin','admin@qq.com'),('小明','xiaoming@163.com'),('jack','jack@gmail.com');
select * from user;
create table type(       -- 创建类型表
tid int primary key auto_increment,
typename varchar(255)
);
insert into type(typename) values('普通文章'),('金华文章'),('原创文章'),('草稿');
SELECT article.aid,article.title,user.username,type.typename FROM article RIGHT
 JOIN user ON article.uid=user.uid left JOIN type ON article.tid=type.tid;  -- 对于 MySQL 多表 JOIN，还可以 INNER、LEFT 和 RIGHT 混用，其返回结果与各关键字顺序有关