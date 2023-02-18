import helper
import requests

query = """
query user {
  me {
    impersonated
    hasPersonalGithubInstall
    privateCompanyMember
    selfServeEnabled
    privateMode
    showTosModal
    id
    path
    imageUrl
    amIAdmin
    title
    displayName
    companyName
    canIModerate
    username
    location
    shouldForceVcsConnection
    stripePortalUrl
    selfServeChecklist {
      completed
      dismissed
      items {
        slug
        completed
        __typename
      }
      __typename
    }
    stackApiTrialSubscription {
      plan {
        slug
        __typename
      }
      currentPeriodEndsAt
      active
      __typename
    }
    stackApiCurrentSubscription {
      couponPercentOff
      plan {
        slug
        __typename
      }
      currentPeriodEndsAt
      active
      __typename
    }
    stackApiKey {
      apiKey
      usageLimit
      currentPeriod {
        usageCount
        periodEndsAt
        __typename
      }
      __typename
    }
    jobSearch {
      companies {
        name
        imageUrl
        slug
        __typename
      }
      tools {
        name
        imageUrl
        __typename
      }
      keywords
      location
      latitude
      longitude
      emailEnabled
      __typename
    }
    bookmarkedJobs {
      count
      edges {
        node {
          bookmarked
          id
          angellistJobUrl
          title
          location
          tools {
            id
            imageUrl
            name
            __typename
          }
          company {
            imageUrl
            name
            path
            __typename
          }
          __typename
        }
        __typename
      }
      __typename
    }
    followedCompanies {
      count
      edges {
        node {
          id
          name
          thumbUrl
          imageUrl
          path
          __typename
        }
        __typename
      }
      __typename
    }
    stacks {
      edges {
        node {
          ...stackFields
          __typename
        }
        __typename
      }
      __typename
    }
    companies {
      id
      slug
      name
      imageUrl
      myRole
      privateMode
      stacksList(first: 10) {
        edges {
          node {
            ...stackFields
            __typename
          }
          __typename
        }
        __typename
      }
      plans {
        id
        slug
        __typename
      }
      __typename
    }
    decisionPrompt {
      id
      active
      message
      promptType
      selectedTool {
        id
        name
        imageUrl
        __typename
      }
      __typename
    }
    emailSettings {
      emailFeedDaily
      emailFeedWeekly
      __typename
    }
    plans {
      slug
      __typename
    }
    __typename
  }
}

fragment stackFields on Stack {
  id
  imageUrl
  name
  identifier
  path
  private
  owner {
    ... on User {
      id
      imageUrl
      username
      __typename
    }
    ... on Company {
      id
      imageUrl
      slug
      name
      __typename
    }
    __typename
  }
  __typename
}
"""
variables = {}


def test_User():
    response = requests.post(helper.base_url, json={"query": query, "variables": variables})
    assert response.status_code == 200
    assert response.json()['data']['me'] is None
