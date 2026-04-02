
# SchedulerEventExportData

`tb_paas_client.models.SchedulerEventExportData`

**Extends:** **EntityExportData**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|



## Referenced Types

> **EntityId types** (`CalculatedFieldId`, `TenantId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### EntityExportData
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| entity | ExportableEntity |  | [optional] |
| relations | List[EntityRelation] |  | [optional] |
| attributes | Dict[str, List[AttributeExportData]] | Map of attributes where key is the scope of attributes and value is the list of attributes for that scope | [optional] |
| calculated_fields | List[CalculatedField] |  | [optional] |
| entity_type | EntityType |  |  |

#### ExportableEntity
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | EntityId |  | [optional] |
| name | str |  | [optional] |

#### EntityRelation
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| var_from | EntityId | JSON object with [from] Entity Id. |  |
| to | EntityId | JSON object with [to] Entity Id. |  |
| type | str | String value of relation type. |  |
| type_group | RelationTypeGroup | Represents the type group of the relation. |  |
| version | int |  | [optional] |
| additional_info | object | Additional parameters of the relation. | [optional] |

#### CalculatedField
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | CalculatedFieldId | JSON object with the Calculated Field Id. Referencing non-existing Calculated Field Id will cause error. | [optional] |
| created_time | int | Timestamp of the calculated field creation, in milliseconds | [optional] [readonly] |
| tenant_id | TenantId |  | [optional] |
| entity_id | EntityId |  | [optional] |
| type | CalculatedFieldType |  | [optional] |
| name | str | User defined name of the calculated field. | [optional] |
| debug_settings | DebugSettings | Debug settings object. | [optional] |
| configuration_version | int | Version of calculated field configuration. | [optional] |
| configuration | CalculatedFieldConfiguration |  |  |
| version | int |  | [optional] |
| additional_info | object | Additional parameters of the calculated field | [optional] |
| debug_mode | bool |  | [optional] |

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (52 values total)

#### RelationTypeGroup (enum)
`COMMON` | `DASHBOARD` | `FROM_ENTITY_GROUP` | `RULE_CHAIN` | `RULE_NODE` | `EDGE` | `EDGE_AUTO_ASSIGN_RULE_CHAIN`

#### CalculatedFieldType (enum)
`SIMPLE` | `SCRIPT` | `GEOFENCING` | `ALARM` | `PROPAGATION` | `RELATED_ENTITIES_AGGREGATION` | `ENTITY_AGGREGATION`

#### DebugSettings
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| failures_enabled | bool | Debug failures. | [optional] |
| all_enabled | bool | Debug All. Used as a trigger for updating debugAllUntil. | [optional] |
| all_enabled_until | int | Timestamp of the end time for the processing debug events. | [optional] |

#### CalculatedFieldConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |
| output | Output |  | [optional] |
| ai_generated | bool |  | [optional] |

#### Output
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| name | str |  | [optional] |
| scope | AttributeScope |  | [optional] |
| decimals_by_default | int |  | [optional] |
| strategy | object |  | [optional] |
| type | str |  |  |

#### AttributeScope (enum)
`CLIENT_SCOPE` | `SERVER_SCOPE` | `SHARED_SCOPE`

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `SchedulerEventExportData.model_validate(data)` or `SchedulerEventExportData.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

