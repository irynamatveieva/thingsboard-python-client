
# Font

`tb_paas_client.models.Font`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **size** | **float** |  | [optional] |
| **weight** | [**FontWeight**](FontWeight.md) |  | [optional] |
| **style** | [**FontStyle**](FontStyle.md) |  | [optional] |
| **family** | **str** |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.size`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `Font.model_validate(data)` or `Font.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

