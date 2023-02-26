from graphql_tests.helper import base_url
import requests
from test_contactBySlug import test_contactBySlug

query = """
query toolDecisions($id: ID!, $after: String) {
  tool(id: $id) {
    stackDecisions(first: 6, after: $after) {
      count
      pageInfo {
        hasNextPage
        endCursor
        __typename
      }
      edges {
        node {
          user {
            id
            username
            title
            companyName
            imageUrl
            thumbUrl
            displayName
            __typename
          }
          company {
            imageUrl
            thumbUrl
            name
            path
            features {
              slug
              __typename
            }
            __typename
          }
          link {
            url
            title
            __typename
          }
          publicId
          id
          htmlContent
          viewCount
          publishedAt
          upvotesCount
          services {
            name
            path
            id
            imageUrl
            thumbUrl
            stacks
            fans
            votes
            following
            __typename
          }
          topics {
            name
            id
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


def test_toolDecisions():
    tool_id = test_contactBySlug()
    variables = {
        "id": tool_id
    }
    response = requests.post(base_url, json={"query": query, "variables": variables})
    data = response.json()['data']
    response.raise_for_status()
    assert data['tool']['stackDecisions']['count'] > 0
    list_users_id = []
    for i in range(5):
        list_users_id.append(data['tool']['stackDecisions']['edges'][i]['node']['user']['id'])
    return list_users_id

