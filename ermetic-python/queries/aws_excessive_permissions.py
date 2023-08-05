def aws_excessive_permissions(after:str, filters:str='null', first:int=1000):
    return f""" query {{
    Findings(filter:{{{filters}}}, first:{first}, after:{after}) {{
        totalCount
        nodes{{
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
    