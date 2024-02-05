import assignment0.assignment0 as assignment0
import pytest
import urllib.error

def test_fetchincidents_output():
    url = "https://www.normanok.gov/sites/default/files/documents/2024-02/2024-02-01_daily_incident_summary.pdf"
    result = assignment0.fetchincidents(url)
    assert result.read()

def test_fetchincidents_invalid_url():
    url = "https://www.normanok.gov/sites/default/files/documents/2025-02/2024-02-01_daily_incident_summary.pdf"
    with pytest.raises(urllib.error.URLError):
        assignment0.fetchincidents(url)

