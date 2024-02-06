import assignment0.assignment0 as assignment0
import pytest

# Testcase to check if empty nature count is displayed
def test_status_empty_nature():
    db = assignment0.createdb()
    incidents = [["2/1/2024 13:15", "2024-00007421", "1776 E ROBINSON ST", "", "OK0140200"]]
    assignment0.populatedb(db, incidents)
    result = assignment0.status(db)
    assert result[0][0] == '' and result[0][1] == 1

# Testcase to check if multiple nature count is displayed 
def test_status_count():
    db = assignment0.createdb()
    incidents = [["2/1/2024 13:15", "2024-00007421", "1776 E ROBINSON ST", "Falls", "OK0140200"], ["2/1/2024 13:03", "2024-00001839", "2000 W BROOKS ST", "Falls", "14005"]]
    assignment0.populatedb(db, incidents)
    result = assignment0.status(db)
    assert result[0][0] == 'Falls' and result[0][1] == 2
