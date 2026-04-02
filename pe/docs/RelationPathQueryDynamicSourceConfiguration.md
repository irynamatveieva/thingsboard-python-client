
# RelationPathQueryDynamicSourceConfiguration

`tb_pe_client.models.RelationPathQueryDynamicSourceConfiguration`

**Extends:** **CfArgumentDynamicSourceConfiguration**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **levels** | [**List[RelationPathLevel]**](RelationPathLevel.md) |  | [optional] |



## Referenced Types

#### CfArgumentDynamicSourceConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### CurrentOwnerDynamicSourceConfiguration  *(extends CfArgumentDynamicSourceConfiguration, type=`CURRENT_OWNER`)*
*See CfArgumentDynamicSourceConfiguration for properties.*

#### RelationPathLevel
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| direction | EntitySearchDirection |  |  |
| relation_type | str |  |  |

#### EntitySearchDirection (enum)
`FROM` | `TO`

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.levels`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `RelationPathQueryDynamicSourceConfiguration.model_validate(data)` or `RelationPathQueryDynamicSourceConfiguration.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

