# We need to double curly brace to escape
def aws_accounts_query(current_cursor):
    query = f"""query {{
      AwsAccounts(after:{current_cursor} first:1000) {{
          nodes {{
              Id
              Name
              Status
              Issues
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
