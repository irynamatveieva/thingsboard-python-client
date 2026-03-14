
# EntityVersion

`tb_pe_client.models.EntityVersion`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **timestamp** | **int** |  | [optional] |
| **id** | **str** |  | [optional] |
| **name** | **str** |  | [optional] |
| **author** | **str** |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.timestamp`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EntityVersion.model_validate(data)` or `EntityVersion.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

