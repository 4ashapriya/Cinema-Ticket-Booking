import pytest
import requests


url_server = "http://localhost:8000/"

# Test code for get_tickets API
@pytest.mark.get_tickets
def test_get_tickets():
    url_ticket = url_server + "get_tickets"
    response = requests.post(url_ticket)
    print(f"test_GetTickets => {response}")
    assert response.status_code == 200


test_get_tickets()
