
# LwM2mResourceObserve

`tb_pe_client.models.LwM2mResourceObserve`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | **int** | LwM2M Resource Observe id. | [optional] |
| **name** | **str** | LwM2M Resource Observe name. | [optional] |
| **observe** | **bool** | LwM2M Resource Observe observe. | [optional] |
| **attribute** | **bool** | LwM2M Resource Observe attribute. | [optional] |
| **telemetry** | **bool** | LwM2M Resource Observe telemetry. | [optional] |
| **key_name** | **str** | LwM2M Resource Observe key name. | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `LwM2mResourceObserve.model_validate(data)` or `LwM2mResourceObserve.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

