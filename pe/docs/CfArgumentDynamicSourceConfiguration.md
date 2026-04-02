
# CfArgumentDynamicSourceConfiguration

`tb_pe_client.models.CfArgumentDynamicSourceConfiguration`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **type** | **str** |  | |



## Subtypes

#### CurrentOwnerDynamicSourceConfiguration  *(type=`CURRENT_OWNER`)*
*(no additional properties)*

#### RelationPathQueryDynamicSourceConfiguration  *(type=`RELATION_PATH_QUERY`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| levels | List[RelationPathLevel] |  | [optional] |

## Referenced Types

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
- **Attribute access:** `obj.type`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `CfArgumentDynamicSourceConfiguration.model_validate(data)` or `CfArgumentDynamicSourceConfiguration.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

