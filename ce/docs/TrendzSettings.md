
# TrendzSettings

`tb_ce_client.models.TrendzSettings`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **enabled** | **bool** |  | [optional] |
| **base_url** | **str** |  | [optional] |
| **api_key** | **str** |  | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.enabled`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TrendzSettings.model_validate(data)` or `TrendzSettings.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

