from enum import Enum

class FindingTypes(Enum):
    AwsCloudFrontDistributionHttpsOnlyDisabledFinding = "AwsCloudFrontDistributionHttpsOnlyDisabledFinding"
    AwsCloudFrontDistributionInsecureTlsProtocolFinding = "AwsCloudFrontDistributionInsecureTlsProtocolFinding"
    AwsCloudFrontDistributionLoggingDisabledFinding = "AwsCloudFrontDistributionLoggingDisabledFinding"
    AwsCloudFrontDistributionOriginHttpsOnlyDisabledFinding = "AwsCloudFrontDistributionOriginHttpsOnlyDisabledFinding"
    AwsCloudFrontDistributionRootObjectNotExistsFinding = "AwsCloudFrontDistributionRootObjectNotExistsFinding"
    AwsCloudFrontDistributionWebAclNotExistsFinding = "AwsCloudFrontDistributionWebAclNotExistsFinding"
    AwsCloudTrailTrailBucketEventDisabledFinding = "AwsCloudTrailTrailBucketEventDisabledFinding"
    AwsCloudTrailTrailBucketPublicAccessEnabledFinding = "AwsCloudTrailTrailBucketPublicAccessEnabledFinding"
    AwsCloudTrailTrailDigestDisabledFinding = "AwsCloudTrailTrailDigestDisabledFinding"
    AwsCloudTrailTrailEncryptionDisabledFinding = "AwsCloudTrailTrailEncryptionDisabledFinding"
    AwsCloudTrailTrailMultiRegionNotExistFinding = "AwsCloudTrailTrailMultiRegionNotExistFinding"
    AwsCloudWatchAlarmCloudTrailChangesNotExistFinding = "AwsCloudWatchAlarmCloudTrailChangesNotExistFinding"
    AwsCloudWatchAlarmConfigChangesNotExistFinding = "AwsCloudWatchAlarmConfigChangesNotExistFinding"
    AwsCloudWatchAlarmEc2InternetGatewayChangesNotExistFinding = "AwsCloudWatchAlarmEc2InternetGatewayChangesNotExistFinding"
    AwsCloudWatchAlarmEc2NetworkAclChangesNotExistFinding = "AwsCloudWatchAlarmEc2NetworkAclChangesNotExistFinding"
    AwsCloudWatchAlarmEc2RouteTableChangesNotExistFinding = "AwsCloudWatchAlarmEc2RouteTableChangesNotExistFinding"
    AwsCloudWatchAlarmEc2SecurityGroupChangesNotExistFinding = "AwsCloudWatchAlarmEc2SecurityGroupChangesNotExistFinding"
    AwsCloudWatchAlarmEc2VpcChangesNotExistFinding = "AwsCloudWatchAlarmEc2VpcChangesNotExistFinding"
    AwsCloudWatchAlarmIamPolicyChangesNotExistFinding = "AwsCloudWatchAlarmIamPolicyChangesNotExistFinding"
    AwsCloudWatchAlarmKmsCustomerMasterKeyDisabledNotExistFinding = "AwsCloudWatchAlarmKmsCustomerMasterKeyDisabledNotExistFinding"
    AwsCloudWatchAlarmManagementConsoleAuthenticationFailuresNotExistFinding = "AwsCloudWatchAlarmManagementConsoleAuthenticationFailuresNotExistFinding"
    AwsCloudWatchAlarmManagementConsoleMfaDisabledNotExistFinding = "AwsCloudWatchAlarmManagementConsoleMfaDisabledNotExistFinding"
    AwsCloudWatchAlarmOrganizationsOrganizationChangesNotExistFinding = "AwsCloudWatchAlarmOrganizationsOrganizationChangesNotExistFinding"
    AwsCloudWatchAlarmRootUsageNotExistFinding = "AwsCloudWatchAlarmRootUsageNotExistFinding"
    AwsCloudWatchAlarmS3BucketPolicyChangesNotExistFinding = "AwsCloudWatchAlarmS3BucketPolicyChangesNotExistFinding"
    AwsCloudWatchAlarmUnauthorizedApiCallsNotExistFinding = "AwsCloudWatchAlarmUnauthorizedApiCallsNotExistFinding"
    AwsContainerImageOperatingSystemEndOfLifeFinding = "AwsContainerImageOperatingSystemEndOfLifeFinding"
    AwsContainerImageOperatingSystemUnpatchedFinding = "AwsContainerImageOperatingSystemUnpatchedFinding"
    AwsContainerImageVulnerabilityFinding = "AwsContainerImageVulnerabilityFinding"
    AwsDataLeakageFinding = "AwsDataLeakageFinding"
    AwsEc2ImagePublicAccessExistsFinding = "AwsEc2ImagePublicAccessExistsFinding"
    AwsEc2InstanceMetadataServiceVersionFinding = "AwsEc2InstanceMetadataServiceVersionFinding"
    AwsEc2InstanceOperatingSystemEndOfLifeFinding = "AwsEc2InstanceOperatingSystemEndOfLifeFinding"
    AwsEc2InstanceOperatingSystemUnpatchedFinding = "AwsEc2InstanceOperatingSystemUnpatchedFinding"
    AwsEc2InstanceUserDataSecretExistsFinding = "AwsEc2InstanceUserDataSecretExistsFinding"
    AwsEc2InstanceVulnerabilityFinding = "AwsEc2InstanceVulnerabilityFinding"
    AwsEc2LoadBalancerListenerInsecureSslProtocolExistsFinding = "AwsEc2LoadBalancerListenerInsecureSslProtocolExistsFinding"
    AwsEc2SecurityGroupAllowedInboundRuleFinding = "AwsEc2SecurityGroupAllowedInboundRuleFinding"
    AwsEc2SecurityGroupInboundRuleSubnetAnyExistsFinding = "AwsEc2SecurityGroupInboundRuleSubnetAnyExistsFinding"
    AwsEc2SecurityGroupManagementFinding = "AwsEc2SecurityGroupManagementFinding"
    AwsEc2SecurityGroupNotAllowedInboundRuleFinding = "AwsEc2SecurityGroupNotAllowedInboundRuleFinding"
    AwsEc2SecurityGroupUnusedFinding = "AwsEc2SecurityGroupUnusedFinding"
    AwsEc2SnapshotEncryptionDisabledFinding = "AwsEc2SnapshotEncryptionDisabledFinding"
    AwsEc2SnapshotPublicAccessExistsFinding = "AwsEc2SnapshotPublicAccessExistsFinding"
    AwsEc2VolumeEncryptionDisabledFinding = "AwsEc2VolumeEncryptionDisabledFinding"
    AwsEc2VpcDefaultSecurityGroupRuleExistsFinding = "AwsEc2VpcDefaultSecurityGroupRuleExistsFinding"
    AwsEc2VpcEndpointUnrestrictedServiceAccessFinding = "AwsEc2VpcEndpointUnrestrictedServiceAccessFinding"
    AwsEc2VpcRejectFlowLogNotExistFinding = "AwsEc2VpcRejectFlowLogNotExistFinding"
    AwsEcrRepositoryContainerImageVulnerabilityFinding = "AwsEcrRepositoryContainerImageVulnerabilityFinding"
    AwsEcrRepositoryPublicAccessExistsFinding = "AwsEcrRepositoryPublicAccessExistsFinding"
    AwsEcsTaskDefinitionEnvironmentVariableSecretExistsFinding = "AwsEcsTaskDefinitionEnvironmentVariableSecretExistsFinding"
    AwsEksClusterInboundExternalWideRangeFinding = "AwsEksClusterInboundExternalWideRangeFinding"
    AwsEncryptedResourceKmsEncryptionNotExistsFinding = "AwsEncryptedResourceKmsEncryptionNotExistsFinding"
    AwsEsDomainEncryptionDisabledFinding = "AwsEsDomainEncryptionDisabledFinding"
    AwsEsDomainNodeCommunicationEncryptionDisabledFinding = "AwsEsDomainNodeCommunicationEncryptionDisabledFinding"
    AwsEsDomainPublicAccessExistsFinding = "AwsEsDomainPublicAccessExistsFinding"
    AwsExcessivePermissionBucketFinding = "AwsExcessivePermissionBucketFinding"
    AwsExcessivePermissionGroupFinding = "AwsExcessivePermissionGroupFinding"
    AwsExcessivePermissionPermissionSetFinding = "AwsExcessivePermissionPermissionSetFinding"
    AwsExcessivePermissionRepositoryFinding = "AwsExcessivePermissionRepositoryFinding"
    AwsExcessivePermissionRoleFinding = "AwsExcessivePermissionRoleFinding"
    AwsExcessivePermissionSecretFinding = "AwsExcessivePermissionSecretFinding"
    AwsExcessivePermissionUserFinding = "AwsExcessivePermissionUserFinding"
    AwsIamPasswordLengthPolicyFinding = "AwsIamPasswordLengthPolicyFinding"
    AwsIamPasswordReusePolicyFinding = "AwsIamPasswordReusePolicyFinding"
    AwsIamPrincipalCreationFinding = "AwsIamPrincipalCreationFinding"
    AwsIamRoleManagementFinding = "AwsIamRoleManagementFinding"
    AwsIamRolePublicAccessExistsFinding = "AwsIamRolePublicAccessExistsFinding"
    AwsIamRoleVendorAssumeRolePolicyDocumentExternalIdConditionNotExistFinding = "AwsIamRoleVendorAssumeRolePolicyDocumentExternalIdConditionNotExistFinding"
    AwsIamRootUserAccessKeyEnabledFinding = "AwsIamRootUserAccessKeyEnabledFinding"
    AwsIamRootUserActivityFinding = "AwsIamRootUserActivityFinding"
    AwsIamRootUserMfaDisabledFinding = "AwsIamRootUserMfaDisabledFinding"
    AwsIamUserMfaDisabledFinding = "AwsIamUserMfaDisabledFinding"
    AwsIamUserUnrotatedAccessKeyFinding = "AwsIamUserUnrotatedAccessKeyFinding"
    AwsIamUserUnusedCredentialsEnabledFinding = "AwsIamUserUnusedCredentialsEnabledFinding"
    AwsIdentityActivityFinding = "AwsIdentityActivityFinding"
    AwsInactiveRoleFinding = "AwsInactiveRoleFinding"
    AwsInactiveUserFinding = "AwsInactiveUserFinding"
    AwsInboundExternalEc2InstanceFinding = "AwsInboundExternalEc2InstanceFinding"
    AwsInboundExternalElbLoadBalancerFinding = "AwsInboundExternalElbLoadBalancerFinding"
    AwsInboundExternalRdsDatabaseInstanceFinding = "AwsInboundExternalRdsDatabaseInstanceFinding"
    AwsInboundExternalRedshiftClusterFinding = "AwsInboundExternalRedshiftClusterFinding"
    AwsInboundExternalSubnetFinding = "AwsInboundExternalSubnetFinding"
    AwsInboundExternalVpcFinding = "AwsInboundExternalVpcFinding"
    AwsKmsKeyManagementFinding = "AwsKmsKeyManagementFinding"
    AwsKmsKeyPublicAccessExistsFinding = "AwsKmsKeyPublicAccessExistsFinding"
    AwsKmsKeyRotationDisabledFinding = "AwsKmsKeyRotationDisabledFinding"
    AwsKubernetesWorkloadResourceContainerPrivilegeEscalationFinding = "AwsKubernetesWorkloadResourceContainerPrivilegeEscalationFinding"
    AwsKubernetesWorkloadResourceContainerPrivilegedFinding = "AwsKubernetesWorkloadResourceContainerPrivilegedFinding"
    AwsKubernetesWorkloadResourceContainerSensitiveCapabilityRisk = "AwsKubernetesWorkloadResourceContainerSensitiveCapabilityRisk"
    AwsLambdaFunctionConfigurationEnvironmentVariableSecretExistsFinding = "AwsLambdaFunctionConfigurationEnvironmentVariableSecretExistsFinding"
    AwsLambdaFunctionConfigurationPublicAccessExistsFinding = "AwsLambdaFunctionConfigurationPublicAccessExistsFinding"
    AwsNetworkAccessManagementFinding = "AwsNetworkAccessManagementFinding"
    AwsNetworkedResourceInboundExternalPortFinding = "AwsNetworkedResourceInboundExternalPortFinding"
    AwsPermissionManagementFinding = "AwsPermissionManagementFinding"
    AwsPrincipalAllowedPermissionFinding = "AwsPrincipalAllowedPermissionFinding"
    AwsPrincipalAllowedResourcePermissionFinding = "AwsPrincipalAllowedResourcePermissionFinding"
    AwsPrincipalNotAllowedResourcePermissionFinding = "AwsPrincipalNotAllowedResourcePermissionFinding"
    AwsPrivilegeEscalationFinding = "AwsPrivilegeEscalationFinding"
    AwsRdsDatabaseInstanceStorageEncryptionDisabledFinding = "AwsRdsDatabaseInstanceStorageEncryptionDisabledFinding"
    AwsRdsSnapshotEncryptionDisabledFinding = "AwsRdsSnapshotEncryptionDisabledFinding"
    AwsRdsSnapshotPublicAccessExistsFinding = "AwsRdsSnapshotPublicAccessExistsFinding"
    AwsReconnaissanceFinding = "AwsReconnaissanceFinding"
    AwsResourceTagNotExistsFinding = "AwsResourceTagNotExistsFinding"
    AwsResourceTagSecretExistsFinding = "AwsResourceTagSecretExistsFinding"
    AwsS3BucketBlockPublicAccessDisabledFinding = "AwsS3BucketBlockPublicAccessDisabledFinding"
    AwsS3BucketEncryptionDisabledFinding = "AwsS3BucketEncryptionDisabledFinding"
    AwsS3BucketHttpsOnlyDisabledFinding = "AwsS3BucketHttpsOnlyDisabledFinding"
    AwsS3BucketManagementFinding = "AwsS3BucketManagementFinding"
    AwsS3BucketObjectMfaDeleteDisabledFinding = "AwsS3BucketObjectMfaDeleteDisabledFinding"
    AwsS3BucketPublicAccessExistsFinding = "AwsS3BucketPublicAccessExistsFinding"
    AwsSecretsManagerSecretManagementFinding = "AwsSecretsManagerSecretManagementFinding"
    AwsSecretsManagerSecretPublicAccessExistsFinding = "AwsSecretsManagerSecretPublicAccessExistsFinding"
    AwsSecretsManagerSecretRotationDisabledFinding = "AwsSecretsManagerSecretRotationDisabledFinding"
    AwsSeverePermissionPrincipalFinding = "AwsSeverePermissionPrincipalFinding"
    AwsSnsTopicEncryptionDisabledFinding = "AwsSnsTopicEncryptionDisabledFinding"
    AwsSnsTopicPublicAccessExistsFinding = "AwsSnsTopicPublicAccessExistsFinding"
    AwsSqsQueueEncryptionDisabledFinding = "AwsSqsQueueEncryptionDisabledFinding"
    AwsSqsQueuePublicAccessExistsFinding = "AwsSqsQueuePublicAccessExistsFinding"
    AwsSsmParameterSecretExistsFinding = "AwsSsmParameterSecretExistsFinding"
    AwsSsoPermissionSetsManagementFinding = "AwsSsoPermissionSetsManagementFinding"
    AwsSsoPrincipalCreationFinding = "AwsSsoPrincipalCreationFinding"
    AwsUnusedPermissionSetFinding = "AwsUnusedPermissionSetFinding"
    AzureComputeVirtualMachineUnmanagedDiskExistsFinding = "AzureComputeVirtualMachineUnmanagedDiskExistsFinding"
    AzureContainerRegistryRegistryAccessKeyEnabledFinding = "AzureContainerRegistryRegistryAccessKeyEnabledFinding"
    AzureContainerRegistryRegistryInboundExternalWideRangeFinding = "AzureContainerRegistryRegistryInboundExternalWideRangeFinding"
    AzureContainerServiceManagedClusterIdentityAuthenticationDisabledFinding = "AzureContainerServiceManagedClusterIdentityAuthenticationDisabledFinding"
    AzureContainerServiceManagedClusterInboundExternalWideRangeFinding = "AzureContainerServiceManagedClusterInboundExternalWideRangeFinding"
    AzureCosmosDbDatabaseAccountWideRangeInboundFinding = "AzureCosmosDbDatabaseAccountWideRangeInboundFinding"
    AzureDocumentDbDatabaseAccountKeyAccessEnabledFinding = "AzureDocumentDbDatabaseAccountKeyAccessEnabledFinding"
    AzureEventHubNamespaceInboundExternalWideRangeFinding = "AzureEventHubNamespaceInboundExternalWideRangeFinding"
    AzureExcessivePermissionApplicationServicePrincipalFinding = "AzureExcessivePermissionApplicationServicePrincipalFinding"
    AzureExcessivePermissionGroupFinding = "AzureExcessivePermissionGroupFinding"
    AzureExcessivePermissionManagedIdentityServicePrincipalFinding = "AzureExcessivePermissionManagedIdentityServicePrincipalFinding"
    AzureExcessivePermissionUserFinding = "AzureExcessivePermissionUserFinding"
    AzureGuestUserAdministratorFinding = "AzureGuestUserAdministratorFinding"
    AzureInactiveApplicationServicePrincipalFinding = "AzureInactiveApplicationServicePrincipalFinding"
    AzureInactiveManagedIdentityServicePrincipalFinding = "AzureInactiveManagedIdentityServicePrincipalFinding"
    AzureInactiveUserFinding = "AzureInactiveUserFinding"
    AzureInboundExternalComputeVirtualMachineFinding = "AzureInboundExternalComputeVirtualMachineFinding"
    AzureInboundExternalComputeVirtualMachineScaleSetFinding = "AzureInboundExternalComputeVirtualMachineScaleSetFinding"
    AzureInsightsDiagnosticSettingsStorageAccountBlobContainerDefaultEncryptionFinding = "AzureInsightsDiagnosticSettingsStorageAccountBlobContainerDefaultEncryptionFinding"
    AzureInsightsDiagnosticSettingsStorageAccountBlobContainerPublicAccessEnabledFinding = "AzureInsightsDiagnosticSettingsStorageAccountBlobContainerPublicAccessEnabledFinding"
    AzureInsightsDiagnosticSettingsSubscriptionLogCategoryAdministrativeNotExistsFinding = "AzureInsightsDiagnosticSettingsSubscriptionLogCategoryAdministrativeNotExistsFinding"
    AzureKeyVaultVaultCertificateNotRotatedFinding = "AzureKeyVaultVaultCertificateNotRotatedFinding"
    AzureKeyVaultVaultEventDisabledFinding = "AzureKeyVaultVaultEventDisabledFinding"
    AzureKeyVaultVaultKeyExpirationDisabledFinding = "AzureKeyVaultVaultKeyExpirationDisabledFinding"
    AzureKeyVaultVaultRbacDisabledFinding = "AzureKeyVaultVaultRbacDisabledFinding"
    AzureKeyVaultVaultSecretExpirationDisabledFinding = "AzureKeyVaultVaultSecretExpirationDisabledFinding"
    AzureKeyVaultVaultSoftDeleteDisabledFinding = "AzureKeyVaultVaultSoftDeleteDisabledFinding"
    AzureKeyVaultVaultWideRangeInboundFinding = "AzureKeyVaultVaultWideRangeInboundFinding"
    AzureKubernetesWorkloadResourceContainerPrivilegeEscalationFinding = "AzureKubernetesWorkloadResourceContainerPrivilegeEscalationFinding"
    AzureKubernetesWorkloadResourceContainerPrivilegedFinding = "AzureKubernetesWorkloadResourceContainerPrivilegedFinding"
    AzureKubernetesWorkloadResourceContainerSensitiveCapabilityRisk = "AzureKubernetesWorkloadResourceContainerSensitiveCapabilityRisk"
    AzureLogicWorkflowInboundExternalWideRangeFinding = "AzureLogicWorkflowInboundExternalWideRangeFinding"
    AzureLogicWorkflowSecretExistsFinding = "AzureLogicWorkflowSecretExistsFinding"
    AzureMySqlServerHttpsOnlyDisabledFinding = "AzureMySqlServerHttpsOnlyDisabledFinding"
    AzureMySqlServerWideRangeInboundFinding = "AzureMySqlServerWideRangeInboundFinding"
    AzureNetworkAccessManagementFinding = "AzureNetworkAccessManagementFinding"
    AzureNetworkNetworkSecurityGroupInboundRuleSubnetAnyRdpExistsFinding = "AzureNetworkNetworkSecurityGroupInboundRuleSubnetAnyRdpExistsFinding"
    AzureNetworkNetworkSecurityGroupInboundRuleSubnetAnySshExistsFinding = "AzureNetworkNetworkSecurityGroupInboundRuleSubnetAnySshExistsFinding"
    AzureNetworkNetworkSecurityGroupInboundRuleSubnetAnyUdpExistsFinding = "AzureNetworkNetworkSecurityGroupInboundRuleSubnetAnyUdpExistsFinding"
    AzureNetworkVirtualNetworkSubnetUnrestrictedInboundAccessFinding = "AzureNetworkVirtualNetworkSubnetUnrestrictedInboundAccessFinding"
    AzurePermissionManagementFinding = "AzurePermissionManagementFinding"
    AzurePostgreSqlServerConnectionThrottlingDisabledFinding = "AzurePostgreSqlServerConnectionThrottlingDisabledFinding"
    AzurePostgreSqlServerHttpsOnlyDisabledFinding = "AzurePostgreSqlServerHttpsOnlyDisabledFinding"
    AzurePostgreSqlServerLogCheckpointsDisabledFinding = "AzurePostgreSqlServerLogCheckpointsDisabledFinding"
    AzurePostgreSqlServerLogConnectionsDisabledFinding = "AzurePostgreSqlServerLogConnectionsDisabledFinding"
    AzurePostgreSqlServerLogDisconnectionsDisabledFinding = "AzurePostgreSqlServerLogDisconnectionsDisabledFinding"
    AzurePostgreSqlServerLogRetentionFinding = "AzurePostgreSqlServerLogRetentionFinding"
    AzurePostgreSqlServerWideRangeInboundFinding = "AzurePostgreSqlServerWideRangeInboundFinding"
    AzurePrincipalAllowedResourcePermissionFinding = "AzurePrincipalAllowedResourcePermissionFinding"
    AzurePrincipalNotAllowedResourcePermissionFinding = "AzurePrincipalNotAllowedResourcePermissionFinding"
    AzureResourceInboundExternalPortFinding = "AzureResourceInboundExternalPortFinding"
    AzureResourceTagNotExistsFinding = "AzureResourceTagNotExistsFinding"
    AzureResourceTagSecretExistsFinding = "AzureResourceTagSecretExistsFinding"
    AzureSeverePermissionPrincipalFinding = "AzureSeverePermissionPrincipalFinding"
    AzureSqlServerDatabaseEncryptionDisabledFinding = "AzureSqlServerDatabaseEncryptionDisabledFinding"
    AzureSqlServerEventDisabledFinding = "AzureSqlServerEventDisabledFinding"
    AzureSqlServerWideRangeInboundFinding = "AzureSqlServerWideRangeInboundFinding"
    AzureStorageStorageAccountBlobContainerPublicAccessExistsFinding = "AzureStorageStorageAccountBlobContainerPublicAccessExistsFinding"
    AzureStorageStorageAccountHttpsOnlyDisabledFinding = "AzureStorageStorageAccountHttpsOnlyDisabledFinding"
    AzureStorageStorageAccountSharedKeyAccessEnabledFinding = "AzureStorageStorageAccountSharedKeyAccessEnabledFinding"
    AzureStorageStorageAccountSoftDeleteDisabledFinding = "AzureStorageStorageAccountSoftDeleteDisabledFinding"
    AzureStorageStorageAccountWideRangeInboundFinding = "AzureStorageStorageAccountWideRangeInboundFinding"
    AzureTenantEntityCreationFinding = "AzureTenantEntityCreationFinding"
    AzureWebApplicationHttpsOnlyDisabledFinding = "AzureWebApplicationHttpsOnlyDisabledFinding"
    AzureWebApplicationInboundExternalWideRangeFinding = "AzureWebApplicationInboundExternalWideRangeFinding"
    AzureWebApplicationInsecureTlsProtocolFinding = "AzureWebApplicationInsecureTlsProtocolFinding"
    AzureWebApplicationScmInboundExternalWideRangeFinding = "AzureWebApplicationScmInboundExternalWideRangeFinding"
    GcpAppEngineApplicationServiceEnvironmentVariableSecretExistsFinding = "GcpAppEngineApplicationServiceEnvironmentVariableSecretExistsFinding"
    GcpAppEngineApplicationServiceUnencryptedTransportExistsFinding = "GcpAppEngineApplicationServiceUnencryptedTransportExistsFinding"
    GcpArtifactRegistryPublicAccessExistsFinding = "GcpArtifactRegistryPublicAccessExistsFinding"
    GcpBigQueryDatasetPublicAccessExistsFinding = "GcpBigQueryDatasetPublicAccessExistsFinding"
    GcpCloudRunServiceEnvironmentVariableSecretExistsFinding = "GcpCloudRunServiceEnvironmentVariableSecretExistsFinding"
    GcpCloudRunServicePublicAccessExistsFinding = "GcpCloudRunServicePublicAccessExistsFinding"
    GcpComputeImagePublicAccessExistsFinding = "GcpComputeImagePublicAccessExistsFinding"
    GcpComputeInstanceBlockProjectWideSshKeysNotEnabledFinding = "GcpComputeInstanceBlockProjectWideSshKeysNotEnabledFinding"
    GcpComputeInstanceDefaultServiceAccountFinding = "GcpComputeInstanceDefaultServiceAccountFinding"
    GcpComputeInstanceIpForwardingEnabledFinding = "GcpComputeInstanceIpForwardingEnabledFinding"
    GcpComputeInstanceOperatingSystemEndOfLifeFinding = "GcpComputeInstanceOperatingSystemEndOfLifeFinding"
    GcpComputeInstanceOperatingSystemUnpatchedFinding = "GcpComputeInstanceOperatingSystemUnpatchedFinding"
    GcpComputeInstanceSshSerialPortEnabledFinding = "GcpComputeInstanceSshSerialPortEnabledFinding"
    GcpComputeInstanceStartupScriptSecretExistsFinding = "GcpComputeInstanceStartupScriptSecretExistsFinding"
    GcpComputeInstanceVulnerabilityFinding = "GcpComputeInstanceVulnerabilityFinding"
    GcpComputeLoadBalancerInsecureSslPolicyFinding = "GcpComputeLoadBalancerInsecureSslPolicyFinding"
    GcpComputeProjectSshIamNotEnabledFinding = "GcpComputeProjectSshIamNotEnabledFinding"
    GcpComputeVpcUnrestrictedRdpInboundAccessFinding = "GcpComputeVpcUnrestrictedRdpInboundAccessFinding"
    GcpComputeVpcUnrestrictedSshInboundAccessFinding = "GcpComputeVpcUnrestrictedSshInboundAccessFinding"
    GcpContainerClusterDefaultServiceAccountFinding = "GcpContainerClusterDefaultServiceAccountFinding"
    GcpContainerClusterInboundExternalWideRangeFinding = "GcpContainerClusterInboundExternalWideRangeFinding"
    GcpContainerImageOperatingSystemEndOfLifeFinding = "GcpContainerImageOperatingSystemEndOfLifeFinding"
    GcpContainerImageOperatingSystemUnpatchedFinding = "GcpContainerImageOperatingSystemUnpatchedFinding"
    GcpContainerImageVulnerabilityFinding = "GcpContainerImageVulnerabilityFinding"
    GcpExcessivePermissionServiceAccountFinding = "GcpExcessivePermissionServiceAccountFinding"
    GcpExcessivePermissionUserFinding = "GcpExcessivePermissionUserFinding"
    GcpFunctionsFunctionEnvironmentVariableSecretExistsFinding = "GcpFunctionsFunctionEnvironmentVariableSecretExistsFinding"
    GcpFunctionsFunctionPublicAccessExistsFinding = "GcpFunctionsFunctionPublicAccessExistsFinding"
    GcpIamServiceAccountUnrotatedUserManagedKeyFinding = "GcpIamServiceAccountUnrotatedUserManagedKeyFinding"
    GcpIamServiceAccountUserManagedKeyExistsFinding = "GcpIamServiceAccountUserManagedKeyExistsFinding"
    GcpIdentityActivityFinding = "GcpIdentityActivityFinding"
    GcpInactiveServiceAccountFinding = "GcpInactiveServiceAccountFinding"
    GcpInactiveUserFinding = "GcpInactiveUserFinding"
    GcpInboundExternalComputeInstanceFinding = "GcpInboundExternalComputeInstanceFinding"
    GcpKmsKeyRingKeyPublicAccessExistsFinding = "GcpKmsKeyRingKeyPublicAccessExistsFinding"
    GcpKmsKeyRingKeyRotationIntervalFinding = "GcpKmsKeyRingKeyRotationIntervalFinding"
    GcpKmsKeyRingPublicAccessExistsFinding = "GcpKmsKeyRingPublicAccessExistsFinding"
    GcpKubernetesWorkloadResourceContainerPrivilegeEscalationFinding = "GcpKubernetesWorkloadResourceContainerPrivilegeEscalationFinding"
    GcpKubernetesWorkloadResourceContainerPrivilegedFinding = "GcpKubernetesWorkloadResourceContainerPrivilegedFinding"
    GcpKubernetesWorkloadResourceContainerSensitiveCapabilityFinding = "GcpKubernetesWorkloadResourceContainerSensitiveCapabilityFinding"
    GcpLoggingAuditLogProjectDefaultNotEnabledFinding = "GcpLoggingAuditLogProjectDefaultNotEnabledFinding"
    GcpPermissionManagementFinding = "GcpPermissionManagementFinding"
    GcpPrincipalAllowedResourcePermissionFinding = "GcpPrincipalAllowedResourcePermissionFinding"
    GcpPrincipalNotAllowedResourcePermissionFinding = "GcpPrincipalNotAllowedResourcePermissionFinding"
    GcpPrincipalServiceAccountWideScopeAdministratorRoleFinding = "GcpPrincipalServiceAccountWideScopeAdministratorRoleFinding"
    GcpPrincipalServiceAccountWideScopeImpersonateServiceAccountActionExistsFinding = "GcpPrincipalServiceAccountWideScopeImpersonateServiceAccountActionExistsFinding"
    GcpPrincipalUserWideScopeImpersonateServiceAccountActionExistsFinding = "GcpPrincipalUserWideScopeImpersonateServiceAccountActionExistsFinding"
    GcpProjectResourceCreationFinding = "GcpProjectResourceCreationFinding"
    GcpPubSubSubscriptionPublicAccessExistsFinding = "GcpPubSubSubscriptionPublicAccessExistsFinding"
    GcpPubSubTopicPublicAccessExistsFinding = "GcpPubSubTopicPublicAccessExistsFinding"
    GcpResourceInboundExternalPortFinding = "GcpResourceInboundExternalPortFinding"
    GcpResourceTagNotExistsFinding = "GcpResourceTagNotExistsFinding"
    GcpResourceTagSecretExistsFinding = "GcpResourceTagSecretExistsFinding"
    GcpSecretManagerSecretRotationIntervalFinding = "GcpSecretManagerSecretRotationIntervalFinding"
    GcpSeverePermissionPrincipalFinding = "GcpSeverePermissionPrincipalFinding"
    GcpSqlInstanceHttpsOnlyDisabledFinding = "GcpSqlInstanceHttpsOnlyDisabledFinding"
    GcpSqlInstanceMySqlListDatabasesPermissionRequiredDisabledFinding = "GcpSqlInstanceMySqlListDatabasesPermissionRequiredDisabledFinding"
    GcpSqlInstanceMySqlLoadClientFileEnabledFinding = "GcpSqlInstanceMySqlLoadClientFileEnabledFinding"
    GcpSqlInstancePostgreSqlLogConnectionsDisabledFinding = "GcpSqlInstancePostgreSqlLogConnectionsDisabledFinding"
    GcpSqlInstancePostgreSqlLogConnectionsHostNameDisabledFinding = "GcpSqlInstancePostgreSqlLogConnectionsHostNameDisabledFinding"
    GcpSqlInstancePostgreSqlLogDisconnectionsDisabledFinding = "GcpSqlInstancePostgreSqlLogDisconnectionsDisabledFinding"
    GcpSqlInstancePostgreSqlMinDurationLogQueryEnabledFinding = "GcpSqlInstancePostgreSqlMinDurationLogQueryEnabledFinding"
    GcpSqlInstancePostgreSqlMinLogLevelLogQueryFinding = "GcpSqlInstancePostgreSqlMinLogLevelLogQueryFinding"
    GcpSqlInstanceSqlServerCrossDatabaseImplicitPermissionsEnabledFinding = "GcpSqlInstanceSqlServerCrossDatabaseImplicitPermissionsEnabledFinding"
    GcpSqlInstanceSqlServerCrossInstanceProcedureExecutionEnabledFinding = "GcpSqlInstanceSqlServerCrossInstanceProcedureExecutionEnabledFinding"
    GcpSqlInstanceSqlServerScriptExecutionEnabledFinding = "GcpSqlInstanceSqlServerScriptExecutionEnabledFinding"
    GcpSqlInstanceWideRangeInboundFinding = "GcpSqlInstanceWideRangeInboundFinding"
    GcpStorageBucketPublicAccessExistsFinding = "GcpStorageBucketPublicAccessExistsFinding"
    GcpStorageBucketUniformAccessControlDisabledFinding = "GcpStorageBucketUniformAccessControlDisabledFinding"
    GcpTenantEntityUnusedFinding = "GcpTenantEntityUnusedFinding"