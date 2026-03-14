
# KeySample

`tb_pe_client.models.KeySample`

Most recent value and its timestamp.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **ts** | **int** | Timestamp in milliseconds since epoch. | |
| **value** | **object** |  | |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.ts`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `KeySample.model_validate(data)` or `KeySample.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

