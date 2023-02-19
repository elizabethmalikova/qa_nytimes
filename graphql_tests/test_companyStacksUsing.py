from helper import base_url
import requests
from test_contactBySlug import test_contactBySlug

query = """
query companyStacksUsing($id: ID!, $after: String, $first: Int) {
  tool(id: $id) {
    companyStacksUsing(first: $first, after: $after) {
      count
      pageInfo {
        hasNextPage
        endCursor
        __typename
      }
      edges {
        node {
          name
          imageUrl
          thumbUrl
          thumbRetinaUrl
          identifier
          id
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
variables = {
    "id": test_contactBySlug(),
    "first": 9
}


def test_companyStacksUsing():
    response = requests.post(base_url, json={"query": query, "variables": variables})
    assert response.status_code == 200 and response.json()['data']['tool']['companyStacksUsing']['count'] > 0
