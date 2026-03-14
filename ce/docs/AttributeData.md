
# AttributeData

`tb_ce_client.models.AttributeData`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **last_update_ts** | **int** | Timestamp last updated attribute, in milliseconds | [optional] [readonly] |
| **key** | **str** | String representing attribute key | [optional] [readonly] |
| **value** | **object** |  | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.last_update_ts`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AttributeData.model_validate(data)` or `AttributeData.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

