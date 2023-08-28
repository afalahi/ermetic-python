def aws_ec2_resources(after:str, filters:str='null', first:int=1000):
    return f""" query {{
  AwsResources(
    after:{after},
    filter: {{
        Types: [AwsEc2Instance]
    }},
    first:{first}
    first:10) {{
    nodes {{
      Name
      Id
    ...on AwsEc2Instance {{
        State
        MetadataServiceV1UsageTime
        MetadataServiceVersion
    }}
    }}
  }}
}}
  """
    