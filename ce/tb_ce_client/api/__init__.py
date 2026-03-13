#
# Copyright 2026 ThingsBoard, Inc.
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
import importlib
from typing import TYPE_CHECKING

__all__ = [
    "AdminControllerApi",
    "AiModelControllerApi",
    "AlarmCommentControllerApi",
    "AlarmControllerApi",
    "ApiKeyControllerApi",
    "AssetControllerApi",
    "AssetProfileControllerApi",
    "AuditLogControllerApi",
    "AuthControllerApi",
    "CalculatedFieldControllerApi",
    "ComponentDescriptorControllerApi",
    "CustomerControllerApi",
    "DashboardControllerApi",
    "DeviceConnectivityControllerApi",
    "DeviceControllerApi",
    "DeviceProfileControllerApi",
    "DomainControllerApi",
    "EdgeControllerApi",
    "EdgeEventControllerApi",
    "EntitiesVersionControlControllerApi",
    "EntityQueryControllerApi",
    "EntityRelationControllerApi",
    "EntityViewControllerApi",
    "EventControllerApi",
    "ImageControllerApi",
    "JobControllerApi",
    "LoginEndpointApi",
    "Lwm2mControllerApi",
    "MailConfigTemplateControllerApi",
    "MobileAppBundleControllerApi",
    "MobileAppControllerApi",
    "NotificationControllerApi",
    "NotificationRuleControllerApi",
    "NotificationTargetControllerApi",
    "NotificationTemplateControllerApi",
    "OAuth2ConfigTemplateControllerApi",
    "OAuth2ControllerApi",
    "OtaPackageControllerApi",
    "QrCodeSettingsControllerApi",
    "QueueControllerApi",
    "QueueStatsControllerApi",
    "RpcV1ControllerApi",
    "RpcV2ControllerApi",
    "RuleChainControllerApi",
    "RuleEngineControllerApi",
    "TbResourceControllerApi",
    "TelemetryControllerApi",
    "TenantControllerApi",
    "TenantProfileControllerApi",
    "TrendzControllerApi",
    "TwoFactorAuthConfigControllerApi",
    "TwoFactorAuthControllerApi",
    "UiSettingsControllerApi",
    "UsageInfoControllerApi",
    "UserControllerApi",
    "WidgetTypeControllerApi",
    "WidgetsBundleControllerApi",
]

if TYPE_CHECKING:
    from tb_ce_client.api.admin_controller_api import AdminControllerApi
    from tb_ce_client.api.ai_model_controller_api import AiModelControllerApi
    from tb_ce_client.api.alarm_comment_controller_api import AlarmCommentControllerApi
    from tb_ce_client.api.alarm_controller_api import AlarmControllerApi
    from tb_ce_client.api.api_key_controller_api import ApiKeyControllerApi
    from tb_ce_client.api.asset_controller_api import AssetControllerApi
    from tb_ce_client.api.asset_profile_controller_api import AssetProfileControllerApi
    from tb_ce_client.api.audit_log_controller_api import AuditLogControllerApi
    from tb_ce_client.api.auth_controller_api import AuthControllerApi
    from tb_ce_client.api.calculated_field_controller_api import CalculatedFieldControllerApi
    from tb_ce_client.api.component_descriptor_controller_api import ComponentDescriptorControllerApi
    from tb_ce_client.api.customer_controller_api import CustomerControllerApi
    from tb_ce_client.api.dashboard_controller_api import DashboardControllerApi
    from tb_ce_client.api.device_connectivity_controller_api import DeviceConnectivityControllerApi
    from tb_ce_client.api.device_controller_api import DeviceControllerApi
    from tb_ce_client.api.device_profile_controller_api import DeviceProfileControllerApi
    from tb_ce_client.api.domain_controller_api import DomainControllerApi
    from tb_ce_client.api.edge_controller_api import EdgeControllerApi
    from tb_ce_client.api.edge_event_controller_api import EdgeEventControllerApi
    from tb_ce_client.api.entities_version_control_controller_api import EntitiesVersionControlControllerApi
    from tb_ce_client.api.entity_query_controller_api import EntityQueryControllerApi
    from tb_ce_client.api.entity_relation_controller_api import EntityRelationControllerApi
    from tb_ce_client.api.entity_view_controller_api import EntityViewControllerApi
    from tb_ce_client.api.event_controller_api import EventControllerApi
    from tb_ce_client.api.image_controller_api import ImageControllerApi
    from tb_ce_client.api.job_controller_api import JobControllerApi
    from tb_ce_client.api.login_endpoint_api import LoginEndpointApi
    from tb_ce_client.api.lwm2m_controller_api import Lwm2mControllerApi
    from tb_ce_client.api.mail_config_template_controller_api import MailConfigTemplateControllerApi
    from tb_ce_client.api.mobile_app_bundle_controller_api import MobileAppBundleControllerApi
    from tb_ce_client.api.mobile_app_controller_api import MobileAppControllerApi
    from tb_ce_client.api.notification_controller_api import NotificationControllerApi
    from tb_ce_client.api.notification_rule_controller_api import NotificationRuleControllerApi
    from tb_ce_client.api.notification_target_controller_api import NotificationTargetControllerApi
    from tb_ce_client.api.notification_template_controller_api import NotificationTemplateControllerApi
    from tb_ce_client.api.o_auth2_config_template_controller_api import OAuth2ConfigTemplateControllerApi
    from tb_ce_client.api.o_auth2_controller_api import OAuth2ControllerApi
    from tb_ce_client.api.ota_package_controller_api import OtaPackageControllerApi
    from tb_ce_client.api.qr_code_settings_controller_api import QrCodeSettingsControllerApi
    from tb_ce_client.api.queue_controller_api import QueueControllerApi
    from tb_ce_client.api.queue_stats_controller_api import QueueStatsControllerApi
    from tb_ce_client.api.rpc_v1_controller_api import RpcV1ControllerApi
    from tb_ce_client.api.rpc_v2_controller_api import RpcV2ControllerApi
    from tb_ce_client.api.rule_chain_controller_api import RuleChainControllerApi
    from tb_ce_client.api.rule_engine_controller_api import RuleEngineControllerApi
    from tb_ce_client.api.tb_resource_controller_api import TbResourceControllerApi
    from tb_ce_client.api.telemetry_controller_api import TelemetryControllerApi
    from tb_ce_client.api.tenant_controller_api import TenantControllerApi
    from tb_ce_client.api.tenant_profile_controller_api import TenantProfileControllerApi
    from tb_ce_client.api.trendz_controller_api import TrendzControllerApi
    from tb_ce_client.api.two_factor_auth_config_controller_api import TwoFactorAuthConfigControllerApi
    from tb_ce_client.api.two_factor_auth_controller_api import TwoFactorAuthControllerApi
    from tb_ce_client.api.ui_settings_controller_api import UiSettingsControllerApi
    from tb_ce_client.api.usage_info_controller_api import UsageInfoControllerApi
    from tb_ce_client.api.user_controller_api import UserControllerApi
    from tb_ce_client.api.widget_type_controller_api import WidgetTypeControllerApi
    from tb_ce_client.api.widgets_bundle_controller_api import WidgetsBundleControllerApi

_API_CLASSES = {
    "AdminControllerApi": "tb_ce_client.api.admin_controller_api",
    "AiModelControllerApi": "tb_ce_client.api.ai_model_controller_api",
    "AlarmCommentControllerApi": "tb_ce_client.api.alarm_comment_controller_api",
    "AlarmControllerApi": "tb_ce_client.api.alarm_controller_api",
    "ApiKeyControllerApi": "tb_ce_client.api.api_key_controller_api",
    "AssetControllerApi": "tb_ce_client.api.asset_controller_api",
    "AssetProfileControllerApi": "tb_ce_client.api.asset_profile_controller_api",
    "AuditLogControllerApi": "tb_ce_client.api.audit_log_controller_api",
    "AuthControllerApi": "tb_ce_client.api.auth_controller_api",
    "CalculatedFieldControllerApi": "tb_ce_client.api.calculated_field_controller_api",
    "ComponentDescriptorControllerApi": "tb_ce_client.api.component_descriptor_controller_api",
    "CustomerControllerApi": "tb_ce_client.api.customer_controller_api",
    "DashboardControllerApi": "tb_ce_client.api.dashboard_controller_api",
    "DeviceConnectivityControllerApi": "tb_ce_client.api.device_connectivity_controller_api",
    "DeviceControllerApi": "tb_ce_client.api.device_controller_api",
    "DeviceProfileControllerApi": "tb_ce_client.api.device_profile_controller_api",
    "DomainControllerApi": "tb_ce_client.api.domain_controller_api",
    "EdgeControllerApi": "tb_ce_client.api.edge_controller_api",
    "EdgeEventControllerApi": "tb_ce_client.api.edge_event_controller_api",
    "EntitiesVersionControlControllerApi": "tb_ce_client.api.entities_version_control_controller_api",
    "EntityQueryControllerApi": "tb_ce_client.api.entity_query_controller_api",
    "EntityRelationControllerApi": "tb_ce_client.api.entity_relation_controller_api",
    "EntityViewControllerApi": "tb_ce_client.api.entity_view_controller_api",
    "EventControllerApi": "tb_ce_client.api.event_controller_api",
    "ImageControllerApi": "tb_ce_client.api.image_controller_api",
    "JobControllerApi": "tb_ce_client.api.job_controller_api",
    "LoginEndpointApi": "tb_ce_client.api.login_endpoint_api",
    "Lwm2mControllerApi": "tb_ce_client.api.lwm2m_controller_api",
    "MailConfigTemplateControllerApi": "tb_ce_client.api.mail_config_template_controller_api",
    "MobileAppBundleControllerApi": "tb_ce_client.api.mobile_app_bundle_controller_api",
    "MobileAppControllerApi": "tb_ce_client.api.mobile_app_controller_api",
    "NotificationControllerApi": "tb_ce_client.api.notification_controller_api",
    "NotificationRuleControllerApi": "tb_ce_client.api.notification_rule_controller_api",
    "NotificationTargetControllerApi": "tb_ce_client.api.notification_target_controller_api",
    "NotificationTemplateControllerApi": "tb_ce_client.api.notification_template_controller_api",
    "OAuth2ConfigTemplateControllerApi": "tb_ce_client.api.o_auth2_config_template_controller_api",
    "OAuth2ControllerApi": "tb_ce_client.api.o_auth2_controller_api",
    "OtaPackageControllerApi": "tb_ce_client.api.ota_package_controller_api",
    "QrCodeSettingsControllerApi": "tb_ce_client.api.qr_code_settings_controller_api",
    "QueueControllerApi": "tb_ce_client.api.queue_controller_api",
    "QueueStatsControllerApi": "tb_ce_client.api.queue_stats_controller_api",
    "RpcV1ControllerApi": "tb_ce_client.api.rpc_v1_controller_api",
    "RpcV2ControllerApi": "tb_ce_client.api.rpc_v2_controller_api",
    "RuleChainControllerApi": "tb_ce_client.api.rule_chain_controller_api",
    "RuleEngineControllerApi": "tb_ce_client.api.rule_engine_controller_api",
    "TbResourceControllerApi": "tb_ce_client.api.tb_resource_controller_api",
    "TelemetryControllerApi": "tb_ce_client.api.telemetry_controller_api",
    "TenantControllerApi": "tb_ce_client.api.tenant_controller_api",
    "TenantProfileControllerApi": "tb_ce_client.api.tenant_profile_controller_api",
    "TrendzControllerApi": "tb_ce_client.api.trendz_controller_api",
    "TwoFactorAuthConfigControllerApi": "tb_ce_client.api.two_factor_auth_config_controller_api",
    "TwoFactorAuthControllerApi": "tb_ce_client.api.two_factor_auth_controller_api",
    "UiSettingsControllerApi": "tb_ce_client.api.ui_settings_controller_api",
    "UsageInfoControllerApi": "tb_ce_client.api.usage_info_controller_api",
    "UserControllerApi": "tb_ce_client.api.user_controller_api",
    "WidgetTypeControllerApi": "tb_ce_client.api.widget_type_controller_api",
    "WidgetsBundleControllerApi": "tb_ce_client.api.widgets_bundle_controller_api",
}

def __getattr__(name: str):
    if name in _API_CLASSES:
        module = importlib.import_module(_API_CLASSES[name])
        cls = getattr(module, name)
        globals()[name] = cls  # Cache for subsequent access
        return cls
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

def __dir__():
    return list(_API_CLASSES.keys())
