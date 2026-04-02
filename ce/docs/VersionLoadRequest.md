
# VersionLoadRequest

`tb_ce_client.models.VersionLoadRequest`

Request for loading a version

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **version_id** | **str** |  | [optional] |
| **type** | [**VersionLoadRequestType**](VersionLoadRequestType.md) | Type of the version to load | |



## Subtypes

#### EntityTypeVersionLoadRequest  *(type=`ENTITY_TYPE`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| entity_types | Dict[str, EntityTypeVersionLoadConfig] |  | [optional] |
| rollback_on_error | bool |  | [optional] |

#### SingleEntityVersionLoadRequest  *(type=`SINGLE_ENTITY`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| external_entity_id | EntityId |  | [optional] |
| config | VersionLoadConfig |  | [optional] |

## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `CalculatedFieldId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityViewId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `QueueId`, `QueueStatsId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### VersionLoadRequestType (enum)
`SINGLE_ENTITY` | `ENTITY_TYPE`

#### EntityTypeVersionLoadConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| load_relations | bool |  | [optional] |
| load_attributes | bool |  | [optional] |
| load_credentials | bool |  | [optional] |
| load_calculated_fields | bool |  | [optional] |
| remove_other_entities | bool |  | [optional] |
| find_existing_entity_by_name | bool |  | [optional] |

#### VersionLoadConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| load_relations | bool |  | [optional] |
| load_attributes | bool |  | [optional] |
| load_credentials | bool |  | [optional] |
| load_calculated_fields | bool |  | [optional] |

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `RULE_CHAIN` | `RULE_NODE` | `ENTITY_VIEW` | … (36 values total)

---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.version_id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `VersionLoadRequest.model_validate(data)` or `VersionLoadRequest.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

