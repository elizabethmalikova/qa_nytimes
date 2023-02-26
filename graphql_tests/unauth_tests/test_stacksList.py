from graphql_tests.helper import base_url
import requests
from test_contactBySlug import test_contactBySlug

query = """
query stacksList($id: ID!, $vcsOrgId: ID, $first: Int, $after: String, $queryVar: String) {
  company(id: $id) {
    id
    stacksList(vcsOrgId: $vcsOrgId, first: $first, after: $after, query: $queryVar) {
      count
      edges {
        node {
          websiteUrl
          id
          slug
          name
          path
          private
          repoStack
          services(withoutPackages: true) {
            id
            name
            imageUrl
            canonicalUrl
            layer {
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
      pageInfo {
        endCursor
        hasNextPage
        __typename
      }
      __typename
    }
    __typename
  }
}
"""
variables = {
  "id": "101231709572352041",
  "queryVar": "",
  "vcsOrgId": "all",
  "first": 9,
  "after": None
}


def test_userStacksUsing():
    response = requests.post(base_url, json={"query": query, "variables": variables})
    response.raise_for_status()
    assert response.json()['data']['company']['stacksList']['count'] > 0
