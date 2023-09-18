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
from common.ermetic_request import ermetic_request
from common.ReportHandler import ReportHandler
from common.get_ermetic_folder_path import get_ermetic_folder_path
from operations.get_aws_accounts import get_aws_accounts
from operations.Folders import Folders
from queries.aws_billable_resources import aws_billable_resources


def get_aws_billable_resources():
    aws_accounts = get_aws_accounts()
    get_folders = Folders()
    count = 0
    result = []
    for account in aws_accounts:
        count += 1
        print(
            f"Currently calculating resources on Account {account['Id']}: {round(count / len(aws_accounts) * 100)}% completion")
        obj = {
            "AccountName": account['Name'],
            "AccountId": account['Id'],
            "Folder": get_ermetic_folder_path(folders=get_folders.foldes_list, folder_id=account['ParentScopeId'])
        }
        ec2_instances = ermetic_request(
            aws_billable_resources, filters=f'Types: AwsEc2Instance, AccountIds: "{account["Id"]}"')
        ecs_services = ermetic_request(
            aws_billable_resources, filters=f'Types: AwsEcsService, AccountIds: "{account["Id"]}"')
        eks_clusters = ermetic_request(
            aws_billable_resources, filters=f'Types: AwsEksCluster, AccountIds: "{account["Id"]}"')
        dynamo_db_tables = ermetic_request(
            aws_billable_resources, filters=f'Types: AwsDynamoDbTable, AccountIds: "{account["Id"]}"')
        elastic_search_domains = ermetic_request(
            aws_billable_resources, filters=f'Types: AwsElasticsearchDomain, AccountIds: "{account["Id"]}"')
        lambda_functions = ermetic_request(
            aws_billable_resources, filters=f'Types: AwsLambdaFunctionConfiguration, AccountIds: "{account["Id"]}"')
        rds_clusters = ermetic_request(
            aws_billable_resources, filters=f'Types: AwsRdsCluster, AccountIds: "{account["Id"]}"')
        redshift_clusters = ermetic_request(
            aws_billable_resources, filters=f'Types: AwsRedshiftCluster, AccountIds: "{account["Id"]}"')
        s3_buckets = ermetic_request(
            aws_billable_resources, filters=f'Types: AwsS3Bucket, AccountIds: "{account["Id"]}"')

        normalized_lambdas = round(len(lambda_functions) / 10)
        total_resources = len(ec2_instances) + len(ecs_services) + len(eks_clusters) + len(dynamo_db_tables) + len(
            elastic_search_domains) + normalized_lambdas + len(rds_clusters) + len(redshift_clusters) + len(s3_buckets)

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

        result.append(obj)

    return result
