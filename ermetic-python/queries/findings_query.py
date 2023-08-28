def findings_query(after: str, filters: str = 'null', first: int = 1000):
    return f""" query {{
    Findings({filters}, first:{first}, after:{after}) {{
        nodes{{
            CreationTime
            CloudProvider
            Title
            AccountId
            __typename
        }} 
        pageInfo {{
            hasNextPage
            endCursor
        }}
    }}
}}
  """
