def findings_by_resource_group_query(after: str, filters: str, first: int = 1000):
    return f""" query {{
    Findings(filter:{filters}, first:{first}, after:{after}) {{
        nodes {{
            Title
            Status
            Severity
            Category
            Labels
            Resources {{
                Id
                Name
            }}
            Remediation {{
                Console {{
                    Steps
                }}
            }}

        }} pageInfo {{
            hasNextPage
            endCursor
        }}
    }}
}}
  """
