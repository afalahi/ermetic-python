# We need to double curly brace to escape
def aws_accounts_query(after: str, first: int = 1000):
    query = f"""query {{
      AwsAccounts(after:{after}, first:{first}) {{
          nodes {{
              Id
              Name
              Status
              Issues
              ParentScopeId
              Audit
              CreationTime
          }}
          pageInfo {{
              hasNextPage
              endCursor
          }}
      }}
    }}"""
    return query
