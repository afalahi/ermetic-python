def users_assignments_query():
    return f""" query {{
    UserRoleAssignments {{
        UserId
        Role
        ScopeId
    }}
}}
  """
