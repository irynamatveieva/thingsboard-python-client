
# DataSource

`tb_paas_client.models.DataSource`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **type** | [**DataSourceType**](DataSourceType.md) |  | [optional] |
| **device_id** | **str** |  | [optional] |
| **entity_alias_id** | **str** |  | [optional] |
| **filter_id** | **str** |  | [optional] |
| **data_keys** | [**List[DataKey]**](DataKey.md) |  | [optional] |
| **latest_data_keys** | [**List[DataKey]**](DataKey.md) |  | [optional] |
| **alarm_filter_config** | [**AlarmFilterConfig**](AlarmFilterConfig.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.type`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `DataSource.model_validate(data)` or `DataSource.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

