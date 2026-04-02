
# PageDataEdgeEvent

`tb_ce_client.models.PageDataEdgeEvent`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **data** | [**List[EdgeEvent]**](EdgeEvent.md) | Array of the entities | [optional] |
| **total_pages** | **int** | Total number of available pages. Calculated based on the 'pageSize' request parameter and total number of entities that match search criteria | [optional] [readonly] |
| **total_elements** | **int** | Total number of elements in all available pages | [optional] [readonly] |
| **has_next** | **bool** | 'false' value indicates the end of the result set | [optional] [readonly] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `CalculatedFieldId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityViewId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `QueueId`, `QueueStatsId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### EdgeEvent
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | EdgeEventId |  | [optional] |
| created_time | int | Entity creation timestamp in milliseconds since Unix epoch | [optional] [readonly] |
| seq_id | int |  | [optional] |
| tenant_id | TenantId |  | [optional] |
| edge_id | EdgeId |  | [optional] |
| action | EdgeEventActionType |  | [optional] |
| entity_id | UUID |  | [optional] |
| uid | str |  | [optional] |
| type | EdgeEventType |  | [optional] |
| body | object |  | [optional] |

#### EdgeEventId
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | UUID | string |  |

#### EdgeEventActionType (enum)
`ADDED` | `UPDATED` | `DELETED` | `POST_ATTRIBUTES` | `ATTRIBUTES_UPDATED` | `ATTRIBUTES_DELETED` | `TIMESERIES_UPDATED` | `CREDENTIALS_UPDATED` | `ASSIGNED_TO_CUSTOMER` | `UNASSIGNED_FROM_CUSTOMER` | … (25 values total)

#### EdgeEventType (enum)
`DASHBOARD` | `ASSET` | `DEVICE` | `DEVICE_PROFILE` | `ASSET_PROFILE` | `ENTITY_VIEW` | `ALARM` | `ALARM_COMMENT` | `RULE_CHAIN` | `RULE_CHAIN_METADATA` | … (30 values total)

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `RULE_CHAIN` | `RULE_NODE` | `ENTITY_VIEW` | … (36 values total)

---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.data`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `PageDataEdgeEvent.model_validate(data)` or `PageDataEdgeEvent.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

