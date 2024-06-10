1 - MySQL --version : - For check the version of MySQL database

2 - MySQL -u root -p : - ask for password

3 -  show databases - for showing the database created
3.1 -use database  - for use a particular database 


4 - create database -
    CREATE DATABASE db_name;

4.2 - delete database -
      DROP DATABASE db_name;


5 - for creating a Table -
    CREATE TABLE table_name(
    Column 1 Datatypeofcolmn,
    Column 2 Datatypeofcolmn,
    Column 3 Datatypeofcolmn,
    Column 4 Datatypeofcolmn,

5.2 - for deleting a table -
    DROP TABLE tb_name;


6 - for describe a table -
    DESC table_name;
    

7 - inserting values in a table -
    mysql>  INSERT INTO table_name (nameofcol1,nameofcol2,nameofcol3,nameofcol4,nameofcol5) VALUES (valofcol1,'valofcol2',valofcol3,valofcol4,valofcol5);
    # in case when value of the column is in varchar then it will be in 'string'


8 - # Selecting from Table -
    SELECT * FROM table_name
    

8.2 - for select a particulr column from the table.
    mysql> SELECT col_name FROM table_name;


9 - NOT NULL CONSTRAINT -
    -> Col_name Data_type NOT NULL,


10 - Unique Constraint -
    -> UNIQUE(colm_name)


11 - Primary Key Constraints -
    ->   PRIMARY KEY(colm_name)


12 - CHECK Constraint -
    CHECK(colm_name Ccondition Limit)


13 - DEFAULT Constraint -
    colm_name data_type DEFAULT 'VALUEOFDEfAULT'


14 - Index Constraint -

14.1 - Creating Index -
    
    CREATE INDEX name_ofindex
    ON table_name(column_name);

14.2 - Deleting Index

    DROP INDEX name_ofindex
    ON table_name;
    
14.3 - for showing index constraint -
    mysql> SHOW INDEXES FROM table_name;



15 - Adding a Column in a table -
    
 Syntaxc - ALTER TABLE table_name    
           ADD colm_name data_type;


15.2 - deLeTInG A cOLM in a existing table-

 Syntaxc - ALTER TABLE table_name
          DROP COLUMN colm_name_toremove;


16 - Alter a Table Modify a Column
    
        mysql>  ALTER TABLE EMPLOYEE
        -> MODIFY COLUMN EmpZONE int;
    

17 - SELECT DISTINCT STATEMENT in mysql -
    
    mysql> SELECT DISTINCT Com_name_where_duplicate_value_remove FROM table_name;

    
    

18 - #For display whole table -
    SELECT * FROM tbale_name;

    #For display from a specific column
    SELECT colm_name FROM table_name;

    #For display from more than one specific column
    SELECT colm1_name,colm2_name, colm3_name FROM table_name;


19 - Where Clause in mysql

   Syntax - SELECT * FROM table_name
            WHERE colm_name Symbol Conndition;
    
    mysql> SELECT * FROM EMPLOYEE
    -> WHERE EmpAGE=25;


19.1 - And Clause -
    WHERE EmpAGE=25 AND EmpZONE='NorthIndian' AND LastName='Sparrow';

19.2 - OR Clause -
    WHERE EmpZONE='SouthIndian' OR empZONE='WestIndian';

19.3 - NOT Clause -
    WHERE NOT EmpAGE=30;


20 - Single Line Comment can be using double dash (--) OR Hasg(#)
     Multi Line Comment can be using /* ...........*/


21 - Count Function Working -
     SELECT COUNT(colm_name_where_record_count) FROM table_name


22 - Alias Function (AS) -
    Syntax - SELECT com_name AS jo_naam_aap_dena_chaahe

22.1 - For Multiple Column Name Chnange -
    Syntax - SELECT com_name AS jo_naam_aap_dena_chaahe1, com_name AS jo_naam_aap_dena_chaahe2


23 - In & NOT In Operators

    Syntax In operator -
         SELECT * FROM EMPLOYEE
         WHERE colm_name IN('colm_record1_wants_to_put_in_IN','colm_record2_wants_to_put_in_IN')

    Syntax NOT In operator -
         SELECT * FROM EMPLOYEE
         WHERE colm_name NOT IN('colm_record1_NOT_wants_to_put_in_IN','colm_record2_NOT_wants_to_put_in_IN')


24 - Like Operator -

        Syntax - SELECT * FROM EMPLOYEE
        WHERE colm_name LIKE 'Startwith%';

        Syntax - SELECT * FROM EMPLOYEE
        WHERE colm_name LIKE '%endwith';
     

25 - Between & Not between Operator -

Syntax - mysql> SELECT * FROM table_name
        -> WHERE colm_name BETWEEN record1 AND record2;


Syntax - mysql> SELECT * FROM table_name
        -> WHERE colm_name NOT BETWEEN record1 AND record2;


26 - Case Statement in MySQL -

Syntax - SELECT col_name1,col_name2,col_name3
         CASE
         CONDITION FOR COLUMNS
         ENDS AS LAST_COLUMN
         FROM table_name

27 - Delete statement in MYSQL

For Delete Specific column's Record 
        sYNTAX - DELETE FROM EMPLOYEE
                 WHERE colm_name='record_which_delete';

For delete all records from table
         sYNTax - DELETE FROM table_name;
         For see delete or not - SELECT * FROM table_name;

28 - Update Statement in mysql -

     uPDATIOn of Single record -

Syntax - UPDATE table_name
        SET colm_name = new_data
        WHERE colm_name(idemtity)= where need to edit;


29 - Drop Table Statement in MYSQL -
     Syntax - DROP TABLE table_name;


30 - Drop Databse in mysql -

     Syntax - DROP DATABASE dab_name;


31 -  Avg() function in mysql

     Syntax - SELECT  AVG(colm_name)
                      FROM table_name;


32- Sum() Function in mysql -

     Syntax - SELECT SUM(colm_name_whoose_sum)
                 FROM table_name;   


33 - Order By Keywork in mysql -

     For """increasing/Ascending Order """ - 
    Syntax - SELECT * FROM table_name
             ORDER BY colm_name;

     For """decreasing/descending Order """ -         
        Syntax - SELECT * FROM table_name
                 ORDER BY colm_name DESC;


34 -  Auto Increment in Mysql-

     Synatx - CREATE TABLE table_name(
         colm1 int NOT NULL AUTO_INCREMENT,
         colm2 data_type,
         colm3 data_type,
         colm4 int,
         colm5 data_type,
         PRIMARY KEY(col1)
     );


35 -  Max() Function in Mysql-

     Synatx - SELECT MAX(colm_name_whoose_max)
         FROM table_name;


36 -  Min() Function in Mysql-

     Synatx - SELECT MIN(colm_name_whoose_max)
         FROM table_name;


37 - Limit Clause in mysql -

     sYNtax - SELECT * FROM table_name
         LIMIT No_as_require;

38 - Joins in Mysql -
     
    
    
























