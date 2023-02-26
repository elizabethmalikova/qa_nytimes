from graphql_tests.helper import base_url
import requests

query = """
query organizationsQuery($first: Int, $after: String, $query: String, $slug: String) {
  currentPrivateCompany {
    id
    totalVcsOrgsCount
    vcsOrgs(first: $first, after: $after, searchQuery: $query, selectedSlug: $slug) {
      count
      edges {
        node {
          id
          name
          slug
          imageUrl
          vcsProvider
          orgUrl
          __typename
        }
        __typename
      }
      pageInfo {
        hasNextPage
        endCursor
        __typename
      }
      __typename
    }
    __typename
  }
}
"""
variables = {
  "query": "",
  "first": 10,
  "slug": None
}


def test_organizationsQuery():
    response = requests.post(base_url, json={"query": query, "variables": variables})
    response.raise_for_status()
    assert response.json()['data']['currentPrivateCompany'] is None
