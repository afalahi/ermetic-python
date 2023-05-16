def azure_resources_query(after: str, filters: str, first: int = 1000):
    return f""" query {{
    AzureResources(filter:{filters}, first:{first}, after:{after}) {{
        nodes {{
            Id
            Name
        }}
        pageInfo {{
            hasNextPage
            endCursor
        }}
    }}
}}
  """
