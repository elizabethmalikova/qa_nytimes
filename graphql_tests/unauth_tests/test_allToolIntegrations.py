from graphql_tests.helper import base_url
import requests
from test_contactBySlug import test_contactBySlug

query = """
query allToolIntegrations($id: ID!, $after: String, $first: Int) {
  tool(id: $id) {
    allToolIntegrations(first: $first, after: $after) {
      count
      pageInfo {
        hasNextPage
        endCursor
        __typename
      }
      edges {
        node {
          imageUrl
          thumbUrl
          thumbRetinaUrl
          name
          id
          slug
          path
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


def test_allToolIntegrations():
    tool_id = test_contactBySlug()
    variables = {
        "first": 9,
        "id": tool_id
    }
    response = requests.post(base_url, json={"query": query, "variables": variables})
    data = response.json()['data']
    response.raise_for_status()
    assert data['tool']['allToolIntegrations']['count'] > 0
