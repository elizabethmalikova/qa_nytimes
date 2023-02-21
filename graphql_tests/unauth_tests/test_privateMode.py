from graphql_tests.helper import base_url
import requests

query = """
query privateMode {
  currentPrivateCompany {
    id
    name
    myRole
    slug
    verified
    privateMode
    imageUrl
    restrictPublicStackshare
    showUneditedAutoDecisions
    permissions {
      edit
      __typename
    }
    adoptionStages {
      id
      slug
      name
      __typename
    }
    members {
      count
      __typename
    }
    emailAddress
    plans {
      slug
      __typename
    }
    features {
      slug
      __typename
    }
    forcedVcsProvider
    vcsOrgs {
      count
      __typename
    }
    __typename
  }
}
"""
variables = {}


def test_privateMode():
    response = requests.post(base_url, json={"query": query, "variables": variables})
    assert response.status_code == 200 and response.json()['data']['currentPrivateCompany'] is None