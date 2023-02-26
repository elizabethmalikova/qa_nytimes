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
    data = response.json().get('data', {})
    response.raise_for_status()
    assert data.get('onboardingChecklist') is None
