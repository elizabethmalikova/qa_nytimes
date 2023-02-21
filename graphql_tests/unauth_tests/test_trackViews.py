from graphql_tests.helper import base_url
import requests

query = """
mutation trackViews($decisionIds: [ID!]!, $clientContext: String) {
  trackViews(decisionIds: $decisionIds, clientContext: $clientContext)
}
"""
variables = {
  "clientContext": "StackAdvice-/stackups/angularjs-vs-backbone-vs-knockout",
  "decisionIds": [
    "104046417712610986",
    "104070793281526402",
    "104093267031982177",
    "104055431108877531"
  ]
}


def test_trackViews():
    response = requests.post(base_url, json={"query": query, "variables": variables})
    assert response.status_code == 200 and response.json()['data']['trackViews'] is True
