def get_folders_query(after: str, first: int = 1000):
    return f""" query {{
    Folders(after:{after}, first:{first}) {{
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
