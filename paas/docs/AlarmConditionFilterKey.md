
# AlarmConditionFilterKey

`tb_paas_client.models.AlarmConditionFilterKey`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **type** | [**AlarmConditionKeyType**](AlarmConditionKeyType.md) | The key type | [optional] |
| **key** | **str** | String value representing the key | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.type`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmConditionFilterKey.model_validate(data)` or `AlarmConditionFilterKey.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

