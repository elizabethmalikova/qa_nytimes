from graphql_tests.helper import base_url
import requests

query = """
{
  onboardingChecklist {
    completed
    dismissed
    items {
      slug
      completed
      __typename
    }
    __typename
  }
}
"""
variables = {}


def test_onboardingChecklist():
    response = requests.post(base_url, json={"query": query, "variables": variables})
    assert response.status_code == 200 and response.json()['data']['onboardingChecklist'] is None
