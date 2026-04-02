
# KeyInfo

`tb_paas_client.models.KeyInfo`

Key name with an optional sample value.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **key** | **str** | Key name. | |
| **sample** | [**KeySample**](KeySample.md) | Most recent sample value for this key across the matched entities. Omitted when samples were not requested. | [optional] |



## Referenced Types

#### KeySample
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| ts | int | Timestamp in milliseconds since epoch. |  |
| value | object |  |  |

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.key`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `KeyInfo.model_validate(data)` or `KeyInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

