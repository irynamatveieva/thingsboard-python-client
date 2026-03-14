
# EntityCoordinates

`tb_pe_client.models.EntityCoordinates`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **latitude_key_name** | **str** |  | |
| **longitude_key_name** | **str** |  | |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.latitude_key_name`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EntityCoordinates.model_validate(data)` or `EntityCoordinates.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

