from helper import base_url
import requests

query = """
query contactBySlug($id: ID!) {
  tool(id: $id) {
    id
    contactEnabled
    contactButtonText
    contactFlow
    __typename
  }
}
"""
variables = {
  "id": "pypi-azure"
}


def test_contactBySlug():
    response = requests.post(base_url, json={"query": query, "variables": variables})
    assert response.status_code == 200 and len(response.json()['data']['tool']['id']) > 0
    return str(response.json()['data']['tool']['id'])
