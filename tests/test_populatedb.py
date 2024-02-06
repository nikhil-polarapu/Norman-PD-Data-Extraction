import assignment0.assignment0 as assignment0
import pytest
import os
import sqlite3

# Testcase to check if a single row is populated correctly
def test_populatedb_check_data():
    db = assignment0.createdb()
    incidents = [["2/1/2024 13:15", "2024-00007421", "1776 E ROBINSON ST", "Sick Person", "OK0140200"]]
    assignment0.populatedb(db, incidents)
    database_path = os.path.join('resources', 'normanpd.db')
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()
    cursor.execute('SELECT nature FROM incidents')
    for row in cursor.fetchall():
        nature = row[0]
        assert nature == incidents[0][3]
    connection.commit()
    connection.close()

# Testcase to check if multiple rows are populated correctly
def test_populate_db_multiple_rows():
    db = assignment0.createdb()
    incidents = [["2/1/2024 13:15", "2024-00007421", "1776 E ROBINSON ST", "Sick Person", "OK0140200"], ["2/1/2024 13:03", "2024-00001839", "2000 W BROOKS ST", "Falls", "14005"]]
    assignment0.populatedb(db, incidents)
    database_path = os.path.join('resources', 'normanpd.db')
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()
    cursor.execute('SELECT nature FROM incidents')
    nature = []
    for row in cursor.fetchall():
        i = 0
        nature.append(row[0])
    for i in range(len(nature)):
        assert nature[i] == incidents[i][3]
    connection.commit()
    connection.close()