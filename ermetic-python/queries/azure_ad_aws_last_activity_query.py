def azure_ad_aws_last_activity_query(after:str, filters:str='null', first:int=1000):
    return f""" query {{
  AzureAdUsers(after:{after},filter:{filters},first:{first})
  {{
    nodes {{
      UserPrincipalName,
      Name,
      AccountId,
      AwsAssumableRoles {{
        Role {{
          Id,
          Name,
          LastActivityTime
        }}
      }}
    }}
    pageInfo {{
      hasNextPage
      endCursor
    }}
  }}
}}
  """
    