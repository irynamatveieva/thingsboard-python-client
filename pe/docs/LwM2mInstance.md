
# LwM2mInstance

`tb_pe_client.models.LwM2mInstance`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | **int** | LwM2M Instance id. | [optional] |
| **resources** | [**List[LwM2mResourceObserve]**](LwM2mResourceObserve.md) | LwM2M Resource observe. | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `LwM2mInstance.model_validate(data)` or `LwM2mInstance.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

