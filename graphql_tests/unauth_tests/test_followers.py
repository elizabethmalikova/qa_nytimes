from graphql_tests.helper import base_url
import requests
from test_contactBySlug import test_contactBySlug

query = """
query followers($id: ID!, $after: String, $first: Int) {
  tool(id: $id) {
    followers(first: $first, after: $after) {
      count
      pageInfo {
        hasNextPage
        endCursor
        __typename
      }
      edges {
        node {
          id
          displayName
          username
          imageUrl
          title
          popularity
          path
          stacksCount
          favoritesCount
          votesCount
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


def test_followers():
    tool_id = test_contactBySlug()
    variables = {
        "first": 10,
        "id": tool_id
    }
    response = requests.post(base_url, json={"query": query, "variables": variables})
    data = response.json()['data']
    response.raise_for_status()
    assert data['tool']['followers']['count'] > 0
