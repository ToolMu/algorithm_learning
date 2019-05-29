--
-- @lc app=leetcode.cn id=196 lang=mysql
--
-- [196] 删除重复的电子邮箱
--
# Write your MySQL query statement below

DELETE P1 
FROM Person P1, Person p2
WHERE P1.Email = P2.Email AND P1.Id > P2.Id;


