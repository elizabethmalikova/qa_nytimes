from graphql_tests.helper import base_url
import requests
from test_contactBySlug import test_contactBySlug

query = """
query posts($id: ID!, $after: String, $first: Int) {
  tool(id: $id) {
    featuredPosts(first: $first, after: $after) {
      count
      pageInfo {
        hasNextPage
        endCursor
        __typename
      }
      edges {
        node {
          id
          views
          title
          imageUrl
          publishedAt
          canonicalUrl
          previewImageUrl
          company {
            name
            __typename
          }
          tools {
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
          favoriteStacksCount
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


def test_posts():
    tool_id = test_contactBySlug()
    variables = {
        "first": 9,
        "id": tool_id
    }
    response = requests.post(base_url, json={"query": query, "variables": variables})
    data = response.json()['data']
    response.raise_for_status()
    assert data['tool']['allToolIntegrations']['count'] > 0
