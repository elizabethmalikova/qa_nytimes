from graphql_tests.helper import base_url
import requests
from test_toolDecisions import test_toolDecisions

query = """
mutation trackViews($decisionIds: [ID!]!, $clientContext: String) {
  trackViews(decisionIds: $decisionIds, clientContext: $clientContext)
}
"""


def test_trackViews():
    users_id = test_toolDecisions()
    variables = {
        "clientContext": "Reasons-/" + "react",
        "decisionIds": users_id
    }
    response = requests.post(base_url, json={"query": query, "variables": variables})
    response.raise_for_status()
    assert response.json()['data']['trackViews'] is True
    print(response.json())
