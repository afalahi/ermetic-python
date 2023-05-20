def okta_users_query(after: str, filters: str = 'null', first: int = 1000):
    return f""" query {{
    OktaUsers(after:{after} filter:{filters},first:{first}) {{
        nodes {{
            Mail
            Status
            AwsLastActivity
            Groups {{
                Name
            }}
            AwsAssumableRoles {{
                Role {{
                    Name
                    AccountId
                }}
            }}
        }}
        pageInfo {{
            endCursor
            hasNextPage
        }}
    }}
}}
  """
