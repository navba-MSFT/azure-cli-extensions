# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "stack-hci cluster update",
)
class Update(AAZCommand):
    """Update an HCI cluster.

    :example: Update cluster
        az stack-hci cluster update --endpoint "https://98294836-31be-4668-aeae-698667faf99b.waconazure.com" --desired-properties "{diagnosticLevel:Basic,windowsServerSubscription:Enabled}" --tags "tag:"value" --name "myCluster" --resource-group "test-rg"
    """

    _aaz_info = {
        "version": "2023-03-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.azurestackhci/clusters/{}", "2023-03-01"],
        ]
    }

    AZ_SUPPORT_GENERIC_UPDATE = True

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.cluster_name = AAZStrArg(
            options=["-n", "--name", "--cluster-name"],
            help="The name of the cluster.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Cluster"

        _args_schema = cls._args_schema
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="Cluster",
            help="Resource tags.",
            nullable=True,
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg(
            nullable=True,
        )

        # define Arg Group "Identity"

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.aad_client_id = AAZStrArg(
            options=["--aad-client-id"],
            arg_group="Properties",
            help="App id of cluster AAD identity.",
            nullable=True,
        )
        _args_schema.aad_tenant_id = AAZStrArg(
            options=["--aad-tenant-id"],
            arg_group="Properties",
            help="Tenant id of cluster AAD identity.",
            nullable=True,
        )
        _args_schema.endpoint = AAZStrArg(
            options=["--endpoint"],
            arg_group="Properties",
            help="Endpoint configured for management from the Azure portal.",
            nullable=True,
        )
        _args_schema.desired_properties = AAZObjectArg(
            options=["--desired-properties"],
            arg_group="Properties",
            help="Desired properties of the cluster.",
            nullable=True,
        )

        desired_properties = cls._args_schema.desired_properties
        desired_properties.diagnostic_level = AAZStrArg(
            options=["diagnostic-level"],
            help="Desired level of diagnostic data emitted by the cluster.",
            nullable=True,
            enum={"Basic": "Basic", "Enhanced": "Enhanced", "Off": "Off"},
        )
        desired_properties.windows_server_subscription = AAZStrArg(
            options=["windows-server-subscription"],
            help="Desired state of Windows Server Subscription.",
            nullable=True,
            enum={"Disabled": "Disabled", "Enabled": "Enabled"},
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.ClustersGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        self.ClustersCreate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class ClustersGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzureStackHCI/clusters/{clusterName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "clusterName", self.ctx.args.cluster_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-03-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _UpdateHelper._build_schema_cluster_read(cls._schema_on_200)

            return cls._schema_on_200

    class ClustersCreate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzureStackHCI/clusters/{clusterName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "clusterName", self.ctx.args.cluster_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-03-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _UpdateHelper._build_schema_cluster_read(cls._schema_on_200)

            return cls._schema_on_200

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("identity", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("aadClientId", AAZStrType, ".aad_client_id")
                properties.set_prop("aadTenantId", AAZStrType, ".aad_tenant_id")
                properties.set_prop("cloudManagementEndpoint", AAZStrType, ".endpoint")
                properties.set_prop("desiredProperties", AAZObjectType, ".desired_properties")

            desired_properties = _builder.get(".properties.desiredProperties")
            if desired_properties is not None:
                desired_properties.set_prop("diagnosticLevel", AAZStrType, ".diagnostic_level")
                desired_properties.set_prop("windowsServerSubscription", AAZStrType, ".windows_server_subscription")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    _schema_cluster_read = None

    @classmethod
    def _build_schema_cluster_read(cls, _schema):
        if cls._schema_cluster_read is not None:
            _schema.id = cls._schema_cluster_read.id
            _schema.identity = cls._schema_cluster_read.identity
            _schema.location = cls._schema_cluster_read.location
            _schema.name = cls._schema_cluster_read.name
            _schema.properties = cls._schema_cluster_read.properties
            _schema.system_data = cls._schema_cluster_read.system_data
            _schema.tags = cls._schema_cluster_read.tags
            _schema.type = cls._schema_cluster_read.type
            return

        cls._schema_cluster_read = _schema_cluster_read = AAZObjectType()

        cluster_read = _schema_cluster_read
        cluster_read.id = AAZStrType(
            flags={"read_only": True},
        )
        cluster_read.identity = AAZObjectType(
            flags={"client_flatten": True},
        )
        cluster_read.location = AAZStrType(
            flags={"required": True},
        )
        cluster_read.name = AAZStrType(
            flags={"read_only": True},
        )
        cluster_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        cluster_read.system_data = AAZObjectType(
            serialized_name="systemData",
            flags={"read_only": True},
        )
        cluster_read.tags = AAZDictType()
        cluster_read.type = AAZStrType(
            flags={"read_only": True},
        )

        identity = _schema_cluster_read.identity
        identity.principal_id = AAZStrType(
            serialized_name="principalId",
            flags={"read_only": True},
        )
        identity.tenant_id = AAZStrType(
            serialized_name="tenantId",
            flags={"read_only": True},
        )
        identity.type = AAZStrType(
            flags={"required": True},
        )
        identity.user_assigned_identities = AAZDictType(
            serialized_name="userAssignedIdentities",
        )

        user_assigned_identities = _schema_cluster_read.identity.user_assigned_identities
        user_assigned_identities.Element = AAZObjectType()

        _element = _schema_cluster_read.identity.user_assigned_identities.Element
        _element.client_id = AAZStrType(
            serialized_name="clientId",
            flags={"read_only": True},
        )
        _element.principal_id = AAZStrType(
            serialized_name="principalId",
            flags={"read_only": True},
        )

        properties = _schema_cluster_read.properties
        properties.aad_application_object_id = AAZStrType(
            serialized_name="aadApplicationObjectId",
        )
        properties.aad_client_id = AAZStrType(
            serialized_name="aadClientId",
        )
        properties.aad_service_principal_object_id = AAZStrType(
            serialized_name="aadServicePrincipalObjectId",
        )
        properties.aad_tenant_id = AAZStrType(
            serialized_name="aadTenantId",
        )
        properties.billing_model = AAZStrType(
            serialized_name="billingModel",
            flags={"read_only": True},
        )
        properties.cloud_id = AAZStrType(
            serialized_name="cloudId",
            flags={"read_only": True},
        )
        properties.cloud_management_endpoint = AAZStrType(
            serialized_name="cloudManagementEndpoint",
        )
        properties.desired_properties = AAZObjectType(
            serialized_name="desiredProperties",
        )
        properties.last_billing_timestamp = AAZStrType(
            serialized_name="lastBillingTimestamp",
            flags={"read_only": True},
        )
        properties.last_sync_timestamp = AAZStrType(
            serialized_name="lastSyncTimestamp",
            flags={"read_only": True},
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.registration_timestamp = AAZStrType(
            serialized_name="registrationTimestamp",
            flags={"read_only": True},
        )
        properties.reported_properties = AAZObjectType(
            serialized_name="reportedProperties",
        )
        properties.resource_provider_object_id = AAZStrType(
            serialized_name="resourceProviderObjectId",
            flags={"read_only": True},
        )
        properties.service_endpoint = AAZStrType(
            serialized_name="serviceEndpoint",
            flags={"read_only": True},
        )
        properties.software_assurance_properties = AAZObjectType(
            serialized_name="softwareAssuranceProperties",
        )
        properties.status = AAZStrType(
            flags={"read_only": True},
        )
        properties.trial_days_remaining = AAZFloatType(
            serialized_name="trialDaysRemaining",
            flags={"read_only": True},
        )

        desired_properties = _schema_cluster_read.properties.desired_properties
        desired_properties.diagnostic_level = AAZStrType(
            serialized_name="diagnosticLevel",
        )
        desired_properties.windows_server_subscription = AAZStrType(
            serialized_name="windowsServerSubscription",
        )

        reported_properties = _schema_cluster_read.properties.reported_properties
        reported_properties.cluster_id = AAZStrType(
            serialized_name="clusterId",
            flags={"read_only": True},
        )
        reported_properties.cluster_name = AAZStrType(
            serialized_name="clusterName",
            flags={"read_only": True},
        )
        reported_properties.cluster_type = AAZStrType(
            serialized_name="clusterType",
            flags={"read_only": True},
        )
        reported_properties.cluster_version = AAZStrType(
            serialized_name="clusterVersion",
            flags={"read_only": True},
        )
        reported_properties.diagnostic_level = AAZStrType(
            serialized_name="diagnosticLevel",
        )
        reported_properties.imds_attestation = AAZStrType(
            serialized_name="imdsAttestation",
            flags={"read_only": True},
        )
        reported_properties.last_updated = AAZStrType(
            serialized_name="lastUpdated",
            flags={"read_only": True},
        )
        reported_properties.manufacturer = AAZStrType(
            flags={"read_only": True},
        )
        reported_properties.nodes = AAZListType(
            flags={"read_only": True},
        )
        reported_properties.supported_capabilities = AAZListType(
            serialized_name="supportedCapabilities",
            flags={"read_only": True},
        )

        nodes = _schema_cluster_read.properties.reported_properties.nodes
        nodes.Element = AAZObjectType()

        _element = _schema_cluster_read.properties.reported_properties.nodes.Element
        _element.core_count = AAZFloatType(
            serialized_name="coreCount",
            flags={"read_only": True},
        )
        _element.ehc_resource_id = AAZStrType(
            serialized_name="ehcResourceId",
            flags={"read_only": True},
        )
        _element.id = AAZFloatType(
            flags={"read_only": True},
        )
        _element.last_licensing_timestamp = AAZStrType(
            serialized_name="lastLicensingTimestamp",
            flags={"read_only": True},
        )
        _element.manufacturer = AAZStrType(
            flags={"read_only": True},
        )
        _element.memory_in_gi_b = AAZFloatType(
            serialized_name="memoryInGiB",
            flags={"read_only": True},
        )
        _element.model = AAZStrType(
            flags={"read_only": True},
        )
        _element.name = AAZStrType(
            flags={"read_only": True},
        )
        _element.node_type = AAZStrType(
            serialized_name="nodeType",
            flags={"read_only": True},
        )
        _element.os_display_version = AAZStrType(
            serialized_name="osDisplayVersion",
            flags={"read_only": True},
        )
        _element.os_name = AAZStrType(
            serialized_name="osName",
            flags={"read_only": True},
        )
        _element.os_version = AAZStrType(
            serialized_name="osVersion",
            flags={"read_only": True},
        )
        _element.serial_number = AAZStrType(
            serialized_name="serialNumber",
            flags={"read_only": True},
        )
        _element.windows_server_subscription = AAZStrType(
            serialized_name="windowsServerSubscription",
            flags={"read_only": True},
        )

        supported_capabilities = _schema_cluster_read.properties.reported_properties.supported_capabilities
        supported_capabilities.Element = AAZStrType(
            flags={"read_only": True},
        )

        software_assurance_properties = _schema_cluster_read.properties.software_assurance_properties
        software_assurance_properties.last_updated = AAZStrType(
            serialized_name="lastUpdated",
            flags={"read_only": True},
        )
        software_assurance_properties.software_assurance_intent = AAZStrType(
            serialized_name="softwareAssuranceIntent",
        )
        software_assurance_properties.software_assurance_status = AAZStrType(
            serialized_name="softwareAssuranceStatus",
        )

        system_data = _schema_cluster_read.system_data
        system_data.created_at = AAZStrType(
            serialized_name="createdAt",
        )
        system_data.created_by = AAZStrType(
            serialized_name="createdBy",
        )
        system_data.created_by_type = AAZStrType(
            serialized_name="createdByType",
        )
        system_data.last_modified_at = AAZStrType(
            serialized_name="lastModifiedAt",
        )
        system_data.last_modified_by = AAZStrType(
            serialized_name="lastModifiedBy",
        )
        system_data.last_modified_by_type = AAZStrType(
            serialized_name="lastModifiedByType",
        )

        tags = _schema_cluster_read.tags
        tags.Element = AAZStrType()

        _schema.id = cls._schema_cluster_read.id
        _schema.identity = cls._schema_cluster_read.identity
        _schema.location = cls._schema_cluster_read.location
        _schema.name = cls._schema_cluster_read.name
        _schema.properties = cls._schema_cluster_read.properties
        _schema.system_data = cls._schema_cluster_read.system_data
        _schema.tags = cls._schema_cluster_read.tags
        _schema.type = cls._schema_cluster_read.type


__all__ = ["Update"]
