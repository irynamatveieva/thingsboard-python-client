
# TrendzConfiguration

`tb_paas_client.models.TrendzConfiguration`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **trendz_url** | **str** |  | [optional] |
| **tb_url** | **str** |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.trendz_url`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TrendzConfiguration.model_validate(data)` or `TrendzConfiguration.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

