# Gilbert Anthony Bernal MSDS-692 Data Science Project

## Overview
The data science project that was worked on for the Regis MSDS 692 practicum is titled "Establishment of Regis Healthcare Informatics Database". The goal of this project was to build a database for the Regis School of Health Informatics. The type of data that the school of health informatics uses is health data from various health organizations. These organizations provide data in various formats such as CSV, JSON, EXCEL, and more. The data format that is most commonly used by these organizations. Using PostgreSQL as the database management system and Python as a tool to upload the CSV files. A method was created in order to create a unique table based off a CSV file stored a directory in the PostgreSQL database, and upload the data in the CSV to the unique table created. An analysis on the effects of rainfall has on West Nile virus in California was done to provide an example of how this database and python code could be used. 

## Database Requirments & Goal
After talking to Dr. Judit Olah about the database needed for the program there were no clear requements. It was clear however that many indivudals could use this database for a variety of data from different sources that might not be used by anyone else but the person uploading it. This made the goal for the project to create a simple method for any one to use or update that would create a table based for each of the CSV files in a directory based its headers and then upload the data from the CSV file to its table. After that the files CSV files would have to be moved to an archive folder to make sure that the table does not get created more than once. 

## Tools

### PostGres
PostgreSQL is a open source object-relational database system that uses the standard SQL language and extends the language with various features. The reasons why Postgres was chosen for this project over other database management systems was first the fact that Postgre was free and opensource. This means that there was absolutely no money needed in order to install and start using the database management system. The second reason was because Postgres works with a variety of data types. Examples of data types that Postgre works with are JSON, CSV, and XML. Making sure that the database chosen works well with various formats is important because the data the Health Informatics school will be using can vary based on the health organization they are getting their data from. The next reason is because Postgre works with various coding languages such as Python. Python has various libraries that can be used with PostgreSQL or manipulate data if needed before uploading the CSV data to the database. The last reason why PostgreSQL was chosen over other database is because it has a simple built in method COPY that allows users to upload CSV, JSON, and XML data files into its tables quickly.

### Python
Python is an open source high level programming language. The reason why Python was chosen for this project is that it has various libraries that work well with PostgreSQL and has other libraries that could help with the goals of the project.
### Python Libraries Used
Below are the Python libraries used for this project

**CSV:**
The CSV Library is used to allow python to work with CSV files. The reason why it was used in this code was simply to import any csv file needed. 

**AST:**
AST stands for abstract syntax trees and is a python library that is used to find out programmatically what the current grammar looks like. This package was used to look at the fields in the CSV file and identify the datatype that is stored in them. This helps with creating a CREATE TABLE PostgreSQL statement. The reason why this library is important is because if the CREATE TABLE statement does not have the correct data types for the column then the data cannot be uploaded. 

**PSYCOPG2:**
This library is the most popular PostgreSQL adaptor for Python. This package allows python to use PostgreSQL commands. The package was needed for the code in this project in order to create the table in the database for CSV files and to use the PostgreSQL COPY command to upload the data from the CSV files to their unique tables. 

**OS:**
The OS library is used to allow operating system functionality in python. This library is used to see all CSV files within a directory and begin running the created to create a table for these files and upload them to their unique table. 

**SHUTIL**
This library offers a number of high level operations for manipulating files. It can provide a way to copy, move, or remove files. This library was used to create a way to move CSV files from its main folder used for the python code to an archive folder so that multiple tables will not be created. 

#Part 1: Create the database
Creating the database was the first step that had to be completed for the project. The reason is because a database was needed in order to test the CSV table creation and upload methods. Since no money was provided for this project open source database management systems were examined. After examining different open source databases, the one chosen was PostgreSQL. The reason why this one was chosen over other open source databases was because it uses the standard SQL language and has a command called COPY that can be used to upload CSV files directly into tables. Making sure that the database used the standard SQL language was important because many users know this language already. This makes it easy for users to work with the data that is being uploaded and understand the code used in python. The ability to upload CSV is important since these are the types of files used by many health care organizations. 

**Step 1: Download PostgreSQL**
![](Images/Postgre_Download.PNG)

**Step 2: Follow Install Directions and Start Database**
![](Images/Postgre_Server.PNG)

# Part 2: Create Python Code
Three Python codes were created for this project. These codes were Info.py, Import_Function.py and Import_CSV.py.

**Info.py:** This code is used to store login credentials of the PostgreSQL admin account as variables for any Python code using PostgreSQL to use. This user must be an admin so that it can use any of the database table commands with no issue.

![](Images/Info.PNG)

**Import_Function.py:** This code stores a function that is used to take any CSV file and create a table based on the headers and values stored in the CSV. After the CREATE TABLE statement is created the code then uses the variables in the Info.py file to connect to the PostgreSQL database and run the CREATE TABLE statement in order to create the unique table for the CSV. After that another connection is made and the COPY command is used to upload the data from the CSV used to create the table into it. 

![](Images/Import_Function1.PNG)

![](Images/Import_Function2.PNG)

**Import_CSV.py:** This code is used to obtain the paths of the directory where the CSV files are stored and the archive directory that we want our files to move to after running the Import_function.py. After obtaining the paths the code then creates a function that will go through each of the files within a certain directory. After this a loop is used to go through all of the files in the directory and run the function created in the Import_Function.py to create the table and upload the data for every CSV file in the directory. After that the file is then moved to the archive folder to make sure that the table is not created again. 

![](Images/Import_CSV.PNG)

