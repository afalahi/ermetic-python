def update_folder_query(folder_id: str, name: str):
    return f""" mutation {{
    UpdateFolder (input:{{
        Id:{folder_id},
        Name:{name}
    }}) {{
        Folder {{
            Name
            Id
        }}
    }}
}}
  """
