- creates database hbtn_0d_2 and user user_0d_2
-- user_0d_2 should have only SELECT privileges, password set to user_0d_2_pwd

CREATE DATABASE IF NOT EXIST hbtn_0d_2;
CREATE USER IF NOT EXIST user_0d_2;
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
