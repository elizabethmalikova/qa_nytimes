import requests
from graphql_tests.helper import base_url

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
    "id": "React"
}


def test_contactBySlug():
    response = requests.post(base_url, json={"query": query, "variables": variables})

    response.raise_for_status()
    assert 'data' in response.json()
    assert 'tool' in response.json()['data']
    assert 'id' in response.json()['data']['tool']

    tool_id = str(response.json()['data']['tool']['id'])
    assert len(tool_id) > 0
    return tool_id
