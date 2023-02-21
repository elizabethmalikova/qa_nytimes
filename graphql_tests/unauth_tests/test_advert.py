from graphql_tests.helper import base_url
import requests

query = """
query advert($placement: String, $objectType: String, $objectId: String) {
  advert(placement: $placement, objectType: $objectType, objectId: $objectId) {
    ctaText
    imageUrl
    sponsorFeatured
    sponsorToolId
    targetUrl
    text
    title
    bannerAdUrl
    mobileAdUrl
    sidebarAdUrl
    __typename
  }
}
"""
variables = {
  "placement": "featured-banner"
}


def test_advert():
    response = requests.post(base_url, json={"query": query, "variables": variables})
    assert response.status_code == 200 and response.json()['data']['advert']['sponsorFeatured'] is True
