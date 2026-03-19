#
# Copyright © 2026-2026 ThingsBoard, Inc.
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
#
# noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from tb_paas_client.models.tenant_profile_configuration import TenantProfileConfiguration
from typing import Optional, Set
from typing_extensions import Self

class DefaultTenantProfileConfiguration(TenantProfileConfiguration):
    """
    DefaultTenantProfileConfiguration
    """ # noqa: E501
    max_devices: Optional[StrictInt] = Field(default=None, alias="maxDevices")
    max_assets: Optional[StrictInt] = Field(default=None, alias="maxAssets")
    max_customers: Optional[StrictInt] = Field(default=None, alias="maxCustomers")
    max_users: Optional[StrictInt] = Field(default=None, alias="maxUsers")
    max_dashboards: Optional[StrictInt] = Field(default=None, alias="maxDashboards")
    max_rule_chains: Optional[StrictInt] = Field(default=None, alias="maxRuleChains")
    max_edges: Optional[StrictInt] = Field(default=None, alias="maxEdges")
    max_resources_in_bytes: Optional[StrictInt] = Field(default=None, alias="maxResourcesInBytes")
    max_ota_packages_in_bytes: Optional[StrictInt] = Field(default=None, alias="maxOtaPackagesInBytes")
    max_resource_size: Optional[StrictInt] = Field(default=None, alias="maxResourceSize")
    max_report_size_in_bytes: Optional[StrictInt] = Field(default=None, alias="maxReportSizeInBytes")
    max_integrations: Optional[StrictInt] = Field(default=None, alias="maxIntegrations")
    max_converters: Optional[StrictInt] = Field(default=None, alias="maxConverters")
    max_scheduler_events: Optional[StrictInt] = Field(default=None, alias="maxSchedulerEvents")
    white_labeling_enabled: Optional[StrictBool] = Field(default=None, alias="whiteLabelingEnabled")
    trendz_enabled: Optional[StrictBool] = Field(default=None, alias="trendzEnabled")
    edge_enabled: Optional[StrictBool] = Field(default=None, alias="edgeEnabled")
    transport_tenant_msg_rate_limit: Optional[StrictStr] = Field(default=None, alias="transportTenantMsgRateLimit")
    transport_tenant_telemetry_msg_rate_limit: Optional[StrictStr] = Field(default=None, alias="transportTenantTelemetryMsgRateLimit")
    transport_tenant_telemetry_data_points_rate_limit: Optional[StrictStr] = Field(default=None, alias="transportTenantTelemetryDataPointsRateLimit")
    transport_device_msg_rate_limit: Optional[StrictStr] = Field(default=None, alias="transportDeviceMsgRateLimit")
    transport_device_telemetry_msg_rate_limit: Optional[StrictStr] = Field(default=None, alias="transportDeviceTelemetryMsgRateLimit")
    transport_device_telemetry_data_points_rate_limit: Optional[StrictStr] = Field(default=None, alias="transportDeviceTelemetryDataPointsRateLimit")
    transport_gateway_msg_rate_limit: Optional[StrictStr] = Field(default=None, alias="transportGatewayMsgRateLimit")
    transport_gateway_telemetry_msg_rate_limit: Optional[StrictStr] = Field(default=None, alias="transportGatewayTelemetryMsgRateLimit")
    transport_gateway_telemetry_data_points_rate_limit: Optional[StrictStr] = Field(default=None, alias="transportGatewayTelemetryDataPointsRateLimit")
    transport_gateway_device_msg_rate_limit: Optional[StrictStr] = Field(default=None, alias="transportGatewayDeviceMsgRateLimit")
    transport_gateway_device_telemetry_msg_rate_limit: Optional[StrictStr] = Field(default=None, alias="transportGatewayDeviceTelemetryMsgRateLimit")
    transport_gateway_device_telemetry_data_points_rate_limit: Optional[StrictStr] = Field(default=None, alias="transportGatewayDeviceTelemetryDataPointsRateLimit")
    integration_msgs_per_tenant_rate_limit: Optional[StrictStr] = Field(default=None, alias="integrationMsgsPerTenantRateLimit")
    integration_msgs_per_device_rate_limit: Optional[StrictStr] = Field(default=None, alias="integrationMsgsPerDeviceRateLimit")
    integration_msgs_per_asset_rate_limit: Optional[StrictStr] = Field(default=None, alias="integrationMsgsPerAssetRateLimit")
    tenant_entity_export_rate_limit: Optional[StrictStr] = Field(default=None, alias="tenantEntityExportRateLimit")
    tenant_entity_import_rate_limit: Optional[StrictStr] = Field(default=None, alias="tenantEntityImportRateLimit")
    tenant_notification_requests_rate_limit: Optional[StrictStr] = Field(default=None, alias="tenantNotificationRequestsRateLimit")
    tenant_notification_requests_per_rule_rate_limit: Optional[StrictStr] = Field(default=None, alias="tenantNotificationRequestsPerRuleRateLimit")
    max_transport_messages: Optional[StrictInt] = Field(default=None, alias="maxTransportMessages")
    max_transport_data_points: Optional[StrictInt] = Field(default=None, alias="maxTransportDataPoints")
    max_re_executions: Optional[StrictInt] = Field(default=None, alias="maxREExecutions")
    max_js_executions: Optional[StrictInt] = Field(default=None, alias="maxJSExecutions")
    max_tbel_executions: Optional[StrictInt] = Field(default=None, alias="maxTbelExecutions")
    max_dp_storage_days: Optional[StrictInt] = Field(default=None, alias="maxDPStorageDays")
    max_rule_node_executions_per_message: Optional[StrictInt] = Field(default=None, alias="maxRuleNodeExecutionsPerMessage")
    max_debug_mode_duration_minutes: Optional[StrictInt] = Field(default=None, alias="maxDebugModeDurationMinutes")
    max_emails: Optional[StrictInt] = Field(default=None, alias="maxEmails")
    sms_enabled: Optional[StrictBool] = Field(default=None, alias="smsEnabled")
    max_sms: Optional[StrictInt] = Field(default=None, alias="maxSms")
    max_created_alarms: Optional[StrictInt] = Field(default=None, alias="maxCreatedAlarms")
    max_generated_reports: Optional[StrictInt] = Field(default=None, alias="maxGeneratedReports")
    max_ai_credits: Optional[StrictInt] = Field(default=None, alias="maxAiCredits")
    tenant_server_rest_limits_configuration: Optional[StrictStr] = Field(default=None, alias="tenantServerRestLimitsConfiguration")
    customer_server_rest_limits_configuration: Optional[StrictStr] = Field(default=None, alias="customerServerRestLimitsConfiguration")
    max_ws_sessions_per_tenant: Optional[StrictInt] = Field(default=None, alias="maxWsSessionsPerTenant")
    max_ws_sessions_per_customer: Optional[StrictInt] = Field(default=None, alias="maxWsSessionsPerCustomer")
    max_ws_sessions_per_regular_user: Optional[StrictInt] = Field(default=None, alias="maxWsSessionsPerRegularUser")
    max_ws_sessions_per_public_user: Optional[StrictInt] = Field(default=None, alias="maxWsSessionsPerPublicUser")
    ws_msg_queue_limit_per_session: Optional[StrictInt] = Field(default=None, alias="wsMsgQueueLimitPerSession")
    max_ws_subscriptions_per_tenant: Optional[StrictInt] = Field(default=None, alias="maxWsSubscriptionsPerTenant")
    max_ws_subscriptions_per_customer: Optional[StrictInt] = Field(default=None, alias="maxWsSubscriptionsPerCustomer")
    max_ws_subscriptions_per_regular_user: Optional[StrictInt] = Field(default=None, alias="maxWsSubscriptionsPerRegularUser")
    max_ws_subscriptions_per_public_user: Optional[StrictInt] = Field(default=None, alias="maxWsSubscriptionsPerPublicUser")
    ws_updates_per_session_rate_limit: Optional[StrictStr] = Field(default=None, alias="wsUpdatesPerSessionRateLimit")
    cassandra_read_query_tenant_core_rate_limits: Optional[StrictStr] = Field(default=None, alias="cassandraReadQueryTenantCoreRateLimits")
    cassandra_write_query_tenant_core_rate_limits: Optional[StrictStr] = Field(default=None, alias="cassandraWriteQueryTenantCoreRateLimits")
    cassandra_read_query_tenant_rule_engine_rate_limits: Optional[StrictStr] = Field(default=None, alias="cassandraReadQueryTenantRuleEngineRateLimits")
    cassandra_write_query_tenant_rule_engine_rate_limits: Optional[StrictStr] = Field(default=None, alias="cassandraWriteQueryTenantRuleEngineRateLimits")
    edge_event_rate_limits: Optional[StrictStr] = Field(default=None, alias="edgeEventRateLimits")
    edge_event_rate_limits_per_edge: Optional[StrictStr] = Field(default=None, alias="edgeEventRateLimitsPerEdge")
    edge_uplink_messages_rate_limits: Optional[StrictStr] = Field(default=None, alias="edgeUplinkMessagesRateLimits")
    edge_uplink_messages_rate_limits_per_edge: Optional[StrictStr] = Field(default=None, alias="edgeUplinkMessagesRateLimitsPerEdge")
    default_storage_ttl_days: Optional[StrictInt] = Field(default=None, alias="defaultStorageTtlDays")
    alarms_ttl_days: Optional[StrictInt] = Field(default=None, alias="alarmsTtlDays")
    rpc_ttl_days: Optional[StrictInt] = Field(default=None, alias="rpcTtlDays")
    queue_stats_ttl_days: Optional[StrictInt] = Field(default=None, alias="queueStatsTtlDays")
    rule_engine_exceptions_ttl_days: Optional[StrictInt] = Field(default=None, alias="ruleEngineExceptionsTtlDays")
    blob_entity_ttl_days: Optional[StrictInt] = Field(default=None, alias="blobEntityTtlDays")
    report_ttl_days: Optional[StrictInt] = Field(default=None, alias="reportTtlDays")
    warn_threshold: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="warnThreshold")
    max_calculated_fields_per_entity: Optional[StrictInt] = Field(default=None, alias="maxCalculatedFieldsPerEntity")
    max_arguments_per_cf: Optional[StrictInt] = Field(default=None, alias="maxArgumentsPerCF")
    min_allowed_scheduled_update_interval_in_sec_for_cf: Optional[StrictInt] = Field(default=None, alias="minAllowedScheduledUpdateIntervalInSecForCF")
    max_relation_level_per_cf_argument: Optional[StrictInt] = Field(default=None, alias="maxRelationLevelPerCfArgument")
    max_related_entities_to_return_per_cf_argument: Optional[StrictInt] = Field(default=None, alias="maxRelatedEntitiesToReturnPerCfArgument")
    max_data_points_per_rolling_arg: Optional[StrictInt] = Field(default=None, alias="maxDataPointsPerRollingArg")
    max_state_size_in_k_bytes: Optional[StrictInt] = Field(default=None, alias="maxStateSizeInKBytes")
    max_single_value_argument_size_in_k_bytes: Optional[StrictInt] = Field(default=None, alias="maxSingleValueArgumentSizeInKBytes")
    min_allowed_deduplication_interval_in_sec_for_cf: Optional[StrictInt] = Field(default=None, alias="minAllowedDeduplicationIntervalInSecForCF")
    min_allowed_aggregation_interval_in_sec_for_cf: Optional[StrictInt] = Field(default=None, alias="minAllowedAggregationIntervalInSecForCF")
    intermediate_aggregation_interval_in_sec_for_cf: Optional[StrictInt] = Field(default=None, alias="intermediateAggregationIntervalInSecForCF")
    cf_reevaluation_check_interval: Optional[StrictInt] = Field(default=None, alias="cfReevaluationCheckInterval")
    alarms_reevaluation_interval: Optional[StrictInt] = Field(default=None, alias="alarmsReevaluationInterval")
    ai_chat_requests_per_tenant_rate_limit: Optional[StrictStr] = Field(default=None, alias="aiChatRequestsPerTenantRateLimit")
    __properties: ClassVar[List[str]] = ["type", "maxDevices", "maxAssets", "maxCustomers", "maxUsers", "maxDashboards", "maxRuleChains", "maxEdges", "maxResourcesInBytes", "maxOtaPackagesInBytes", "maxResourceSize", "maxReportSizeInBytes", "maxIntegrations", "maxConverters", "maxSchedulerEvents", "whiteLabelingEnabled", "trendzEnabled", "edgeEnabled", "transportTenantMsgRateLimit", "transportTenantTelemetryMsgRateLimit", "transportTenantTelemetryDataPointsRateLimit", "transportDeviceMsgRateLimit", "transportDeviceTelemetryMsgRateLimit", "transportDeviceTelemetryDataPointsRateLimit", "transportGatewayMsgRateLimit", "transportGatewayTelemetryMsgRateLimit", "transportGatewayTelemetryDataPointsRateLimit", "transportGatewayDeviceMsgRateLimit", "transportGatewayDeviceTelemetryMsgRateLimit", "transportGatewayDeviceTelemetryDataPointsRateLimit", "integrationMsgsPerTenantRateLimit", "integrationMsgsPerDeviceRateLimit", "integrationMsgsPerAssetRateLimit", "tenantEntityExportRateLimit", "tenantEntityImportRateLimit", "tenantNotificationRequestsRateLimit", "tenantNotificationRequestsPerRuleRateLimit", "maxTransportMessages", "maxTransportDataPoints", "maxREExecutions", "maxJSExecutions", "maxTbelExecutions", "maxDPStorageDays", "maxRuleNodeExecutionsPerMessage", "maxDebugModeDurationMinutes", "maxEmails", "smsEnabled", "maxSms", "maxCreatedAlarms", "maxGeneratedReports", "maxAiCredits", "tenantServerRestLimitsConfiguration", "customerServerRestLimitsConfiguration", "maxWsSessionsPerTenant", "maxWsSessionsPerCustomer", "maxWsSessionsPerRegularUser", "maxWsSessionsPerPublicUser", "wsMsgQueueLimitPerSession", "maxWsSubscriptionsPerTenant", "maxWsSubscriptionsPerCustomer", "maxWsSubscriptionsPerRegularUser", "maxWsSubscriptionsPerPublicUser", "wsUpdatesPerSessionRateLimit", "cassandraReadQueryTenantCoreRateLimits", "cassandraWriteQueryTenantCoreRateLimits", "cassandraReadQueryTenantRuleEngineRateLimits", "cassandraWriteQueryTenantRuleEngineRateLimits", "edgeEventRateLimits", "edgeEventRateLimitsPerEdge", "edgeUplinkMessagesRateLimits", "edgeUplinkMessagesRateLimitsPerEdge", "defaultStorageTtlDays", "alarmsTtlDays", "rpcTtlDays", "queueStatsTtlDays", "ruleEngineExceptionsTtlDays", "blobEntityTtlDays", "reportTtlDays", "warnThreshold", "maxCalculatedFieldsPerEntity", "maxArgumentsPerCF", "minAllowedScheduledUpdateIntervalInSecForCF", "maxRelationLevelPerCfArgument", "maxRelatedEntitiesToReturnPerCfArgument", "maxDataPointsPerRollingArg", "maxStateSizeInKBytes", "maxSingleValueArgumentSizeInKBytes", "minAllowedDeduplicationIntervalInSecForCF", "minAllowedAggregationIntervalInSecForCF", "intermediateAggregationIntervalInSecForCF", "cfReevaluationCheckInterval", "alarmsReevaluationInterval", "aiChatRequestsPerTenantRateLimit"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of DefaultTenantProfileConfiguration from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DefaultTenantProfileConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "maxDevices": obj.get("maxDevices"),
            "maxAssets": obj.get("maxAssets"),
            "maxCustomers": obj.get("maxCustomers"),
            "maxUsers": obj.get("maxUsers"),
            "maxDashboards": obj.get("maxDashboards"),
            "maxRuleChains": obj.get("maxRuleChains"),
            "maxEdges": obj.get("maxEdges"),
            "maxResourcesInBytes": obj.get("maxResourcesInBytes"),
            "maxOtaPackagesInBytes": obj.get("maxOtaPackagesInBytes"),
            "maxResourceSize": obj.get("maxResourceSize"),
            "maxReportSizeInBytes": obj.get("maxReportSizeInBytes"),
            "maxIntegrations": obj.get("maxIntegrations"),
            "maxConverters": obj.get("maxConverters"),
            "maxSchedulerEvents": obj.get("maxSchedulerEvents"),
            "whiteLabelingEnabled": obj.get("whiteLabelingEnabled"),
            "trendzEnabled": obj.get("trendzEnabled"),
            "edgeEnabled": obj.get("edgeEnabled"),
            "transportTenantMsgRateLimit": obj.get("transportTenantMsgRateLimit"),
            "transportTenantTelemetryMsgRateLimit": obj.get("transportTenantTelemetryMsgRateLimit"),
            "transportTenantTelemetryDataPointsRateLimit": obj.get("transportTenantTelemetryDataPointsRateLimit"),
            "transportDeviceMsgRateLimit": obj.get("transportDeviceMsgRateLimit"),
            "transportDeviceTelemetryMsgRateLimit": obj.get("transportDeviceTelemetryMsgRateLimit"),
            "transportDeviceTelemetryDataPointsRateLimit": obj.get("transportDeviceTelemetryDataPointsRateLimit"),
            "transportGatewayMsgRateLimit": obj.get("transportGatewayMsgRateLimit"),
            "transportGatewayTelemetryMsgRateLimit": obj.get("transportGatewayTelemetryMsgRateLimit"),
            "transportGatewayTelemetryDataPointsRateLimit": obj.get("transportGatewayTelemetryDataPointsRateLimit"),
            "transportGatewayDeviceMsgRateLimit": obj.get("transportGatewayDeviceMsgRateLimit"),
            "transportGatewayDeviceTelemetryMsgRateLimit": obj.get("transportGatewayDeviceTelemetryMsgRateLimit"),
            "transportGatewayDeviceTelemetryDataPointsRateLimit": obj.get("transportGatewayDeviceTelemetryDataPointsRateLimit"),
            "integrationMsgsPerTenantRateLimit": obj.get("integrationMsgsPerTenantRateLimit"),
            "integrationMsgsPerDeviceRateLimit": obj.get("integrationMsgsPerDeviceRateLimit"),
            "integrationMsgsPerAssetRateLimit": obj.get("integrationMsgsPerAssetRateLimit"),
            "tenantEntityExportRateLimit": obj.get("tenantEntityExportRateLimit"),
            "tenantEntityImportRateLimit": obj.get("tenantEntityImportRateLimit"),
            "tenantNotificationRequestsRateLimit": obj.get("tenantNotificationRequestsRateLimit"),
            "tenantNotificationRequestsPerRuleRateLimit": obj.get("tenantNotificationRequestsPerRuleRateLimit"),
            "maxTransportMessages": obj.get("maxTransportMessages"),
            "maxTransportDataPoints": obj.get("maxTransportDataPoints"),
            "maxREExecutions": obj.get("maxREExecutions"),
            "maxJSExecutions": obj.get("maxJSExecutions"),
            "maxTbelExecutions": obj.get("maxTbelExecutions"),
            "maxDPStorageDays": obj.get("maxDPStorageDays"),
            "maxRuleNodeExecutionsPerMessage": obj.get("maxRuleNodeExecutionsPerMessage"),
            "maxDebugModeDurationMinutes": obj.get("maxDebugModeDurationMinutes"),
            "maxEmails": obj.get("maxEmails"),
            "smsEnabled": obj.get("smsEnabled"),
            "maxSms": obj.get("maxSms"),
            "maxCreatedAlarms": obj.get("maxCreatedAlarms"),
            "maxGeneratedReports": obj.get("maxGeneratedReports"),
            "maxAiCredits": obj.get("maxAiCredits"),
            "tenantServerRestLimitsConfiguration": obj.get("tenantServerRestLimitsConfiguration"),
            "customerServerRestLimitsConfiguration": obj.get("customerServerRestLimitsConfiguration"),
            "maxWsSessionsPerTenant": obj.get("maxWsSessionsPerTenant"),
            "maxWsSessionsPerCustomer": obj.get("maxWsSessionsPerCustomer"),
            "maxWsSessionsPerRegularUser": obj.get("maxWsSessionsPerRegularUser"),
            "maxWsSessionsPerPublicUser": obj.get("maxWsSessionsPerPublicUser"),
            "wsMsgQueueLimitPerSession": obj.get("wsMsgQueueLimitPerSession"),
            "maxWsSubscriptionsPerTenant": obj.get("maxWsSubscriptionsPerTenant"),
            "maxWsSubscriptionsPerCustomer": obj.get("maxWsSubscriptionsPerCustomer"),
            "maxWsSubscriptionsPerRegularUser": obj.get("maxWsSubscriptionsPerRegularUser"),
            "maxWsSubscriptionsPerPublicUser": obj.get("maxWsSubscriptionsPerPublicUser"),
            "wsUpdatesPerSessionRateLimit": obj.get("wsUpdatesPerSessionRateLimit"),
            "cassandraReadQueryTenantCoreRateLimits": obj.get("cassandraReadQueryTenantCoreRateLimits"),
            "cassandraWriteQueryTenantCoreRateLimits": obj.get("cassandraWriteQueryTenantCoreRateLimits"),
            "cassandraReadQueryTenantRuleEngineRateLimits": obj.get("cassandraReadQueryTenantRuleEngineRateLimits"),
            "cassandraWriteQueryTenantRuleEngineRateLimits": obj.get("cassandraWriteQueryTenantRuleEngineRateLimits"),
            "edgeEventRateLimits": obj.get("edgeEventRateLimits"),
            "edgeEventRateLimitsPerEdge": obj.get("edgeEventRateLimitsPerEdge"),
            "edgeUplinkMessagesRateLimits": obj.get("edgeUplinkMessagesRateLimits"),
            "edgeUplinkMessagesRateLimitsPerEdge": obj.get("edgeUplinkMessagesRateLimitsPerEdge"),
            "defaultStorageTtlDays": obj.get("defaultStorageTtlDays"),
            "alarmsTtlDays": obj.get("alarmsTtlDays"),
            "rpcTtlDays": obj.get("rpcTtlDays"),
            "queueStatsTtlDays": obj.get("queueStatsTtlDays"),
            "ruleEngineExceptionsTtlDays": obj.get("ruleEngineExceptionsTtlDays"),
            "blobEntityTtlDays": obj.get("blobEntityTtlDays"),
            "reportTtlDays": obj.get("reportTtlDays"),
            "warnThreshold": obj.get("warnThreshold"),
            "maxCalculatedFieldsPerEntity": obj.get("maxCalculatedFieldsPerEntity"),
            "maxArgumentsPerCF": obj.get("maxArgumentsPerCF"),
            "minAllowedScheduledUpdateIntervalInSecForCF": obj.get("minAllowedScheduledUpdateIntervalInSecForCF"),
            "maxRelationLevelPerCfArgument": obj.get("maxRelationLevelPerCfArgument"),
            "maxRelatedEntitiesToReturnPerCfArgument": obj.get("maxRelatedEntitiesToReturnPerCfArgument"),
            "maxDataPointsPerRollingArg": obj.get("maxDataPointsPerRollingArg"),
            "maxStateSizeInKBytes": obj.get("maxStateSizeInKBytes"),
            "maxSingleValueArgumentSizeInKBytes": obj.get("maxSingleValueArgumentSizeInKBytes"),
            "minAllowedDeduplicationIntervalInSecForCF": obj.get("minAllowedDeduplicationIntervalInSecForCF"),
            "minAllowedAggregationIntervalInSecForCF": obj.get("minAllowedAggregationIntervalInSecForCF"),
            "intermediateAggregationIntervalInSecForCF": obj.get("intermediateAggregationIntervalInSecForCF"),
            "cfReevaluationCheckInterval": obj.get("cfReevaluationCheckInterval"),
            "alarmsReevaluationInterval": obj.get("alarmsReevaluationInterval"),
            "aiChatRequestsPerTenantRateLimit": obj.get("aiChatRequestsPerTenantRateLimit")
        })
        return _obj


