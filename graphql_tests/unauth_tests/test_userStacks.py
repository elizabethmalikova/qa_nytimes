from graphql_tests.helper import base_url
import requests

query = """
query userStacks {
  me {
    id
    impersonated
    stacks(first: 25) {
      edges {
        node {
          id
          slug
          name
          services {
            id
            slug
            __typename
          }
          __typename
        }
        __typename
      }
      __typename
    }
    companies {
      id
      name
      stacksList(first: 10) {
        pageInfo {
          endCursor
          __typename
        }
        edges {
          node {
            id
            name
            slug
            tools {
              id
              slug
              __typename
            }
            __typename
          }
          __typename
        }
        __typename
      }
      __typename
    }
    __typename
  }
}
"""
variables = {}


def test_userStacks():
    response = requests.post(base_url, json={"query": query, "variables": variables})
    response.raise_for_status()
    assert response.json()['data']['me'] is None
