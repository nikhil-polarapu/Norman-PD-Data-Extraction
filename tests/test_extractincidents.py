import assignment0.assignment0 as assignment0
import pytest

# Testcase to check if page heading is excluded in the output
def test_extractincidents_heading():
    url = "https://www.normanok.gov/sites/default/files/documents/2024-02/2024-02-01_daily_incident_summary.pdf"
    data = assignment0.fetchincidents(url)
    result = assignment0.extractincidents(data)
    string = "NORMAN POLICE DEPARTMENT"
    for row in result:
        assert string not in row

# Testcase to check if table headers are excluded in the output
def test_extractincidents_table_header():
    url = "https://www.normanok.gov/sites/default/files/documents/2024-02/2024-02-01_daily_incident_summary.pdf"
    data = assignment0.fetchincidents(url)
    result = assignment0.extractincidents(data)
    string = "Date / Time Incident Number Location Nature Incident ORI"
    for row in result:
        assert string not in row

# Testcase to check if empty nature values are not removed from the data
def test_extractincidents_empty_nature():
    url = "https://www.normanok.gov/sites/default/files/documents/2024-02/2024-02-01_daily_incident_summary.pdf"
    data = assignment0.fetchincidents(url)
    result = assignment0.extractincidents(data)
    val = ["2/1/2024 13:15", "2024-00007421", "", "", "OK0140200"]
    assert val in result