import assignment0.assignment0 as assignment0
import pytest
import os

# Testcase to check if the database file is created
def test_createdb_check_file():
    assignment0.createdb()
    assert os.path.isfile("resources/normanpd.db")
    incidents = [""]
