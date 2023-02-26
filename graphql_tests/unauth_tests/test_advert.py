from graphql_tests.helper import base_url
import requests

query = f"""
query advert($placement: String) {{
  advert(placement: $placement) {{
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
  }}
}}
"""

variables = {
    "placement": "featured-banner"
}


def test_advert():
    response = requests.post(base_url, json={"query": query, "variables": variables})
    response.raise_for_status()
    data = response.json()['data']['advert']
    assert data['sponsorFeatured'] is True
