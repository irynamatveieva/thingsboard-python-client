
# IntegrationConvertersInfo

`tb_paas_client.models.IntegrationConvertersInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **uplink** | [**ConvertersInfo**](ConvertersInfo.md) |  | [optional] |
| **downlink** | [**ConvertersInfo**](ConvertersInfo.md) |  | [optional] |



## Referenced Types

#### ConvertersInfo
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| library | bool |  | [optional] |
| existing | bool |  | [optional] |
| keys | List[str] |  | [optional] |

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.uplink`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `IntegrationConvertersInfo.model_validate(data)` or `IntegrationConvertersInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

