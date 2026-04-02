
# VersionCreateRequest

`tb_ce_client.models.VersionCreateRequest`

Request for creating a version

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **version_name** | **str** |  | [optional] |
| **branch** | **str** |  | [optional] |
| **type** | [**VersionCreateRequestType**](VersionCreateRequestType.md) | Type of the version to create | |



## Subtypes

#### ComplexVersionCreateRequest  *(type=`COMPLEX`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| sync_strategy | SyncStrategy |  | [optional] |
| entity_types | Dict[str, EntityTypeVersionCreateConfig] |  | [optional] |

#### SingleEntityVersionCreateRequest  *(type=`SINGLE_ENTITY`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| entity_id | EntityId |  | [optional] |
| config | VersionCreateConfig |  | [optional] |

## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `CalculatedFieldId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityViewId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `QueueId`, `QueueStatsId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### VersionCreateRequestType (enum)
`SINGLE_ENTITY` | `COMPLEX`

#### SyncStrategy (enum)
`MERGE` | `OVERWRITE`

#### EntityTypeVersionCreateConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| save_relations | bool |  | [optional] |
| save_attributes | bool |  | [optional] |
| save_credentials | bool |  | [optional] |
| save_calculated_fields | bool |  | [optional] |
| sync_strategy | SyncStrategy |  | [optional] |
| entity_ids | List[UUID] |  | [optional] |
| all_entities | bool |  | [optional] |

#### VersionCreateConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| save_relations | bool |  | [optional] |
| save_attributes | bool |  | [optional] |
| save_credentials | bool |  | [optional] |
| save_calculated_fields | bool |  | [optional] |

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `RULE_CHAIN` | `RULE_NODE` | `ENTITY_VIEW` | … (36 values total)

---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.version_name`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `VersionCreateRequest.model_validate(data)` or `VersionCreateRequest.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

