
# StringFilterPredicate

`tb_pe_client.models.StringFilterPredicate`

**Extends:** **KeyFilterPredicate**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **operation** | [**StringOperation**](StringOperation.md) |  | [optional] |
| **value** | [**FilterPredicateValueString**](FilterPredicateValueString.md) | The value associated with the filter predicate | [optional] |
| **ignore_case** | **bool** |  | [optional] |



## Referenced Types

#### KeyFilterPredicate
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### StringOperation (enum)
`EQUAL` | `NOT_EQUAL` | `STARTS_WITH` | `ENDS_WITH` | `CONTAINS` | `NOT_CONTAINS` | `IN` | `NOT_IN`

#### FilterPredicateValueString
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| default_value | str |  | [optional] |
| user_value | str |  | [optional] |
| dynamic_value | DynamicValueString |  | [optional] |

#### DynamicValueString
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| resolved_value | str |  | [optional] |
| source_type | DynamicValueSourceType |  | [optional] |
| source_attribute | str |  | [optional] |
| inherit | bool |  | [optional] |

#### DynamicValueSourceType (enum)
`CURRENT_TENANT` | `CURRENT_CUSTOMER` | `CURRENT_USER` | `CURRENT_DEVICE`

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.operation`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `StringFilterPredicate.model_validate(data)` or `StringFilterPredicate.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

