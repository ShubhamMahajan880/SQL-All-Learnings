                                            My SQL

What is MySQL?

  - Most popular RDBMS - Based on SQL
  - Swedish Company MySQL AB --> Sun Microsystem -->  Oracle Now, supported and managed by Oracle Corporation.

  - Used by: Facebook,Youtube, Flickr, etc.
  - Written in C and C++
  - Initial Release : 23 May 1995
  - Current Version : MYSQL 8.0.22


MYSQL Workbench 
  - User Interface for MySQL i.e. a graphical tool for working with MYSQL servers and databases.
  - Supports MYSQL server versions 5.6 and higher

MYSQL Features
  - Based on SQL
  - Open Source
  - Friendly & compatible with PHP. Connect easily & manipulate databases.
  - Based on client-server architecture 
  - Scalable : Support large databases.
  * 50 million rows or more in a table.
  * Default file size limit for a table is 4GB.(can be increased)
  - Compatible with major operating systems and languages.
---------------------------------------------------------------------------------------------------------------------------------------------------------



- Setup of MySQL
- creating Database in MySQL
- Creating table in MySQL

---------------------------------------------------------------------------------------------------------------------------------------------------------



In cmd : -
1 - MySQL --version : - For check the version of MySQL database
2 - MySQL -u root -p : - ask for password 
3 - show databases - for showing the database created 

---------------------------------------------------------------------------------------------------------------------------------------------------------


4.1 - # Creating a Database & Deleting a Database -  
	CREATE DATABASE db_name;

4.2 - use db_name - Specifically use this databse
       use shubhdb1;

       DROP DATABASE db_name;
       For delete a created databse
---------------------------------------------------------------------------------------------------------------------------------------------------------


5 - # Creating table & Deleting a Table - 	
    CREATE TABLE table_name(
    Column 1 Datatypeofcolmn,
    Column 2 Datatypeofcolmn,
    Column 3 Datatypeofcolmn,
    Column 4 Datatypeofcolmn,
	 
);
Ex : -
     CREATE TABLE JARVIS(
    -> roboID int,
    -> Nameofrobo varchar(500),
    -> Workofrobo varchar(255),
    -> roboDEPTNO int,
    -> roboProficiency int
    -> );

    DROP TABLE tb_name;
    For delete a Table
---------------------------------------------------------------------------------------------------------------------------------------------------------


6 - # Describing a table -
    It proivdes structure of a table
    DESC table_name;
+-----------------+--------------+------+-----+---------+-------+
| Field           | Type         | Null | Key | Default | Extra |
+-----------------+--------------+------+-----+---------+-------+
| roboID          | int          | YES  |     | NULL    |       |
| Nameofrobo      | varchar(500) | YES  |     | NULL    |       |
| Workofrobo      | varchar(255) | YES  |     | NULL    |       |
| roboDEPTNO      | int          | YES  |     | NULL    |       |
| roboProficiency | int          | YES  |     | NULL    |       |
+-----------------+--------------+------+-----+---------+-------+
---------------------------------------------------------------------------------------------------------------------------------------------------------


7 - # Inserting Records in a Table - 

mysql>  INSERT INTO table_name (nameofcol1,nameofcol2,nameofcol3,nameofcol4,nameofcol5) VALUES (valofcol1,'valofcol2',valofcol3,valofcol4,valofcol5);# in case when value of the column is in varchar then it will be in 'string'

Ex:- 
mysql> INSERT INTO JARVIS (roboID,Nameofrobo,Workofrobo,roboDEPTNO,roboProficiency) VALUES (12,'markone','computeragent',01,466);
mysql> INSERT INTO JARVIS (roboID,Nameofrobo,Workofrobo,roboDEPTNO, roboProficiency) VALUES (22,'mark2','personalagent',02,500)
mysql> INSERT INTO JARVIS (roboID,Nameofrobo,Workofrobo,roboDEPTNO,roboProficiency) VALUES (32,'mark3','Homeagent',03,60
0);


8 - # Selecting from Table -
    SELECT * FROM table_name

 Ex-   
    mysql>  SELECT * FROM JARVIS; : - for selecting full table at a time for display

 +--------+------------+---------------+------------+-----------------+
| roboID | Nameofrobo | Workofrobo    | roboDEPTNO | roboProficiency |
+--------+------------+---------------+------------+-----------------+
|     12 | markone    | computeragent |          1 |             466 |
|     22 | mark2      | personalagent |          2 |             500 |
|     22 | mark2      | personalagent |          2 |             500 |
|     32 | mark3      | Homeagent     |          3 |             600 |
+--------+------------+---------------+------------+-----------------+

    mysql> SELECT col_name FROM table_name;
    mysql> SELECT roboID FROM JARVIS; : - for select a particulr column from the table.

+--------+
| roboID |
+--------+
|     12 |
|     22 |
|     22 |
|     32 |
+--------+

    mysql> SELECT Workofrobo FROM JARVIS;
+---------------+
| Workofrobo    |
+---------------+
| computeragent |
| personalagent |
| personalagent |
| Homeagent     |
+---------------+
---------------------------------------------------------------------------------------------------------------------------------------------------------

9 - # Notnull Constraints in MYSQL
    use NOT NULL constraint for not having null quantity
    mysql> CREATE TABLE Marvel(
    -> Phase int NOT NULL,
    -> MovieName varchar(200),
    -> Collection int not null,
    -> Year int
    -> );

    mysql> desc Marvel;
    +------------+--------------+------+-----+---------+-------+
| Field      | Type         | Null | Key | Default | Extra |
+------------+--------------+------+-----+---------+-------+
| Phase      | int          | NO   |     | NULL    |       |
| MovieName  | varchar(200) | YES  |     | NULL    |       |
| Collection | int          | NO   |     | NULL    |       |
| Year       | int          | YES  |     | NULL    |       |
+------------+--------------+------+-----+---------+-------+

    mysql> INSERT INTO Marvel(Phase,MovieName,Collection,Year) VALUES (1,'Ironman',1500000,2007);
    mysql> INSERT INTO Marvel (Phase,MovieName,Collection,Year)
    -> VALUES (2,'Thor:OdinKabeta',1560000,2012);
    mysql> INSERT INTO Marvel(Phase,MovieName,Collection,Year)
    -> VALUE(3,'TheincredibleHulk',198000,2015);    
    mysql> INSERT INTO Marvel(Phase,MovieName,Collection,Year)
    -> VALUE(4,'WonderWoman',8996000,2017);
    mysql> INSERT INTO Marvel(Phase,MovieName,Collection,Year)
    -> VALUES(5,'BlackWidow',563200,2019);

    mysql> SELECT * FROM Marvel;
+-------+-------------------+------------+------+
| Phase | MovieName         | Collection | Year |
+-------+-------------------+------------+------+
|     1 | Ironman           |    1500000 | 2007 |
|     2 | Thor:OdinKabeta   |    1560000 | 2012 |
|     3 | TheincredibleHulk |     198000 | 2015 |
|     4 | WonderWoman       |    8996000 | 2017 |
|     5 | BlackWidow        |     563200 | 2019 |
+-------+-------------------+------------+------+


mysql> SELECT MovieName from Marvel;
+-------------------+
| MovieName         |
+-------------------+
| Ironman           |
| Thor:OdinKabeta   |
| TheincredibleHulk |
| WonderWoman       |
| BlackWidow        |
+-------------------+
---------------------------------------------------------------------------------------------------------------------------------------------------------

10 - # Unique  Constraints in Mysql -
    Unique constraint is uses for define a column as a primary key and maintain the uniquness of a column
    All the values in the column are unique


    mysql> CREATE TABLE Friends(
    -> SerialNumber int NOT NULL,
    -> Name varchar(255),
    -> MobileNumber int NOT NULL,
    -> Domain varchar(500),
    -> UNIQUE(Domain)
    -> );

    mysql> DESC Friends;
+--------------+--------------+------+-----+---------+-------+
| Field        | Type         | Null | Key | Default | Extra |
+--------------+--------------+------+-----+---------+-------+
| SerialNumber | int          | NO   |     | NULL    |       |
| Name         | varchar(255) | YES  |     | NULL    |       |
| MobileNumber | int          | NO   |     | NULL    |       |
| Domain       | varchar(500) | YES  | UNI | NULL    |       |
+--------------+--------------+------+-----+---------+-------+
---------------------------------------------------------------------------------------------------------------------------------------------------------

11 - # Constraints with Primary Key -
    Primary key constraint uniqly indentify each record in a table and it must contain a unique value and it cannot have null values 
    In primary key that coulumn or entity cannot be """null""" and should be #unique

     CREATE TABLE Employee(
    ->   EmpID int NOT NULL,
    ->   EmpNAME varchar(500),
    ->   EmpMOB int NOT NULL,
    ->   PRIMARY KEY(EmpID)
    ->   );

     
mysql> DESC Employee;
+---------+--------------+------+-----+---------+-------+
| Field   | Type         | Null | Key | Default | Extra |
+---------+--------------+------+-----+---------+-------+
| EmpID   | int          | NO   | PRI | NULL    |       |
| EmpNAME | varchar(500) | YES  |     | NULL    |       |
| EmpMOB  | int          | NO   |     | NULL    |       |
+---------+--------------+------+-----+---------+-------+
---------------------------------------------------------------------------------------------------------------------------------------------------------

12 - # Chekc Constrains in mysql

    CHECK Constrains check the given condition for entity
    CREATE TABLE Boys(
    BoyID int NOT NULL,
    BoyNAME varchar(255),
    BoyAGE int NOT NULL,
    BOYContact,
    CHECK(BoyAGE>20)
    );
  
    DESC Boys;
    +------------+--------------+------+-----+---------+-------+
| Field      | Type         | Null | Key | Default | Extra |
+------------+--------------+------+-----+---------+-------+
| BoyID      | int          | NO   |     | NULL    |       |
| BoyNAME    | varchar(255) | YES  |     | NULL    |       |
| BoyAGE     | int          | NO   |     | NULL    |       |
| BOYContact | int          | YES  |     | NULL    |       |
+------------+--------------+------+-----+---------+-------+

     INSERT INTO Boys(BoyID,BoyNAME,BoyAGE,BOYContact)
    -> VALUES (096,'Himanshu',17,97831);
# ERROR 3819 (HY000): Check constraint 'boys_chk_1' is violated.
It is showing error because CHECK is working as per the age should be > 20 and here for Himanshu the age is 17.

    INSERT INTO Boys(BoyID,BoyNAME,BoyAGE,BOYContact) 
    VALUES (088,'SHubham',22,966999); 
    INSERT INTO Boys(BoyID,BoyNAME,BoyAGE,BOYContact) 
    VALUES (090,'Divyanshu',21,98965); 
    INSERT INTO Boys(BoyID,BoyNAME,BoyAGE,BOYContact) 
    VALUES (093,'Vineet',25,98998);

    mysql> SELECT * FROM  Boys;
+-------+-----------+--------+------------+
| BoyID | BoyNAME   | BoyAGE | BOYContact |
+-------+-----------+--------+------------+
|    88 | SHubham   |     22 |     966999 |
|    90 | Divyanshu |     21 |      98965 |
|    93 | Vineet    |     25 |      98998 |
+-------+-----------+--------+------------+
---------------------------------------------------------------------------------------------------------------------------------------------------------

13 - # Default COnstrain in mysql :-

    Default Constrain allows a DEFAULT value to specified column
    CREATE TABLE Entries(
    EntryID int NOT NULL,
    EntryNAME varchar (200),
    EntryMOB int NOT NULL,
    EntryPASS varchar(300) DEFAULT 'ELIGIBLE'
    );

    mysql> DESC Entries;
+-----------+--------------+------+-----+----------+-------+
| Field     | Type         | Null | Key | Default  | Extra |
+-----------+--------------+------+-----+----------+-------+
| EntryID   | int          | NO   |     | NULL     |       |
| EntryNAME | varchar(200) | YES  |     | NULL     |       |
| EntryMOB  | int          | NO   |     | NULL     |       |
| EntryPASS | varchar(300) | YES  |     | ELIGIBLE |       |
+-----------+--------------+------+-----+----------+-------+

    INSERT INTO Entries(EntryID,EntryNAME,EntryMOB)
    VALUES (12,'Shubh',99);
    INSERT INTO Entries(EntryID,EntryNAME,EntryMOB)
    VALUES (15,'Rushi',100);
    INSERT INTO Entries(EntryID,EntryNAME,EntryMOB)
    VALUES (20,'Rohit',112);

    mysql> SELECT * FROM Entries;
+---------+-----------+----------+-----------+
| EntryID | EntryNAME | EntryMOB | EntryPASS |
+---------+-----------+----------+-----------+
|      12 | Shubh     |       99 | ELIGIBLE  |
|      15 | Rushi     |      100 | ELIGIBLE  |
|      20 | Rohit     |      112 | ELIGIBLE  |
+---------+-----------+----------+-----------+

# so here due to DEFAULT value(ELIGIBLE) passed to column(EntryPASS) its having that default value without any declaration
---------------------------------------------------------------------------------------------------------------------------------------------------------

14 - # Index Constraints in mysel : -

    mysql> SELECT * FROM Entries;
+---------+-----------+----------+-----------+
| EntryID | EntryNAME | EntryMOB | EntryPASS |
+---------+-----------+----------+-----------+
|      12 | Shubh     |       99 | ELIGIBLE  |
|      15 | Rushi     |      100 | ELIGIBLE  |
|      20 | Rohit     |      112 | ELIGIBLE  |
+---------+-----------+----------+-----------+

Create INDEX - 
 Syntax : - CREATE INDEX name_ofindex
            ON table_name(column_name);
            
    mysql> CREATE INDEX DEMOINDEX
    -> ON Entries(EntryNAME);

    mysql> SHOW INDEXES FROM Entries;
+---------+------------+-----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+---------+------------+
| Table   | Non_unique | Key_name        | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment | Index_comment | Visible | Expression |
+---------+------------+-----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+---------+------------+
| entries |          1 | DEMOINDEX       |            1 | EntryNAME   | A         |           3 |     NULL |   NULL | YES  | BTREE      |         |               | YES     | NULL       |
| entries |          1 | SECONDDEMOINDEX |            1 | EntryMOB    | A         |           3 |     NULL |   NULL |      | BTREE      |         |               | YES     | NULL       |
+---------+------------+-----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+---------+------------+
#here all created indexes are visible 

DROP index - 
Syntax : -  DROP INDEX name_ofindex
            ON table_name;    
    
    mysql> DROP INDEX DEMOINDEX ON Entries;
    mysql> SHOW INDEXES FROM Entries;
+---------+------------+-----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+---------+------------+
| Table   | Non_unique | Key_name        | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment | Index_comment | Visible | Expression |
+---------+------------+-----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+---------+------------+
| entries |          1 | SECONDDEMOINDEX |            1 | EntryMOB    | A         |           3 |     NULL |   NULL |      | BTREE      |         |
      | YES     | NULL       |
+---------+------------+-----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+---------+------------+
# on deleting one index using droop command only remains secondone
---------------------------------------------------------------------------------------------------------------------------------------------------------

15 - # Alter a Table(Add & Drop a column from an existing sql)
    aDDING A cOLM in a existing table-

Syntaxc - ALTER TABLE table_name
          ADD colm_name data_type;
          
        mysql> ALTER TABLE EMPLOYEE
        -> ADD EmpDEPT varchar(255);
        
        mysql> DESC EMPLOYEE;
+----------+--------------+------+-----+---------+-------+
| Field    | Type         | Null | Key | Default | Extra |
+----------+--------------+------+-----+---------+-------+
| EmpID    | int          | NO   |     | NULL    |       |
| FistName | varchar(50)  | YES  |     | NULL    |       |
| LastName | varchar(60)  | YES  |     | NULL    |       |
| EmpAGE   | int          | YES  |     | NULL    |       |
| EmpZONE  | varchar(25)  | YES  |     | NULL    |       |
| EmpDEPT  | varchar(255) | YES  |     | NULL    |       |
+----------+--------------+------+-----+---------+-------+

    deLeTInG A cOLM in a existing table-

Syntaxc - ALTER TABLE table_name
          DROP COLUMN colm_name_toremove;

          mysql> DESC EMPLOYEE;
          +----------+--------------+------+-----+---------+-------+
| Field    | Type         | Null | Key | Default | Extra |
+----------+--------------+------+-----+---------+-------+
| EmpID    | int          | NO   |     | NULL    |       |
| FistName | varchar(50)  | YES  |     | NULL    |       |
| LastName | varchar(60)  | YES  |     | NULL    |       |
| EmpAGE   | int          | YES  |     | NULL    |       |
| EmpZONE  | varchar(25)  | YES  |     | NULL    |       | 
+----------+--------------+------+-----+---------+-------+
---------------------------------------------------------------------------------------------------------------------------------------------------------

16 - # Alter a Table Modify a Column
    For modyfing a column use modify to column which need to edit

    mysql> DESC EMPLOYEE;
          +----------+--------------+------+-----+---------+-------+
| Field    | Type         | Null | Key | Default | Extra |
+----------+--------------+------+-----+---------+-------+
| EmpID    | int          | NO   |     | NULL    |       |
| FistName | varchar(50)  | YES  |     | NULL    |       |
| LastName | varchar(60)  | YES  |     | NULL    |       |
| EmpAGE   | int          | YES  |     | NULL    |       |
| EmpZONE  | varchar(25)  | YES  |     | NULL    |       | 
+----------+--------------+------+-----+---------+-------+

Syntax - 
        mysql>  ALTER TABLE EMPLOYEE
        -> MODIFY COLUMN EmpZONE int;

    mysql> DESC EMPLOYEE;
+----------+-------------+------+-----+---------+-------+
| Field    | Type        | Null | Key | Default | Extra |
+----------+-------------+------+-----+---------+-------+
| EmpID    | int         | NO   |     | NULL    |       |
| FistName | varchar(50) | YES  |     | NULL    |       |
| LastName | varchar(60) | YES  |     | NULL    |       |
| EmpAGE   | int         | YES  |     | NULL    |       |
| EmpZONE  | int         | YES  |     | NULL    |       |
+----------+-------------+------+-----+---------+-------+
---------------------------------------------------------------------------------------------------------------------------------------------------------

17 - # SELECT DISTINCT STATEMENT in mysql -
    Select Distinct statement is uses for remove similar values from a column. As DISTINCT elements only

     CREATE TABLE EMPLOYEE(
     EmpID int,
     FirstName varchar(20),
     LastName varchar(20),
     EmpAGE int,
     EmpZONE varchar(200)
     );

     mysql> DESC EMPLOYEE;
+-----------+--------------+------+-----+---------+-------+
| Field     | Type         | Null | Key | Default | Extra |
+-----------+--------------+------+-----+---------+-------+
| EmpID     | int          | YES  |     | NULL    |       |
| FirstName | varchar(20)  | YES  |     | NULL    |       |
| LastName  | varchar(20)  | YES  |     | NULL    |       |
| EmpAGE    | int          | YES  |     | NULL    |       |
| EmpZONE   | varchar(200) | YES  |     | NULL    |       |
+-----------+--------------+------+-----+---------+-------+

    INSERT INTO EMPLOYEE(EmpID,FirstName, LastName,EmpAGE,EmpZONE) VALUES
    (1,'jack','Sparrow',25,'NorthIndian');
    INSERT INTO EMPLOYEE(EmpID,FirstName,LastName,EmpAGE,EmpZONE) VALUES
    (2,'Tom','Hanks',25,'SouthIndian');
     INSERT INTO EMPLOYEE(EmpID,FirstName,LastName,EmpAGE,EmpZONE) VALUES
     (3,'Brad','Pitt',30,'WestIndian');
     INSERT INTO EMPLOYEE(EmpID,FirstName,LastName,EmpAGE,EmpZONE) VALUES
     (4,'Emma','Stone',27,'EastIndian');

     
mysql> SELECT * FROM EMPLOYEE;
+-------+-----------+----------+--------+-------------+
| EmpID | FirstName | LastName | EmpAGE | EmpZONE     |
+-------+-----------+----------+--------+-------------+
|     1 | jack      | Sparrow  |     25 | NorthIndian |
|     2 | Tom       | Hanks    |     25 | SouthIndian |
|     3 | Brad      | Pitt     |     30 | WestIndian  |
|     4 | Emma      | Stone    |     27 | EastIndian  |
+-------+-----------+----------+--------+-------------+


mysql> SELECT EmpAGE FROM EMPLOYEE;
+--------+
| EmpAGE |
+--------+
|     25 |
|     25 |
|     30 |
|     27 |
+--------+

mysql> SELECT DISTINCT EmpAGE FROM EMPLOYEE;
+--------+
| EmpAGE |
+--------+
|     25 |
|     30 |
|     27 |
+--------+
# so using this distinct statement, duplicate values can be deleted directly.
---------------------------------------------------------------------------------------------------------------------------------------------------------

18 - # Display Records from a specific Column
    We can desplya records from a specific column not from all columns

#For display whole table -
    SELECT * FROM tbale_name;
    mysql>  SELECT * FROM EMPLOYEE;
+-------+-----------+----------+--------+-------------+
| EmpID | FirstName | LastName | EmpAGE | EmpZONE     |
+-------+-----------+----------+--------+-------------+
|     1 | jack      | Sparrow  |     25 | NorthIndian |
|     2 | Tom       | Hanks    |     25 | SouthIndian |
|     3 | Brad      | Pitt     |     30 | WestIndian  |
|     4 | Emma      | Stone    |     27 | EastIndian  |
+-------+-----------+----------+--------+-------------+

#For display from a specific column
    SELECT colm_name FROM table_name;
    
    mysql> SELECT FirstName FROM EMPLOYEE;
+-----------+
| FirstName |
+-----------+
| jack      |
| Tom       |
| Brad      |
| Emma      |
+-----------+

#For display from more than one specific column
    SELECT colm1_name,colm2_name, colm3_name FROM table_name;

    mysql> SELECT FirstName, LastName, EmpAGE FROM EMPLOYEE;
+-----------+----------+--------+
| FirstName | LastName | EmpAGE |
+-----------+----------+--------+
| jack      | Sparrow  |     25 |
| Tom       | Hanks    |     25 |
| Brad      | Pitt     |     30 |
| Emma      | Stone    |     27 |
+-----------+----------+--------+
---------------------------------------------------------------------------------------------------------------------------------------------------------

19 -# Where Clause in mysql
    where clause is use for getting record as per filter or requirement

    mysql> SELECT * FROM EMPLOYEE;
+-------+-----------+----------+--------+-------------+
| EmpID | FirstName | LastName | EmpAGE | EmpZONE     |
+-------+-----------+----------+--------+-------------+
|     1 | jack      | Sparrow  |     25 | NorthIndian |
|     2 | Tom       | Hanks    |     25 | SouthIndian |
|     3 | Brad      | Pitt     |     30 | WestIndian  |
|     4 | Emma      | Stone    |     27 | EastIndian  |
+-------+-----------+----------+--------+-------------+


mysql> SELECT * FROM EMPLOYEE
    -> WHERE EmpAGE=25;
+-------+-----------+----------+--------+-------------+
| EmpID | FirstName | LastName | EmpAGE | EmpZONE     |
+-------+-----------+----------+--------+-------------+
|     1 | jack      | Sparrow  |     25 | NorthIndian |
|     2 | Tom       | Hanks    |     25 | SouthIndian |
+-------+-----------+----------+--------+-------------+

mysql> SELECT * FROM EMPLOYEE
    -> WHERE EmpAge<30;
+-------+-----------+----------+--------+-------------+
| EmpID | FirstName | LastName | EmpAGE | EmpZONE     |
+-------+-----------+----------+--------+-------------+
|     1 | jack      | Sparrow  |     25 | NorthIndian |
|     2 | Tom       | Hanks    |     25 | SouthIndian |
|     4 | Emma      | Stone    |     27 | EastIndian  |
+-------+-----------+----------+--------+-------------+
    
mysql> SELECT * FROM EMPLOYEE
    -> WHERE EmpAge>30;
Empty set (0.00 sec)

# operators,which we can use in where clause -
=
>
<
>=
<=
<>
BETWEEN
LIKE
IN

#  AND Opertor with Where Clause -
    mysql> SELECT * FROM EMPLOYEE;
+-------+-----------+----------+--------+-------------+
| EmpID | FirstName | LastName | EmpAGE | EmpZONE     |
+-------+-----------+----------+--------+-------------+
|     1 | jack      | Sparrow  |     25 | NorthIndian |
|     2 | Tom       | Hanks    |     25 | SouthIndian |
|     3 | Brad      | Pitt     |     30 | WestIndian  |
|     4 | Emma      | Stone    |     27 | EastIndian  |
+-------+-----------+----------+--------+-------------+

    mysql> SELECT * FROM EMPLOYEE
    -> WHERE EmpAGE=25 AND EmpZONE='SouthIndian';
+-------+-----------+----------+--------+-------------+
| EmpID | FirstName | LastName | EmpAGE | EmpZONE     |
+-------+-----------+----------+--------+-------------+
|     2 | Tom       | Hanks    |     25 | SouthIndian |
+-------+-----------+----------+--------+-------------+

#  more than one AND Opertor with Where Clause -
     mysql> SELECT * FROM EMPLOYEE
     -> WHERE EmpAGE=25 AND EmpZONE='NorthIndian' AND LastName='Sparrow';
+-------+-----------+----------+--------+-------------+
| EmpID | FirstName | LastName | EmpAGE | EmpZONE     |
+-------+-----------+----------+--------+-------------+
|     1 | jack      | Sparrow  |     25 | NorthIndian |
+-------+-----------+----------+--------+-------------+
"""And Selecting for both the conditions"""
    
#  OR Opertor with Where Clause -
    mysql> SELECT * FROM EMPLOYEE;
+-------+-----------+----------+--------+-------------+
| EmpID | FirstName | LastName | EmpAGE | EmpZONE     |
+-------+-----------+----------+--------+-------------+
|     1 | jack      | Sparrow  |     25 | NorthIndian |
|     2 | Tom       | Hanks    |     25 | SouthIndian |
|     3 | Brad      | Pitt     |     30 | WestIndian  |
|     4 | Emma      | Stone    |     27 | EastIndian  |
+-------+-----------+----------+--------+-------------+

    mysql> SELECT * FROM EMPLOYEE
    -> WHERE EmpZONE='SouthIndian' OR empZONE='WestIndian';
+-------+-----------+----------+--------+-------------+
| EmpID | FirstName | LastName | EmpAGE | EmpZONE     |
+-------+-----------+----------+--------+-------------+
|     2 | Tom       | Hanks    |     25 | SouthIndian |
|     3 | Brad      | Pitt     |     30 | WestIndian  |
+-------+-----------+----------+--------+-------------+

mysql> SELECT * FROM EMPLOYEE
    -> WHERE FirstName='Tom' OR LastName='Stone';
+-------+-----------+----------+--------+-------------+
| EmpID | FirstName | LastName | EmpAGE | EmpZONE     |
+-------+-----------+----------+--------+-------------+
|     2 | Tom       | Hanks    |     25 | SouthIndian |
|     4 | Emma      | Stone    |     27 | EastIndian  |
+-------+-----------+----------+--------+-------------+
"""OR Selecting for either of the or both if find conditions"""

#  NOT Opertor with Where Clause -

    mysql> SELECT * FROM EMPLOYEE;
+-------+-----------+----------+--------+-------------+
| EmpID | FirstName | LastName | EmpAGE | EmpZONE     |
+-------+-----------+----------+--------+-------------+
|     1 | jack      | Sparrow  |     25 | NorthIndian |
|     2 | Tom       | Hanks    |     25 | SouthIndian |
|     3 | Brad      | Pitt     |     30 | WestIndian  |
|     4 | Emma      | Stone    |     27 | EastIndian  |
+-------+-----------+----------+--------+-------------+
    mysql> SELECT * FROM EMPLOYEE
    -> WHERE NOT EmpAGE=30;
+-------+-----------+----------+--------+-------------+
| EmpID | FirstName | LastName | EmpAGE | EmpZONE     |
+-------+-----------+----------+--------+-------------+
|     1 | jack      | Sparrow  |     25 | NorthIndian |
|     2 | Tom       | Hanks    |     25 | SouthIndian |
|     4 | Emma      | Stone    |     27 | EastIndian  |
+-------+-----------+----------+--------+-------------+

mysql> SELECT * FROM EMPLOYEE
    -> WHERE NOT FirstName='jack';
+-------+-----------+----------+--------+-------------+
| EmpID | FirstName | LastName | EmpAGE | EmpZONE     |
+-------+-----------+----------+--------+-------------+
|     2 | Tom       | Hanks    |     25 | SouthIndian |
|     3 | Brad      | Pitt     |     30 | WestIndian  |
|     4 | Emma      | Stone    |     27 | EastIndian  |
+-------+-----------+----------+--------+-------------+
"""NOT wll not sekect to not waali condition"""
---------------------------------------------------------------------------------------------------------------------------------------------------------

20 - #Single Line and Multi Line Comment in Mysql -
    "Single Line Comment" can be do with (--) OR (#)
        mysql> SELECT * FROM EMPLOYEE; # i AM just trying for single line comment using hash in mysql
+-------+-----------+----------+--------+-------------+
| EmpID | FirstName | LastName | EmpAGE | EmpZONE     |
+-------+-----------+----------+--------+-------------+
|     1 | jack      | Sparrow  |     25 | NorthIndian |
|     2 | Tom       | Hanks    |     25 | SouthIndian |
|     3 | Brad      | Pitt     |     30 | WestIndian  |
|     4 | Emma      | Stone    |     27 | EastIndian  |
+-------+-----------+----------+--------+-------------+


    mysql> SELECT * FROM EMPLOYEE; -- checking double dash for Single Line Comment in mysql
+-------+-----------+----------+--------+-------------+
| EmpID | FirstName | LastName | EmpAGE | EmpZONE     |
+-------+-----------+----------+--------+-------------+
|     1 | jack      | Sparrow  |     25 | NorthIndian |
|     2 | Tom       | Hanks    |     25 | SouthIndian |
|     3 | Brad      | Pitt     |     30 | WestIndian  |
|     4 | Emma      | Stone    |     27 | EastIndian  |
+-------+-----------+----------+--------+-------------+
    "Multi Line Comment" by same method as we do in Visual in C++
        mysql> SELECT /*
   /*> i AM HERE
   /*> and trying fot
   /*> how to use multi line commeny
   /*> in sql
   /*> So its working fine.
   /*> */
    -> * FROM EMPLOYEE;
+-------+-----------+----------+--------+-------------+
| EmpID | FirstName | LastName | EmpAGE | EmpZONE     |
+-------+-----------+----------+--------+-------------+
|     1 | jack      | Sparrow  |     25 | NorthIndian |
|     2 | Tom       | Hanks    |     25 | SouthIndian |
|     3 | Brad      | Pitt     |     30 | WestIndian  |
|     4 | Emma      | Stone    |     27 | EastIndian  |
+-------+-----------+----------+--------+-------------+
---------------------------------------------------------------------------------------------------------------------------------------------------------

21 - # Count() Function in mysql -
       count() Function uses for count specified condition

     mysql> SELECT COUNT(EmpAGE) FROM EMPLOYEE
     -> WHERE EmpAGE=25;
+---------------+
| COUNT(EmpAGE) |
+---------------+
|             2 |
+---------------+

    mysql> SELECT COUNT(*)
    -> FROM EMPLOYEE;
+----------+
| COUNT(*) |
+----------+
|        4 |
+----------+
---------------------------------------------------------------------------------------------------------------------------------------------------------

22 - # ALIAS(AS) in MYSQL -
     Uses for changing heading or record.ALIAS stands for As. change heading AS new_name
     mysql> SELECT * FROM EMPLOYEE;
+-------+-----------+----------+--------+-------------+
| EmpID | FirstName | LastName | EmpAGE | EmpZONE     |
+-------+-----------+----------+--------+-------------+
|     1 | jack      | Sparrow  |     25 | NorthIndian |
|     2 | Tom       | Hanks    |     25 | SouthIndian |
|     3 | Brad      | Pitt     |     30 | WestIndian  |
|     4 | Emma      | Stone    |     27 | EastIndian  |
+-------+-----------+----------+--------+-------------+

Syntax - SELECT com_name AS jo_naam_aap_dena_chaahe

    mysql> SELECT EmpAGE AS AGE_OF_eMPLOYEES
    -> FROM EMPLOYEE;
+------------------+
| AGE_OF_eMPLOYEES |
+------------------+
|               25 |
|               25 |
|               30 |
|               27 |
+------------------+
    
    mysql> SELECT EmpZONE AS gAME_oF_tHroNes
    -> FROM EMPLOYEE;
+-----------------+
| gAME_oF_tHroNes |
+-----------------+
| NorthIndian     |
| SouthIndian     |
| WestIndian      |
| EastIndian      |
+-----------------+

""" Multiple colmn names can also be change at a time seprated by , and by AS """"        

Syntax - SELECT com_name AS jo_naam_aap_dena_chaahe1, com_name AS jo_naam_aap_dena_chaahe2
        
    mysql> SELECT FirstName AS NAMe1, LastName as NAMe2
    -> FROM EMPLOYEE;
+-------+---------+
| NAMe1 | NAMe2   |
+-------+---------+
| jack  | Sparrow |
| Tom   | Hanks   |
| Brad  | Pitt    |
| Emma  | Stone   |
+-------+---------+
---------------------------------------------------------------------------------------------------------------------------------------------------------

23 - # IN & NOT In Operator in Mysql -
     """In""" Operator uses for take any columns selected values

Syntax In operator -
         SELECT * FROM EMPLOYEE
         WHERE colm_name IN('colm_record1_wants_to_put_in_IN','colm_record2_wants_to_put_in_IN')
        
     mysql> SELECT * FROM EMPLOYEE
    -> WHERE EmpZONE IN('NorthIndian','SouthIndian');
+-------+-----------+----------+--------+-------------+
| EmpID | FirstName | LastName | EmpAGE | EmpZONE     |
+-------+-----------+----------+--------+-------------+
|     1 | jack      | Sparrow  |     25 | NorthIndian |
|     2 | Tom       | Hanks    |     25 | SouthIndian |
+-------+-----------+----------+--------+-------------+

Syntax NOT In operator -
         SELECT * FROM EMPLOYEE
         WHERE colm_name NOT IN('colm_record1_NOT_wants_to_put_in_IN','colm_record2_NOT_wants_to_put_in_IN')
        
    mysql> SELECT * FROM EMPLOYEE
    -> WHERE EmpZONE NOT IN ('NorthIndian','SouthIndian');
+-------+-----------+----------+--------+------------+
| EmpID | FirstName | LastName | EmpAGE | EmpZONE    |
+-------+-----------+----------+--------+------------+
|     3 | Brad      | Pitt     |     30 | WestIndian |
|     4 | Emma      | Stone    |     27 | EastIndian |
+-------+-----------+----------+--------+------------+
---------------------------------------------------------------------------------------------------------------------------------------------------------

24 - # LiKE Operaotr in Mysql -
      uses for select the same in records of a column. It use % operator. becuase we don't know how many character will be dimilar after 1st common character, therefore uses %operator

      mysql> SELECT * FROM EMPLOYEE;
+-------+-----------+----------+--------+---------+
| EmpID | FirstName | LastName | EmpAGE | EmpZONE |
+-------+-----------+----------+--------+---------+
|     1 | jack      | Sparrow  |     25 | North   |
|     2 | Tommy     | Hanks    |     25 | South   |
|     3 | Brad      | Pitt     |     30 | West    |
|     4 | Tommy     | Stone    |     27 | East    |
+-------+-----------+----------+--------+---------+

Syntax - SELECT * FROM EMPLOYEE
        WHERE colm_name LIKE 'satrtwith%';

#Qun : - Select all Employees name which started with T.
        mysql> SELECT * FROM EMPLOYEE
    ->  WHERE FirstName LIKE 'T%';
+-------+-----------+----------+--------+---------+
| EmpID | FirstName | LastName | EmpAGE | EmpZONE |
+-------+-----------+----------+--------+---------+
|     2 | Tommy     | Hanks    |     25 | South   |
|     4 | Tommy     | Stone    |     27 | East    |
+-------+-----------+----------+--------+---------+
"""t%""" - Start with t
"""Here using LIKE 'T%' it takes common words started from T from record from specified column(FirstName)"""        
        

# Qun : - Select all the Employees name which started with H.
        
        mysql>  SELECT * FROM EMPLOYEE
    ->   WHERE LastName LIKE 'S%';
+-------+-----------+----------+--------+---------+
| EmpID | FirstName | LastName | EmpAGE | EmpZONE |
+-------+-----------+----------+--------+---------+
|     1 | jack      | Sparrow  |     25 | North   |
|     4 | Tommy     | Stone    |     27 | East    |
+-------+-----------+----------+--------+---------+
"""s%""" - Start with s
"""Here using LIKE 'S%' it takes common words started from T from record from specified column(LastName)"""        

        
        mysql>  SELECT * FROM EMPLOYEE
        -> WHERE LastName LIKE 'm%';
        Empty set (0.00 sec)

Syntax - SELECT * FROM EMPLOYEE
        WHERE colm_name LIKE '%endwith';        

#Qun - Select All employees whoose zone ends with h.
        mysql> SELECT * FROM EMPLOYEE
        -> WHERE EmpZONE LIKE '%h';
+-------+-----------+----------+--------+---------+
| EmpID | FirstName | LastName | EmpAGE | EmpZONE |
+-------+-----------+----------+--------+---------+
|     1 | jack      | Sparrow  |     25 | North   |
|     2 | Tommy     | Hanks    |     25 | South   |
+-------+-----------+----------+--------+---------+
"""%h""" - END with h        


        mysql> SELECT * FROM EMPLOYEE
        -> WHERE EmpZONE LIKE '%t';
+-------+-----------+----------+--------+---------+
| EmpID | FirstName | LastName | EmpAGE | EmpZONE |
+-------+-----------+----------+--------+---------+
|     3 | Brad      | Pitt     |     30 | West    |
|     4 | Tommy     | Stone    |     27 | East    |
+-------+-----------+----------+--------+---------+
"""%t""" - END with t

#Qun - Find out those employees whhoose employeezone consist t at 4th possition ?
        
     mysql> SELECT *  FROM EMPLOYEE
    -> WHERE EmpZONE LIKE '___%t';
+-------+-----------+----------+--------+---------+
| EmpID | FirstName | LastName | EmpAGE | EmpZONE |
+-------+-----------+----------+--------+---------+
|     3 | Brad      | Pitt     |     30 | West    |
|     4 | Tommy     | Stone    |     27 | East    |
+-------+-----------+----------+--------+---------+
---------------------------------------------------------------------------------------------------------------------------------------------------------        

25 -# Between & Not Between Operator in MySQl -
    Between Operator uses as per the name it selects in record between boundary limits
     
    mysql> SELECT * FROM EMPLOYEE;
+-------+-----------+----------+--------+---------+
| EmpID | FirstName | LastName | EmpAGE | EmpZONE |
+-------+-----------+----------+--------+---------+
|     1 | jack      | Sparrow  |     25 | North   |
|     2 | Tommy     | Hanks    |     26 | South   |
|     3 | Brad      | Pitt     |     28 | West    |
|     4 | Tommy     | Stone    |     30 | East    |
+-------+-----------+----------+--------+---------+

Syntax - mysql> SELECT * FROM table_name
        -> WHERE colm_name BETWEEN record1 AND record2;
        
        mysql> SELECT * FROM EMPLOYEE
        -> WHERE EmpAGE BETWEEN 25 AND 30;
+-------+-----------+----------+--------+---------+
| EmpID | FirstName | LastName | EmpAGE | EmpZONE |
+-------+-----------+----------+--------+---------+
|     1 | jack      | Sparrow  |     25 | North   |
|     2 | Tommy     | Hanks    |     26 | South   |
|     3 | Brad      | Pitt     |     28 | West    |
|     4 | Tommy     | Stone    |     30 | East    |
+-------+-----------+----------+--------+---------+

Syntax - mysql> SELECT * FROM table_name
        -> WHERE colm_name NOT BETWEEN record1 AND record2;        

    mysql> SELECT * FROM EMPLOYEE
    -> WHERE EmpAGE NOT BETWEEN 25 AND 28;
+-------+-----------+----------+--------+---------+
| EmpID | FirstName | LastName | EmpAGE | EmpZONE |
+-------+-----------+----------+--------+---------+
|     4 | Tommy     | Stone    |     30 | East    |
+-------+-----------+----------+--------+---------+
---------------------------------------------------------------------------------------------------------------------------------------------------------

26 - #Case Statement in MySQL -
      Case statement is uses for perfect match and answer showing.

    mysql> SELECT * FROM EMPLOYEE;
+-------+-----------+----------+--------+---------+
| EmpID | FirstName | LastName | EmpAGE | EmpZONE |
+-------+-----------+----------+--------+---------+
|     1 | jack      | Sparrow  |     25 | North   |
|     2 | Tommy     | Hanks    |     26 | South   |
|     3 | Brad      | Pitt     |     28 | West    |
|     4 | Tommy     | Stone    |     30 | East    |
+-------+-----------+----------+--------+---------+

Syntax - SELECT col_name1,col_name2,col_name3
         CASE
         CONDITION FOR COLUMNS
         ENDS AS LAST_COLUMN
         FROM table_name


    mysql> SELECT FirstName, LastName, EmpAGE,
    ->   CASE
    ->   WHEN EmpAGE > 25 THEN 'Employee with experience. Eligible for senior profile'
    ->   WHEN EmpAGE = 25 THEN 'Employee is at mid-level, say him to keep it up'
    ->   ELSE 'Freshers... nned much experience'
    ->   END AS ELIGIBILITY
    ->   FROM EMPLOYEE;
+-----------+----------+--------+-------------------------------------------------------+
| FirstName | LastName | EmpAGE | ELIGIBILITY
                             |
+-----------+----------+--------+-------------------------------------------------------+
| jack      | Sparrow  |     25 | Employee is at mid-level, say him to keep it up       |
| Tommy     | Hanks    |     26 | Employee with experience. Eligible for senior profile |
| Brad      | Pitt     |     28 | Employee with experience. Eligible for senior profile |
| Tommy     | Stone    |     30 | Employee with experience. Eligible for senior profile |
+-----------+----------+--------+-------------------------------------------------------+
"""Using CASE STATEMENT""" CREATED DIFFERENT CASES AND MATCHES FOR A RECORD.
->   END AS ELIGIBILITY - used ALIS Operator by named as END.
---------------------------------------------------------------------------------------------------------------------------------------------------------

27 - # Delete/tRUNCATE statement in MYSQL
      
    mysql> SELECT * FROM EMPLOYEE;
+-------+-----------+----------+--------+---------+
| EmpID | FirstName | LastName | EmpAGE | EmpZONE |
+-------+-----------+----------+--------+---------+
|     1 | jack      | Sparrow  |     25 | North   |
|     2 | Tommy     | Hanks    |     26 | South   |
|     3 | Brad      | Pitt     |     28 | West    |
|     4 | Tommy     | Stone    |     30 | East    |
+-------+-----------+----------+--------+---------+

DELETE  a specific record :  -
sYNTAX - DELETE FROM EMPLOYEE
         WHERE colm_name='record_which_delete';
        
    mysql> DELETE FROM EMPLOYEE
        -> WHERE EmpZONE='West';


    mysql> SELECT * FROM EMPLOYEE;
+-------+-----------+----------+--------+---------+
| EmpID | FirstName | LastName | EmpAGE | EmpZONE |
+-------+-----------+----------+--------+---------+
|     1 | jack      | Sparrow  |     25 | North   |
|     2 | Tommy     | Hanks    |     26 | South   |
|     4 | Tommy     | Stone    |     30 | East    |
+-------+-----------+----------+--------+---------+  
        
DELETE All The Records From The Table -
sYNTax - DELETE FROM table_name;
         For see delete or not - SELECT * FROM table_name;

        mysql> DELETE FROM EMPLOYEE;
        mysql> SELECT * FROM EMPLOYEE;
        Empty set

        
    mysql> DESC EMPLOYEE;
+-----------+--------------+------+-----+---------+-------+
| Field     | Type         | Null | Key | Default | Extra |
+-----------+--------------+------+-----+---------+-------+
| EmpID     | int          | YES  |     | NULL    |       |
| FirstName | varchar(20)  | YES  |     | NULL    |       |
| LastName  | varchar(20)  | YES  |     | NULL    |       |
| EmpAGE    | int          | YES  |     | NULL    |       |
| EmpZONE   | varchar(200) | YES  |     | NULL    |       |
+-----------+--------------+------+-----+---------+-------+
# NOTE : - using DELETE, all the record will be deleted but the table structure or description will remain same
---------------------------------------------------------------------------------------------------------------------------------------------------------
28 - # Update Statement in mysql -


    mysql> SELECT * FROM EMPLOYEE;
+-------+-----------+----------+--------+---------+
| EmpID | FirstName | LastName | EmpAGE | EmpZONE |
+-------+-----------+----------+--------+---------+
|     1 | jack      | Sparrow  |     25 | North   |
|     2 | Tommy     | Hanks    |     26 | South   |
|     3 | Brad      | Pitt     |     28 | West    |
|     4 | Tommy     | Stone    |     30 | East    |
+-------+-----------+----------+--------+---------+
#uPDATIOn of Single record -

Syntax - UPDATE table_name
        SET colm_name = new_data
        WHERE colm_name(idemtity)= where need to edit;
        
     mysql> UPDATE EMPLOYEE
     -> SET EmpAGE = 24
     -> WHERE EmpID=3;

    mysql> SELECT * FROM EMPLOYEE;
+-------+-----------+----------+--------+---------+
| EmpID | FirstName | LastName | EmpAGE | EmpZONE |
+-------+-----------+----------+--------+---------+
|     1 | jack      | Sparrow  |     25 | North   |
|     2 | Tommy     | Hanks    |     26 | South   |
|     3 | Brad      | Pitt     |     24 | West    |
|     4 | Tommy     | Stone    |     30 | East    |
+-------+-----------+----------+--------+---------+
@uPDATION Oof More Than One record -
    mysql> UPDATE EMPLOYEE
    -> SET EmpAGE = 27
    -> WHERE FirstName='eMMA';

        
    mysql> SELECT * FROM EMPLOYEE;
+-------+-----------+----------+--------+---------+
| EmpID | FirstName | LastName | EmpAGE | EmpZONE |
+-------+-----------+----------+--------+---------+
|     1 | jack      | Sparrow  |     25 | North   |
|     2 | eMMA      | Hanks    |     27 | South   |
|     3 | Brad      | Pitt     |     28 | West    |
|     4 | eMMA      | Stone    |     27 | East    |
+-------+-----------+----------+--------+---------+
---------------------------------------------------------------------------------------------------------------------------------------------------------

29 - #Drop Table Statement in MYSQL -
      Drop Table Command is uses for Delete the entire Tabele """Record""" as well as """Structure/Description"""


    mysql> DESC EMPLOYEE;
+-----------+--------------+------+-----+---------+-------+
| Field     | Type         | Null | Key | Default | Extra |
+-----------+--------------+------+-----+---------+-------+
| EmpID     | int          | YES  |     | NULL    |       |
| FirstName | varchar(20)  | YES  |     | NULL    |       |
| LastName  | varchar(20)  | YES  |     | NULL    |       |
| EmpAGE    | int          | YES  |     | NULL    |       |
| EmpZONE   | varchar(200) | YES  |     | NULL    |       |
+-----------+--------------+------+-----+---------+-------+
        
    mysql> SELECT * FROM EMPLOYEE;
+-------+-----------+----------+--------+---------+
| EmpID | FirstName | LastName | EmpAGE | EmpZONE |
+-------+-----------+----------+--------+---------+
|     1 | jack      | Sparrow  |     25 | North   |
|     2 | eMMA      | Hanks    |     27 | South   |
|     3 | Brad      | Pitt     |     28 | West    |
|     4 | eMMA      | Stone    |     27 | East    |
+-------+-----------+----------+--------+---------+
        
    Syntax - DROP TABLE table_name;
        
    mysql> DROP TABLE EMPLOYEE;
    
    mysql> SELECT * FROM EMPLOYEE;
    ERROR 1146 (42S02): Table 'shubhdb1.employee' doesn't exist
    mysql> DESC EMPLOYEE;
    ERROR 1146 (42S02): Table 'shubhdb1.employee' doesn't exist
---------------------------------------------------------------------------------------------------------------------------------------------------------

30 - #Drop Databse in mysql -         
    uSES for drop a database from schema in mysql -

    Syntax - DROP DATABASE dab_name;
    
    mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| shubhdb1           |
+--------------------+
    mysql> CREATE DATABASE Jarvis;

    
    mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| shubhdb1           |
+--------------------+
---------------------------------------------------------------------------------------------------------------------------------------------------------

31 - # Avg() function in mysql
      uSES for get the avg of given numerical data of a column

            
    mysql> SELECT * FROM EMPLOYEE;
+-------+-----------+----------+--------+---------+
| EmpID | FirstName | LastName | EmpAGE | EmpZONE |
+-------+-----------+----------+--------+---------+
|     1 | jack      | Sparrow  |     25 | North   |
|     2 | TOM       | Hanks    |     26 | South   |
|     3 | Brad      | Pitt     |     28 | West    |
|     4 | eMMA      | Stone    |     30 | East    |
+-------+-----------+----------+--------+---------+


Syntax - SELECT  AVG(colm_name_whoose_avg)
                FROM table_name;
        
    mysql> SELECT AVG(EmpAGE)
        -> FROM EMPLOYEE;
+-------------+
| AVG(EmpAGE) |
+-------------+
|     27.2500 |
+-------------+
---------------------------------------------------------------------------------------------------------------------------------------------------------

32 - #Sum() Function in mysql -
       uses for get the sum of given numerical data of a column

        mysql> SELECT * FROM EMPLOYEE;
+-------+-----------+----------+--------+---------+
| EmpID | FirstName | LastName | EmpAGE | EmpZONE |
+-------+-----------+----------+--------+---------+
|     1 | jack      | Sparrow  |     25 | North   |
|     2 | TOM       | Hanks    |     26 | South   |
|     3 | Brad      | Pitt     |     28 | West    |
|     4 | eMMA      | Stone    |     30 | East    |
+-------+-----------+----------+--------+---------+

        Syntax - SELECT SUM(colm_name_whoose_sum)
                 FROM table_name;   
        
        mysql> SELECT SUM(EmpAGE)
            -> FROM EMPLOYEE;
+-------------+
| SUM(EmpAGE) |
+-------------+
|         109 |
+-------------+
        
        mysql> SELECT SUM(EmpAGE) AS Result
            -> FROM EMPLOYEE;
+--------+
| Result |
+--------+
|    109 |
+--------+
---------------------------------------------------------------------------------------------------------------------------------------------------------
33- # Order By Keyword in mysql -
     uses for arranging in increasing order as per record of column

    
    mysql> SELECT * FROM EMPLOYEE;
+-------+-----------+----------+--------+---------+
| EmpID | FirstName | LastName | EmpAGE | EmpZONE |
+-------+-----------+----------+--------+---------+
|     1 | jack      | Sparrow  |     25 | North   |
|     2 | TOM       | Hanks    |     22 | South   |
|     3 | Brad      | Pitt     |     28 | West    |
|     4 | eMMA      | Stone    |     20 | East    |
+-------+-----------+----------+--------+---------+

For """increasing/Ascending Order """ - 
    Syntax - SELECT * FROM table_name
             ORDER BY colm_name;
            
    mysql> SELECT * FROM EMPLOYEE
    -> ORDER BY EmpAGE;
+-------+-----------+----------+--------+---------+
| EmpID | FirstName | LastName | EmpAGE | EmpZONE |
+-------+-----------+----------+--------+---------+
|     4 | eMMA      | Stone    |     20 | East    |
|     2 | TOM       | Hanks    |     22 | South   |
|     1 | jack      | Sparrow  |     25 | North   |
|     3 | Brad      | Pitt     |     28 | West    |
+-------+-----------+----------+--------+---------+
        

For """decreasing/descending Order """ -         
        Syntax - SELECT * FROM table_name
                 ORDER BY colm_name DESC;   
       
        mysql> SELECT * FROM EMPLOYEE
             -> ORDER BY EmpAGE DESC;
+-------+-----------+----------+--------+---------+
| EmpID | FirstName | LastName | EmpAGE | EmpZONE |
+-------+-----------+----------+--------+---------+
|     3 | Brad      | Pitt     |     28 | West    |
|     1 | jack      | Sparrow  |     25 | North   |
|     2 | TOM       | Hanks    |     22 | South   |
|     4 | eMMA      | Stone    |     20 | East    |
+-------+-----------+----------+--------+---------+        
---------------------------------------------------------------------------------------------------------------------------------------------------------
34 - # Auto Increment in Mysql-
       Uses for increment in serial number or particular data of column automatically uniqly.(primary key, so not repeated)

Synatx - CREATE TABLE table_name(
         colm1 int NOT NULL AUTO_INCREMENT,
         colm2 data_type,
         colm3 data_type,
         colm4 int,
         colm5 data_type,
         PRIMARY KEY(col1)
     );

     CREATE TABLE EMPLOYEE(
     EmpID int NOT NULL AUTO_INCREMENT,
     FirstName varchar(20),
     LastName varchar(20),
     EmpAGE int,
     EmpZONE varchar(200),
     PRIMARY KEY(EmpID)
     );

    INSERT INTO EMPLOYEE(FirstName, LastName,EmpAGE,EmpZONE) VALUES
    ('jack','Sparrow',25,'North');
    INSERT INTO EMPLOYEE(FirstName,LastName,EmpAGE,EmpZONE) VALUES
    ('TOM','Hanks',22,'South');
     INSERT INTO EMPLOYEE(FirstName,LastName,EmpAGE,EmpZONE) VALUES
     ('Brad','Pitt',28,'West');
     INSERT INTO EMPLOYEE(FirstName,LastName,EmpAGE,EmpZONE) VALUES
     ('eMMA','Stone',20,'East');

    
    mysql> SELECT * FROM EMPLOYEE;
+-------+-----------+----------+--------+---------+
| EmpID | FirstName | LastName | EmpAGE | EmpZONE |
+-------+-----------+----------+--------+---------+
|     1 | jack      | Sparrow  |     25 | North   |
|     2 | TOM       | Hanks    |     22 | South   |
|     3 | Brad      | Pitt     |     28 | West    |
|     4 | eMMA      | Stone    |     20 | East    |
+-------+-----------+----------+--------+---------+
So using Auto Increment selected Column is increasing its seraial number or ID as per noo. od records
---------------------------------------------------------------------------------------------------------------------------------------------------------

35 - # Max() Function in Mysql-
     uses to get maxium from data of a column

        
    mysql> SELECT * FROM EMPLOYEE;
+-------+-----------+----------+--------+---------+
| EmpID | FirstName | LastName | EmpAGE | EmpZONE |
+-------+-----------+----------+--------+---------+
|     1 | jack      | Sparrow  |     25 | North   |
|     2 | TOM       | Hanks    |     22 | South   |
|     3 | Brad      | Pitt     |     28 | West    |
|     4 | eMMA      | Stone    |     20 | East    |
+-------+-----------+----------+--------+---------+


Synatx - SELECT MAX(colm_name_whoose_max)
         FROM table_name;
        
    mysql> SELECT MAX(EmpAGE) AS LargestAge
        -> FROM EMPLOYEE;
+------------+
| LargestAge |
+------------+
|         28 |
+------------+
---------------------------------------------------------------------------------------------------------------------------------------------------------

36 - # Min() Function in Mysql-
      uses to get manimum from data of a column  
       mysql> SELECT * FROM EMPLOYEE;
+-------+-----------+----------+--------+---------+
| EmpID | FirstName | LastName | EmpAGE | EmpZONE |
+-------+-----------+----------+--------+---------+
|     1 | jack      | Sparrow  |     25 | North   |
|     2 | TOM       | Hanks    |     22 | South   |
|     3 | Brad      | Pitt     |     28 | West    |
|     4 | eMMA      | Stone    |     20 | East    |
+-------+-----------+----------+--------+---------+


Synatx - SELECT MIN(colm_name_whoose_max)
         FROM table_name;
        
    mysql> SELECT MIN(EmpAGE) AS LargestAge
        -> FROM EMPLOYEE;

+------------+
| LargestAge |
+------------+
|         20 |
+------------+        
---------------------------------------------------------------------------------------------------------------------------------------------------------
        
37 - # Limit Clause in mysql -
      uSes for how many records to return. It limit that according to gievn requirement.

      
    mysql> SELECT * FROM EMPLOYEE;
+-------+-----------+----------+--------+---------+
| EmpID | FirstName | LastName | EmpAGE | EmpZONE |
+-------+-----------+----------+--------+---------+
|     1 | jack      | Sparrow  |     25 | North   |
|     2 | TOM       | Hanks    |     22 | South   |
|     3 | Brad      | Pitt     |     28 | West    |
|     4 | eMMA      | Stone    |     20 | East    |
+-------+-----------+----------+--------+---------+

sYNtax - SELECT * FROM table_name
         LIMIT No_as_require;   

        mysql> SELECT * FROM EMPLOYEE
            -> LIMIT 2;
+-------+-----------+----------+--------+---------+
| EmpID | FirstName | LastName | EmpAGE | EmpZONE |
+-------+-----------+----------+--------+---------+
|     1 | jack      | Sparrow  |     25 | North   |
|     2 | TOM       | Hanks    |     22 | South   |
+-------+-----------+----------+--------+---------+


    mysql> SELECT * FROM EMPLOYEE
        -> LIMIT 3;
+-------+-----------+----------+--------+---------+
| EmpID | FirstName | LastName | EmpAGE | EmpZONE |
+-------+-----------+----------+--------+---------+
|     1 | jack      | Sparrow  |     25 | North   |
|     2 | TOM       | Hanks    |     22 | South   |
|     3 | Brad      | Pitt     |     28 | West    |
+-------+-----------+----------+--------+---------+
---------------------------------------------------------------------------------------------------------------------------------------------------------

38 - # Joins in Mysql -
      Join is a Clause. It is used to combine rows from 2 or more table. There are 4 types of Joins
     i - Inner Join
     ii - Left Join
     iii - Right Join
     iv - Full Join(not Supported by Mysql) 

    mysql> SELECT * FROM EMPLOYEE;
+-------+--------+----------------+
| EmpID | DeptID | EmpName        |
+-------+--------+----------------+
|   100 |      2 | Tom Hanks      |
|   101 |      4 | Bradely Cooper |
|   102 |      3 | jack Sparrow   |
+-------+--------+----------------+

    
    mysql> SELECT * FROM DEPARTMENT;
+--------+------------+----------+
| DeptID | DeptName   | DeptZONE |
+--------+------------+----------+
|      1 | Operations | North    |
|      2 | Finance    | South    |
|      3 | Marketing  | East     |
+--------+------------+----------+

        # using Inner Join -

    mysql> SELECT EMPLOYEE.EmpID,DEPARTMENT.DeptName
        -> FROM EMPLOYEE
        -> INNER JOIN DEPARTMENT ON EMPLOYEE.DeptID = DEPARTMENT.DeptID;
    
+-------+-----------+
| EmpID | DeptName  |
+-------+-----------+
|   100 | Finance   |
|   102 | Marketing |
+-------+-----------+

        # using LEFT Join -
        
    mysql> SELECT EMPLOYEE.EmpID,DEPARTMENT.DeptName
        -> FROM DEPARTMENT
        -> LEFT JOIN EMPLOYEE ON EMPLOYEE.DeptID = DEPARTMENT.DEPTID;

+-------+------------+
| EmpID | DeptName   |
+-------+------------+
|  NULL | Operations |
|   100 | Finance    |
|   102 | Marketing  |
+-------+------------+
        
        # using RIGHT Join -

    mysql> SELECT EMPLOYEE.EmpID,DEPARTMENT.DeptName
           -> FROM DEPARTMENT
           -> RIGHT JOIN EMPLOYEE ON EMPLOYEE.DeptID = DEPARTMENT.DEPTID;
+-------+-----------+
| EmpID | DeptName  |
+-------+-----------+
|   100 | Finance   |
|   101 | NULL      |
|   102 | Marketing |
+-------+-----------+
---------------------------------------------------------------------------------------------------------------------------------------------------------        












































































# Some Specified rules for data in the table

"""NOT NULL""" - Won`t have a nulll value

"""Unique""" - All the values in the column are unique

"""Primary Key""" - uniquly idenitify each row in a table. Ex - mobile no,Roll no




