def aws_billable_resources(after:str, filters:str='null', first:int=1000):
    return f""" query {{
  AwsResources(after:{after}, filter:{{{filters}}}, first:{first}) {{
    totalCount
    nodes {{
      AccountId
    }}
    pageInfo {{
        hasNextPage
        endCursor
    }}
  }}
}}
  """
    