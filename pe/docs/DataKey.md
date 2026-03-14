
# DataKey

`tb_pe_client.models.DataKey`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **name** | **str** |  | [optional] |
| **type** | **str** |  | [optional] |
| **label** | **str** |  | [optional] |
| **color** | **str** |  | [optional] |
| **decimals** | **int** |  | [optional] |
| **units** | **str** |  | [optional] |
| **aggregation_type** | [**Aggregation**](Aggregation.md) |  | [optional] |
| **timewindow** | [**TimeWindowConfiguration**](TimeWindowConfiguration.md) |  | [optional] |
| **use_post_processing** | **bool** |  | [optional] |
| **post_func_body** | **str** |  | [optional] |
| **settings** | [**DataKeySettings**](DataKeySettings.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.name`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `DataKey.model_validate(data)` or `DataKey.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

