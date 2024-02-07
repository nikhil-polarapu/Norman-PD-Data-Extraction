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

- curl https://pyenv.run | bash
- pyenv install 3.11
- pyenv global 3.11
- pipenv install pypdf
- pipenv install pytest

## How to run

- pipenv run python assignment0/main.py --incidents https://www.normanok.gov/sites/default/files/documents/2024-02/2024-02-01_daily_incident_summary.pdf
- pipenv run python -m pytest

![DE Assignment0 Demo](/DE%20Assignment0.gif)


## Functions

#### main.py \

- main( ) - This function takes in the URL mentioned in the command line as argument and runs the functions in assignment0.py to get the desired output. 

#### assignment0.py \

- fetchincidents( ) - This function takes the URL as parameter, extracts the data in the page and returns this data in the byte form.

- extractincidents( ) - This function takes in the result of the fetchincidents( ) function as the parameter, extracts the incident data present in the table and returns it as a list-of-lists.

- createdb( ) - This function executes an SQL query that checks if a table called incidents exists in the normanpd.db database, deletes it if it already exists and creates a new one by executing a different query. This function does not take any parameters and does not return anything.

- populatedb( ) - This function takes in the database created in createdb( ) function and the list-of-lists returned by extractincidents( ) function as parameters. It executes an SQL query that connects to the normanpd.db database, inserts the list-of-lists data (each list as a row) into the incidents table. This function does not return anything.

- status( ) - This function takes in the database created in createdb( ) function. It executes an SQL query that goes through the table, selects the nature & its count and prints these values in the "nature|count" format. This function does not return anything.

## Database Development

- **Query to create the table**
  cursor.execute('CREATE TABLE  incidents (incident_time TEXT, incident_number TEXT, incident_location TEXT, nature TEXT, incident_ori TEXT)')

- **Query to insert data into the table**
  cursor.execute('INSERT INTO incidents (incident_time, incident_number, incident_location, nature, incident_ori) VALUES (?, ?, ?, ?, ?)', row)

- **Query to select nature and its count**
  cursor.execute('SELECT nature, COUNT(*) as count FROM incidents GROUP BY nature ORDER BY count DESC, CASE WHEN nature = '' THEN 1 ELSE 0 END, nature')

## Bugs and Assumptions

The following assumptions were made:
  
- There are always 5 columns in the table.
- There date/time and incident number columns are always non-empty.
- The column names and page heading are always the same and they never change.

If any page does not follow the above-mentioned assumptions then bugs related to these assumptions may be encountered.

## Testcase Discussion

- test_fetchincidents_output( ) - Testcase to check if data is fetched properly from the URL.
- test_fetchincidents_invalid_url( ) - Testcase to check if error occurs when wrong URL is given.
- test_extractincidents_heading( ) - Testcase to check if page heading is excluded in the output.
- test_extractincidents_table_header( ) - Testcase to check if table headers are excluded in the output.
- test_extractincidents_empty_nature( ) - Testcase to check if empty nature values are not removed from the data.
- test_createdb_check_file( ) - Testcase to check if the database file is created.
- test_populatedb_check_data( ) - Testcase to check if a single row is populated correctly.
- test_populate_db_multiple_rows( ) - Testcase to check if multiple rows are populated correctly.
- test_status_empty_nature( ) - Testcase to check if empty nature count is displayed.
- test_status_count( ) - Testcase to check if multiple nature count is displayed.
