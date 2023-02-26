from graphql_tests.helper import base_url
import requests

query = """
query tool($id: ID!) {
  tool(id: $id) {
    id
    private
    imageUrl
    thumbUrl
    thumbRetinaUrl
    name
    pressUrl
    contactFlow
    legacyThirdPartyId
    jobsCount
    type
    keywords
    packageUrl
    packageManager {
      slug
      miniImageUrl
      websiteUrl
      packageManagerTools {
        imageUrl
        thumbUrl
        thumbRetinaUrl
        name
        id
        slug
        path
        __typename
      }
      __typename
    }
    featuredPosts {
      any
      __typename
    }
    alternativeTools(first: 5) {
      edges {
        node {
          id
          name
          description
          __typename
        }
        __typename
      }
      __typename
    }
    followers {
      count
      __typename
    }
    privateStacks {
      any
      __typename
    }
    privateUsersUsingViaPersonalStacks {
      any
      __typename
    }
    privateUsersViaContributedStacks {
      any
      __typename
    }
    teams {
      any
      __typename
    }
    privateFollowers {
      count
      __typename
    }
    company {
      name
      amIOwner
      slug
      path
      stacks {
        id
        __typename
      }
      owners {
        amIAdmin
        canIModerate
        id
        __typename
      }
      __typename
    }
    pros {
      pageInfo {
        hasNextPage
        endCursor
        __typename
      }
      edges {
        node {
          ...reasonFields
          __typename
        }
        __typename
      }
      __typename
    }
    slug
    path
    verified
    title
    twitterUsername
    websiteUrl
    followingTool
    githubStarsCount
    githubForksCount
    githubUpdatedAt
    hackernewsOnlineMentionsCount
    redditOnlineMentionsCount
    stackOverflowOnlineMentionsCount
    description
    ampStoryEnabled
    stacks
    votes
    jobs
    function {
      name
      slug
      __typename
    }
    layer {
      name
      slug
      __typename
    }
    category {
      name
      slug
      __typename
    }
    allToolIntegrations {
      any
      __typename
    }
    companyStacksUsing {
      any
      __typename
    }
    userStacksUsing {
      any
      __typename
    }
    features
    footerAlternateTools(first: 5) {
      edges {
        node {
          name
          path
          __typename
        }
        __typename
      }
      __typename
    }
    footerNewTools(first: 5) {
      edges {
        node {
          name
          path
          __typename
        }
        __typename
      }
      __typename
    }
    footerTopTools(first: 5) {
      edges {
        node {
          name
          path
          __typename
        }
        __typename
      }
      __typename
    }
    footerRelatedStackups(first: 5) {
      edges {
        node {
          path
          title
          __typename
        }
        __typename
      }
      __typename
    }
    toolType
    adoptionStageContext
    adoptionStage {
      id
      name
      slug
      __typename
    }
    versionRules {
      any
      __typename
    }
    __typename
  }
}

fragment reasonFields on Reason {
  id
  upvoted
  upvotesCount
  text
  __typename
}
"""
variables = {
  "id": "pypi-azure"
}


def test_userStacks():
    response = requests.post(base_url, json={"query": query, "variables": variables})
    response.raise_for_status()
    return response.json()['data']['tool']['websiteUrl'] == "https://github.com/Azure/azure-sdk-for-python"
