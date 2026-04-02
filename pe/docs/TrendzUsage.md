
# TrendzUsage

`tb_pe_client.models.TrendzUsage`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **used** | **bool** |  | [optional] |
| **anomaly_usage** | [**Entity**](Entity.md) |  | [optional] |
| **prediction_usage** | [**Entity**](Entity.md) |  | [optional] |
| **calculation_usage** | [**Entity**](Entity.md) |  | [optional] |
| **view_usage** | [**SimpleEntity**](SimpleEntity.md) |  | [optional] |
| **metric_usage** | [**SimpleEntity**](SimpleEntity.md) |  | [optional] |
| **chat_usage** | [**SimpleEntity**](SimpleEntity.md) |  | [optional] |



## Referenced Types

#### Entity
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| used | bool |  | [optional] |
| active_count | int |  | [optional] |
| total_count | int |  | [optional] |

#### SimpleEntity
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| used | bool |  | [optional] |
| total_count | int |  | [optional] |

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.used`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TrendzUsage.model_validate(data)` or `TrendzUsage.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

