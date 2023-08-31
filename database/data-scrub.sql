-- Note: Single quotes are ok, double quotes are not. Queries must be one-liners

-- Don't specify buildings
--UPDATE buildings set address='123 Main St, Berea KY', name='Campus'
--UPDATE buildings set name='Building 1' WHERE bId=2
--UPDATE buildings set name='Building 2' WHERE bId=3
--UPDATE buildings set name='Building 3' WHERE bId=4

-- randomize users except for admin
--CREATE TABLE tmp_names AS SELECT userId, first_name, last_name, row_number() over (ORDER BY RAND()) as neworder FROM users
--UPDATE users u join tmp_names tn on tn.neworder=u.userId set u.first_name=tn.first_name where u.username != 'garretta2'
--DROP TABLE tmp_names

--CREATE TABLE tmp_names AS SELECT userId, first_name, last_name, row_number() over (ORDER BY RAND()) as neworder FROM users
--UPDATE users u join tmp_names tn on tn.neworder=u.userId set u.last_name=tn.last_name where u.username != 'garretta2'
--DROP TABLE tmp_names

--UPDATE users set username=LOWER(CONCAT(REPLACE(last_name,' ',''),SUBSTR(first_name,1, 1), SUBSTR(uuid(),3,1)))  where username != 'garretta2'
