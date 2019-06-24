# Gilbert Anthony Bernal MSDS-692 Data Science Project

## Overview
The data science project that was worked on for the Regis MSDS 692 practicum is titled "Establishment of Regis Healthcare Informatics Database". The goal of this project was to build a database for the Regis School of Health Informatics. The type of data that the school of health informatics uses is health data from various health organizations. These organizations provide data in various formats such as CSV, JSON, EXCEL, and more. The data format that is most commonly used by these organizations. Using PostgreSQL as the database management system and Python as a tool to upload the CSV files. A method was created in order to create a unique table based off a CSV file stored a directory in the PostgreSQL database, and upload the data in the CSV to the unique table created. An analysis on the effects of rainfall has on West Nile virus in California was done to provide an example of how this database and python code could be used. 

## Database Requirments & Goal
After talking to Dr. Judit Olah about the database needed for the program there were no clear requements. It was clear however that many indivudals could use this database for a variety of data from different sources that might not be used by anyone else but the person uploading it. This made the goal for the project to create a method to create a table based for each of the CSV files in a directory based its headers and then upload the data from the CSV file to its table. After that the files CSV files would have to be moved to an archive folder to make sure that the table does not get created more than once. 

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

