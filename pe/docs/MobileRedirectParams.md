
# MobileRedirectParams

`tb_pe_client.models.MobileRedirectParams`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **scheme** | **str** | Mobile application verification settings. Used for callback to mobile application once user is registered. | [optional] |
| **host** | **str** | Mobile application verification settings. Used for callback to mobile application once user is registered. | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.scheme`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `MobileRedirectParams.model_validate(data)` or `MobileRedirectParams.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

