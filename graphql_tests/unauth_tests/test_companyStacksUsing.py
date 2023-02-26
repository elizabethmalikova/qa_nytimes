from graphql_tests.helper import base_url
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


def test_companyStacksUsing():
    tool_id = test_contactBySlug()
    variables = {
        "id": tool_id,
        "first": 9
    }
    response = requests.post(base_url, json={"query": query, "variables": variables})
    data = response.json()['data']
    response.raise_for_status()
    assert data['tool']['companyStacksUsing']['count'] > 0
    company_id = str(data['tool']['companyStacksUsing']['edges'][0]['node']['id'])
    return company_id
