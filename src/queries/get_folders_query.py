def get_folders_query(current_cursor):
    return f""" query {{
    Folders(after:{current_cursor}, first:1000) {{
        nodes {{
            Id
            ParentScopeId
            Name
        }}
        pageInfo {{
            endCursor
            hasNextPage
        }}
    }}
}}
  """
