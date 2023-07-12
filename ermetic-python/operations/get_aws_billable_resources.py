# Copyright 2023 ali.falahi@ermetic.com
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from common import ermetic_request
from common import save_to_csv
from operations import get_aws_accounts
from operations.get_folders import get_folders
from queries import aws_billable_resources

def get_aws_billable_resources():
    
    def get_ermetic_aws_folder_path(folders, aws_folder_id):
      '''
      Builds AWS Account Folder path to help locating accounts
      '''
      for item in folders:
        if item['Id'] == aws_folder_id:
          parent_id = item['ParentScopeId']
          if parent_id is None:
            return item['Name']
          else:
            parent_path = get_ermetic_aws_folder_path(folders, parent_id)
            return f"{parent_path}/{item['Name']}"
      return None
    
    aws_accounts = get_aws_accounts()
    folders = get_folders()
    ec2_instances = ermetic_request(aws_billable_resources,filters='Types: AwsEc2Instance')
    ecs_services = ermetic_request(aws_billable_resources,filters='Types: AwsEcsService')
    eks_clusters = ermetic_request(aws_billable_resources,filters='Types: AwsEksCluster')
    dynamo_db_tables = ermetic_request(aws_billable_resources,filters='Types: AwsDynamoDbTable')
    elastic_search_domains = ermetic_request(aws_billable_resources,filters='Types: AwsElasticsearchDomain')
    lambda_functions = ermetic_request(aws_billable_resources,filters='Types: AwsLambdaFunctionConfiguration')
    rds_clusters = ermetic_request(aws_billable_resources,filters='Types: AwsRdsCluster')
    redshift_clusters = ermetic_request(aws_billable_resources,filters='Types: AwsRedshiftCluster')
    s3_buckets = ermetic_request(aws_billable_resources,filters='Types: AwsS3Bucket')

    normalized_lambdas = round(len(lambda_functions) / 10)
    billable_resources_report = []
    for account in aws_accounts:
      print(f"Currently calculating resources on Account {account['Id']}")
      obj = {
        "AccountName":account['Name'],
        "AccountId":account['Id'],
        "Folder": get_ermetic_aws_folder_path(folders=folders, aws_folder_id=account['ParentScopeId'])
      }
      ec2_instances = ermetic_request(aws_billable_resources,filters=f'Types: AwsEc2Instance, AccountIds: "{account["Id"]}"')
      ecs_services = ermetic_request(aws_billable_resources,filters=f'Types: AwsEcsService, AccountIds: "{account["Id"]}"')
      eks_clusters = ermetic_request(aws_billable_resources,filters=f'Types: AwsEksCluster, AccountIds: "{account["Id"]}"')
      dynamo_db_tables = ermetic_request(aws_billable_resources,filters=f'Types: AwsDynamoDbTable, AccountIds: "{account["Id"]}"')
      elastic_search_domains = ermetic_request(aws_billable_resources,filters=f'Types: AwsElasticsearchDomain, AccountIds: "{account["Id"]}"')
      lambda_functions = ermetic_request(aws_billable_resources,filters=f'Types: AwsLambdaFunctionConfiguration, AccountIds: "{account["Id"]}"')
      rds_clusters = ermetic_request(aws_billable_resources,filters=f'Types: AwsRdsCluster, AccountIds: "{account["Id"]}"')
      redshift_clusters = ermetic_request(aws_billable_resources,filters=f'Types: AwsRedshiftCluster, AccountIds: "{account["Id"]}"')
      s3_buckets = ermetic_request(aws_billable_resources,filters=f'Types: AwsS3Bucket, AccountIds: "{account["Id"]}"')

      normalized_lambdas = round(len(lambda_functions) / 10)
      total_resources = len(ec2_instances) + len(ecs_services) + len(eks_clusters) + len(dynamo_db_tables) + len(elastic_search_domains) + normalized_lambdas + len(rds_clusters) + len(redshift_clusters) + len(s3_buckets)
      
      obj["EC2Instance"] = len(ec2_instances)
      obj["EcsServices"] = len(ecs_services)
      obj["EksClusters"] = len(eks_clusters)
      obj["DynamoDBTables"] = len(dynamo_db_tables)
      obj["ElasticSearchDomains"] = len(elastic_search_domains)
      obj["LambdaFunctions"] = normalized_lambdas
      obj["RdsClusters"] = len(rds_clusters)
      obj["RedShiftClusters"] = len(redshift_clusters)
      obj["S3Buckets"] = len(s3_buckets)
      obj["Total"] = total_resources

      billable_resources_report.append(obj)
      
    save_to_csv(file_name='aws_billable_resources',data=billable_resources_report)