def okta_users_query(current_cursor: str):
    return f""" query {{
    OktaUsers(after:{current_cursor} first:1000) {{
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
