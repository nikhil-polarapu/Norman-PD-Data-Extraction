# cis6930sp24 -- Assignment0

Name: Nikhil Polarapu
UFID: 16049519
Email: spolarapu@ufl.edu

# Assignment Description

In this assignment we write a program that goes through the pdf file of Norman Police Department that has the incidents, arrests and other activities. The program reads the tabular data, cleans it and converts it into a list-of-lists, each list representing a row of the table. Using this data we create an sqlite database with a table called incidents that has the following columns.

- Date/Time
- Incident Number
- Location
- Nature
- Incident ORI

We populate this table with the data extracted from the page. The final aim of the assignment is to print the nature and its count across the table, in the "nature|count" format.

# How to install

pipenv install

## How to run

pipenv run ...
![video](video)


## Functions

#### main.py \

main() - This function takes in the URL mentioned in the command line as argument and runs the functions in assignment0.py to get the desired output. 

#### assignment0.py \

fetchincidents() - This function takes the URL as parameter, extracts the data in the page and returns this data in the byte form.

extractincidents() - This function takes in the result of the fetchincidents() function as the parameter, extracts the incident data present in the table and returns it as a list-of-lists.

createdb() - This function executes an SQL query that checks if a table called incidents exists in the normanpd.db database, deletes it if it already exists and creates a new one by executing a different query. This function does not take any parameters and does not return anything.

populatedb() - This function takes in the database created in createdb() function and the list-of-lists returned by extractincidents() function as parameters. It executes an SQL query that connects to the normanpd.db database, inserts the list-of-lists data (each list as a row) into the incidents table. This function does not return anything.

status() - This function takes in the database created in createdb() function. It executes an SQL query that goes through the table, selects the nature & its count and prints these values in the "nature|count" format. This function does not return anything.

## Database Development
...

## Bugs and Assumptions
...

## Testcase Discussion


