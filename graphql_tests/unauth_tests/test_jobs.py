from graphql_tests.helper import base_url
import requests
from test_contactBySlug import test_contactBySlug

query = """
query jobs($id: ID!, $first: Int) {
  tool(id: $id) {
    jobsList(first: $first) {
      count
      edges {
        node {
          id
          angellistJobUrl
          title
          location
          services {
            ...serviceFields
            __typename
          }
          company {
            name
            imageUrl
            path
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
    id
    __typename
  }
}

fragment serviceFields on Tool {
  id
  name
  slug
  title
  verified
  imageUrl
  canonicalUrl
  path
  votes
  fans
  stacks
  following
  followContext
  __typename
}
"""


def test_jobs():
    tool_id = test_contactBySlug()
    variables = {
        "first": 6,
        "id": tool_id
    }
    response = requests.post(base_url, json={"query": query, "variables": variables})
    data = response.json()['data']
    response.raise_for_status()
    assert data['tool']['jobsList']['count'] > 0
