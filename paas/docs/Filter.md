
# Filter

`tb_paas_client.models.Filter`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | **str** |  | [optional] |
| **filter** | **str** |  | [optional] |
| **key_filters** | [**List[KeyFilter]**](KeyFilter.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `Filter.model_validate(data)` or `Filter.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

