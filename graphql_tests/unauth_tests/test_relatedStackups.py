from graphql_tests.helper import base_url
import requests
from test_contactBySlug import test_contactBySlug

query = """
query relatedStackups($id: ID!, $after: String) {
  tool(id: $id) {
    relatedStackups(first: 6, after: $after) {
      edges {
        node {
          id
          path
          services {
            id
            name
            imageUrl
            thumbUrl
            __typename
          }
          __typename
        }
        __typename
      }
      __typename
    }
    id
    __typename
  }
}
"""


def test_relatedStackups():
    tool_id = test_contactBySlug()
    variables = {
        "id": tool_id
    }
    response = requests.post(base_url, json={"query": query, "variables": variables})
    data = response.json()['data']
    response.raise_for_status()
    assert len(data['tool']['relatedStackups']['edges'][0]['node']['id']) > 0
