import helper
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
    response = requests.post(helper.base_url, json={"query": query, "variables": variables})
    assert response.status_code == 200
    assert response.json()['data']['currentPrivateCompany'] is None
