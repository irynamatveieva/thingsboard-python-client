
# BooleanFilterPredicate

`tb_ce_client.models.BooleanFilterPredicate`

**Extends:** **KeyFilterPredicate**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **operation** | [**BooleanOperation**](BooleanOperation.md) |  | [optional] |
| **value** | [**FilterPredicateValueBoolean**](FilterPredicateValueBoolean.md) | The value associated with the filter predicate | [optional] |



## Referenced Types

#### KeyFilterPredicate
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### BooleanOperation (enum)
`EQUAL` | `NOT_EQUAL`

#### FilterPredicateValueBoolean
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| default_value | bool |  | [optional] |
| user_value | bool |  | [optional] |
| dynamic_value | DynamicValueBoolean |  | [optional] |

#### DynamicValueBoolean
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| resolved_value | bool |  | [optional] |
| source_type | DynamicValueSourceType |  | [optional] |
| source_attribute | str |  | [optional] |
| inherit | bool |  | [optional] |

#### DynamicValueSourceType (enum)
`CURRENT_TENANT` | `CURRENT_CUSTOMER` | `CURRENT_USER` | `CURRENT_DEVICE`

---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.operation`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `BooleanFilterPredicate.model_validate(data)` or `BooleanFilterPredicate.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

