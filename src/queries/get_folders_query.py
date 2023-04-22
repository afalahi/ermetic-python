def get_folders_query(current_cursor):
    return f""" query {{
    Folders(after:{current_cursor}) {{
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
    