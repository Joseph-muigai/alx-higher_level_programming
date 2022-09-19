-- a script that creates the database hbtn_0d_2 and the user user_0d_2.
-- user_0d_2 should have only SELECT privilege in the database hbtn_0d_2
-- The user_0d_2 password should be set to user_0d_2_pwd

CREATE IF NOT EXISTS DATABASE hbtn_0d_2;
CREATE IF NOT EXISTS USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd'
GRANT SELECT ON 'hbtn_0d_2'.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;