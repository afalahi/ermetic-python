def create_folder_query(parentId: str, name: str):
    return f""" mutation {{
    CreateFolder(input: {{
        ParentFolderId: {parentId}
        Name:{name}
    }}) {{
        Folder {{
            Name
            Id
            ParentScopeId
        }}
    }}
}}
  """
